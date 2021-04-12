from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import logging
import json


class ComputeServer(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/productionplan":
            self._set_error()
            logging.error("\nInvalid path: %s\n", str(self.path))
            return

        try:
            payload = self._read_data()
            logging.info("\nPOST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                         str(self.path), str(self.headers), payload)

            compute = Compute(payload)
            compute.try_solve(0, payload.get("load"), [])
            result = compute.find_best()

            logging.debug("\nInvalid solution computed: %s\nValid solution computed: %s\n",
                          str(compute.failed_solution), str(len(compute.all_solution)))

            if result is None:
                self._set_no_solution()
                logging.error("\nNo solution found\n")
                return

            self._set_response()
            self._write_data(result)

        except RuntimeError as e:
            logging.exception(str(e))
            self._set_internal_error()
            return

    def _set_response(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _set_error(self):
        self.send_response(HTTPStatus.NOT_FOUND)
        self.end_headers()

    def _set_internal_error(self):
        self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
        self.end_headers()

    def _set_no_solution(self):
        self.send_response(HTTPStatus.BAD_REQUEST)
        self.end_headers()

    def _read_data(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        json_data = post_data.decode('utf8')
        return json.loads(json_data)

    def _write_data(self, result):
        json_data = json.dumps(result)
        logging.info("\nSolution: %s\n", str(json_data))
        self.wfile.write(json_data.encode('utf-8'))


class Compute:
    def __init__(self, payload):
        self.raw_power_plants = []
        self.power_plants = []
        self.all_solution = []
        self.failed_solution = 0
        self.fuels = Fuels(payload.get("fuels"))
        self._create_power_plants(payload)

    def find_best(self):
        self._compute_price()
        best_solution = None
        for solution in self.all_solution:
            if best_solution is None:
                best_solution = solution
                continue

            if best_solution.price > solution.price:
                best_solution = solution

        return self._get_solution(best_solution)

    def try_solve(self, index, load, power_plants_usage):
        at_least_one_solution_exist = False
        for i in range(index, len(self.power_plants)):
            power_plant = self.power_plants[i]
            if power_plant.power_min < load:
                # simple solution, but may failed
                power = power_plant.power_max if power_plant.power_max < load else load
                load -= power
                power_plants_usage.append(PowerPlantUsage(power_plant, power))
            else:
                if len(power_plants_usage) > 0:
                    # we fork the solution, a best one can exist by load balancing
                    if not self._try_load_balancing(load, power_plants_usage, power_plant):
                        # we fork the solution, a best one may exist by forcing the usage of the current power plant
                        at_least_one_solution_exist |= self._try_force_power_plant(load, power_plants_usage,
                                                                                   power_plant)
                    else:
                        at_least_one_solution_exist = True

            if load == 0:
                # this is a valid solution maybe not the best one
                self.all_solution.append(Solution(power_plants_usage, None))
                return True

        self.failed_solution += 1
        return at_least_one_solution_exist

    def _copy_power_plants_usage(self, power_plants_usage):
        copy = []
        for power_plant_usage in power_plants_usage:
            copy.append(PowerPlantUsage(power_plant_usage.power_plant, power_plant_usage.power))
        return copy

    def _get_solution(self, best_solution):
        if best_solution is None:
            return None

        usage = {}
        for power_plant_usage in best_solution.power_plants_usage:
            usage[power_plant_usage.power_plant.name] = power_plant_usage.power

        solution = []
        for power_plant in self.raw_power_plants:
            power = usage.get(power_plant.name, 0)
            solution.append({"name": power_plant.name, "p": power})

        return solution

    def _compute_price(self):
        for solution in self.all_solution:
            solution.price = 0
            for power_plant_usage in solution.power_plants_usage:
                solution.price += power_plant_usage.power * power_plant_usage.power_plant.price

    def _create_power_plants(self, payload):
        for raw_power_plant in payload.get("powerplants"):
            power_plant = PowerPlant(raw_power_plant, self.fuels)
            self.power_plants.append(power_plant)

        self.raw_power_plants = self.power_plants.copy()
        self.power_plants.sort(key=lambda x: (x.price, -x.power_max))
        for i in range(len(self.power_plants)):
            self.power_plants[i].index = i

    def _try_load_balancing(self, load, power_plants_usage, power_plant):
        prev_power_plants_usage = self._copy_power_plants_usage(power_plants_usage)
        missing_power = power_plant.power_min - load
        for i in range(len(prev_power_plants_usage) - 1, -1, -1):
            prev_power_plan_usage = prev_power_plants_usage[i]
            if prev_power_plan_usage.power > prev_power_plan_usage.power_plant.power_min:
                if missing_power <= prev_power_plan_usage.power - prev_power_plan_usage.power_plant.power_min:
                    prev_power_plan_usage.power -= missing_power
                    prev_power_plants_usage.append(PowerPlantUsage(power_plant, missing_power + load))
                    self.all_solution.append(Solution(prev_power_plants_usage, None))
                    return True
                else:
                    gain_power = prev_power_plan_usage.power - prev_power_plan_usage.power_plant.power_min
                    load += gain_power
                    missing_power -= gain_power
                    prev_power_plan_usage.power = prev_power_plan_usage.power_plant.power_min

        self.failed_solution += 1
        return False

    def _try_force_power_plant(self, load, power_plants_usage, power_plant):
        prev_power_plants_usage = self._copy_power_plants_usage(power_plants_usage)
        for i in range(len(prev_power_plants_usage) - 1, -1, -1):
            prev_power_plan_usage = prev_power_plants_usage.pop(i)
            load += prev_power_plan_usage.power
            if power_plant.power_min - load <= 0:
                return self.try_solve(power_plant.index, load, prev_power_plants_usage)

        self.failed_solution += 1
        return False


class Solution:
    def __init__(self, power_plants_usage, price):
        self.power_plants_usage = power_plants_usage
        self.price = price


class PowerPlantUsage:
    def __init__(self, power_plant, power):
        self.power_plant = power_plant
        self.power = power


class Fuels:
    def __init__(self, fuels):
        self.gas_price = fuels.get("gas(euro/MWh)")
        self.kerosine_price = fuels.get("kerosine(euro/MWh)")
        self.co2_price = fuels.get("co2(euro/ton)")
        self.wind_power = fuels.get("wind(%)")


class PowerPlant:
    def __init__(self, power_plant, fuels):
        self.ton_per_mwh = 0.3  # gasfired & turbojet
        self.fuels = fuels
        self._init_fct = {
            "gasfired": self._init_gas_fired,
            "turbojet": self._init_turbo_jet,
            "windturbine": self._init_wind_turbine,
            "undefined": self._undefined,
        }

        self.index = None
        self.price = None
        self.name = power_plant.get("name")
        self.type = power_plant.get("type")
        self.efficiency = power_plant.get("efficiency")
        self.power_min = power_plant.get("pmin")
        self.power_max = power_plant.get("pmax")
        self._init_fct.get(self.type, "undefined")()

    def _init_gas_fired(self):
        self._init_fuel(self.fuels.gas_price)

    def _init_turbo_jet(self):
        self._init_fuel(self.fuels.kerosine_price)

    def _init_wind_turbine(self):
        self.price = 0
        self.power_max = round(self.power_max * (self.fuels.wind_power / 100), 1)
        self.power_min = self.power_max

    def _undefined(self):
        self.power_min = None
        self.power_max = None

    def _init_fuel(self, fuel_price):
        self.price = (1 / self.efficiency) * ((self.fuels.co2_price * self.ton_per_mwh) + fuel_price)


def run(server_class=HTTPServer, handler_class=ComputeServer, port=8888):
    logging.basicConfig(format='%(asctime)s %(message)s', filename='/logs/server.log', level=logging.DEBUG)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info("\nStarting server...\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("\nStopping server...\n")


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
