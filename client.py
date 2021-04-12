import http.client
import json

payload1 = {
    "load": 480,
    "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 60
        },
    "powerplants": [
        {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredsomewhatsmaller",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 210
        },
        {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
        },
        {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
        },
        {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
        }
    ]
}

payload2 = {
    "load": 480,
    "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 0
        },
    "powerplants": [
        {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredsomewhatsmaller",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 210
        },
        {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
        },
        {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
        },
        {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
        }
    ]
}

payload3 = {
    "load": 910,
    "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 60
        },
    "powerplants": [
        {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredsomewhatsmaller",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 210
        },
        {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
        },
        {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
        },
        {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
        }
    ]
}

payload4 = {
    "load": 180,
    "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 100
        },
    "powerplants": [
        {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredsomewhatsmaller1",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 100
        },
        {
            "name": "gasfiredsomewhatsmaller2",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 100,
            "pmax": 210
        },
        {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
        },
        {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
        },
        {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
        }
    ]
}

payload5 = {
    "load": 15,
    "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 100
        },
    "powerplants": [
        {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredsomewhatsmaller1",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 100
        },
        {
            "name": "gasfiredsomewhatsmaller2",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 100,
            "pmax": 210
        },
        {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
        },
        {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
        },
        {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
        }
    ]
}

payload6 = {
    "load": 17,
    "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 100
        },
    "powerplants": [
        {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredsomewhatsmaller1",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 100
        },
        {
            "name": "gasfiredsomewhatsmaller2",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 100,
            "pmax": 210
        },
        {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
        },
        {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
        },
        {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
        }
    ]
}

payload7 = {
    "load": 40,
    "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 100
        },
    "powerplants": [
        {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredsomewhatsmaller1",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 100
        },
        {
            "name": "gasfiredsomewhatsmaller2",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 100,
            "pmax": 210
        },
        {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
        },
        {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
        },
        {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
        }
    ]
}

payload8 = {
    "load": 52,
    "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 100
        },
    "powerplants": [
        {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredsomewhatsmaller1",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 100
        },
        {
            "name": "gasfiredsomewhatsmaller2",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 100,
            "pmax": 210
        },
        {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
        },
        {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
        },
        {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
        }
    ]
}

payload9 = {
    "load": 135,
    "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 100
        },
    "powerplants": [
        {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
        },
        {
            "name": "gasfiredsomewhatsmaller1",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 100
        },
        {
            "name": "gasfiredsomewhatsmaller2",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 100,
            "pmax": 210
        },
        {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
        },
        {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
        },
        {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
        }
    ]
}

payload10 = {
    "load": 930,
    "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 100
        },
    "powerplants": [
        {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 400,
            "pmax": 460
        },
        {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 400,
            "pmax": 460
        },
        {
            "name": "gasfiredsomewhatsmaller1",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 100,
            "pmax": 210
        }
    ]
}


def send(conn, payload):
    headers = {"Content-type": "application/json"}
    json_data = json.dumps(payload)
    conn.request("POST", "/productionplan", json_data, headers)
    response = conn.getresponse()
    print(response.read().decode())


if __name__ == "__main__":
    from sys import argv

    ip = "127.0.0.1"
    port = 8888

    if len(argv) == 2:
        ip = argv[1]

    if len(argv) == 3:
        ip = argv[1]
        port = int(argv[2])

    conn = http.client.HTTPConnection(ip, port, timeout=300)
    send(conn, payload1)
    send(conn, payload2)
    send(conn, payload3)
    send(conn, payload4)
    send(conn, payload5)
    send(conn, payload6)
    send(conn, payload7)
    send(conn, payload8)
    send(conn, payload9)
    send(conn, payload10)
