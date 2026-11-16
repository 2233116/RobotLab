import network
from socket import socket
ap = network.WLAN(network.AP_IF)
server = socket()
ap.config(essid = "RobotLab_Car",password = "88888888",authmode = network.AUTH_WPA_WPA2_PSK)
ap.active(True)
server.bind(("0.0.0.0",80))
server.listen(1)
client,addr = server.accept()
data = client.recv(1024)
response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    "Content-Length: 14\r\n"
    "Connection: close\r\n"
    "\r\n"
    "Hello Robotlab"
)
client.send(response.encode())
print(ap.ifconfig())

