#### udpTest.py ####

## Test to receieve telemetry in a client
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 9100))

while True:
    data, addr = sock.recvfrom(1024)
    print("Telemetry received:", data.decode())
    
# Note - with netcat, could alternatively type: nc -lu 9100