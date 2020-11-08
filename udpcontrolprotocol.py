import sys
import socket 

# inspiration taken from here: 
# https://linuxhint.com/send_receive_udp_python/

# RAT PORT, TODO later I would like this to be better 
RAT_IP = "10.0.0.117"
RAT_PORT = 4210

class UdpControlProtocol:
    # control constants
    LEFT = "L"
    RIGHT = "R"
    JOUST = "J"
    OFF = "O"
    FORWARD = "F"
    BACKWARD = "B"
    UP = "U"
    DOWN = "D"

    # initialize the control server with ip, port
    def __init__(self, ip=RAT_IP, port=RAT_PORT, bs=256):
        self.IP = ip
        self.PORT = port 
        self.BUFFER_SIZE = bs
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # bind this socket
    def bind(self):
        s.bind((self.IP, self.PORT))
        print("successful bind.")
    
    # send data
    def send(self, data):
        self.s.sendto(data.encode('utf-8'), (self.IP, self.PORT))
    
    def left_forward(self):
        self.send(self.LEFT + self.FORWARD)
    def left_backward(self):
        self.send(self.LEFT + self.BACKWARD)
    def left_stop(self):
        self.send(self.LEFT + self.OFF)

    def right_forward(self):
        self.send(self.RIGHT + self.FORWARD)
    def right_backward(self):
        self.send(self.RIGHT + self.BACKWARD)
    def right_stop(self):
        self.send(self.RIGHT + self.OFF)
    
    def joust_up(self):
        self.send(self.JOUST, self.UP)
    def joust_down(self):
        self.send(self.JOUST, self.DOWN)
    def joust_stop(self):
        self.send(self.JOUST, self.OFF)
    


