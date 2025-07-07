#### clientTest.py ####

# creating a client to test TCP command server

import socket

def send_command(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect(('localhost', 9000))
    s.sendall(cmd.encode())
    s.close()
    
send_command("set_oxygen 50")
send_command("charge_battery 25.0")
send_command("reset_fault")

## Note - can also test with "netcat"
# echo "set_oxygen 75.0" | nc localhost 9000