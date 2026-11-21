import network
from socket import socket
import json
ap = network.WLAN(network.AP_IF)
server = socket()
ap.config(essid = "RobotLab_Car",password = "88888888",authmode = network.AUTH_WPA_WPA2_PSK)
ap.active(True)
print(ap.ifconfig())
server.bind(("0.0.0.0",80))
server.listen(1)
body = 0
while True:
    client,addr = server.accept()
    data = client.recv(1024)
    request = data.decode()
    headers = request.split("\r\n")
    for line in headers:
        if line.startswith("Content-Length:"):
            content_length = int(line.split(":")[1])
            break
    body = body + request.split("\r\n\r\n")[1]
    remaining = content_length - len(body)
    if remaining != 0:
        data_2 = client.recv(remaining)
    control = json.loads(body)
    forward = control["forward"]
    turn = control["turn"]
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        "Content-Length: 14\r\n"
        "Connection: close\r\n"
        "\r\n"
        "Hello Robotlab"
    )
    client.send(response.encode())
    client.close()



