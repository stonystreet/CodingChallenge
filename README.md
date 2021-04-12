For the server
--------------
To run the server on linux with the default 8888 port:
python server.py

To run the server on linux with an other port:
python server.py port_number



For the client
--------------
To run the client on linux with the default 127.0.0.1 ip and 8888 port:
python client.py

To run the client on linux with an other ip but the default 8888 port:
python client.py ip

To run the client on linux with an other ip and an other port:
python client.py ip port_number



NOTE:
-----
The client send 10 scenario and not just the 3 given one


Docker
------
Make sure to have a /tmp directory or see NOTE below
Build the image on linux:
docker build -t fab_py:v1 .

Run the image:
docker container run --rm -d -p 8888:8888 -v /tmp/logs:/logs --name fab fab_py:v1

used the server ...

Stop the image:
docker stop fab

the log of the server are located at:
/tmp/logs/log.txt

NOTE:
-----
Tou can replace the target log directory by replacing the -v /tmp/logs:/logs by /<your_dir>:/logs

