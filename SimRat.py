
from udpcontrolprotocol import UdpControlProtocol

# sometimes UDP wont send the message through, so here, send message until ack received
class SimRat:
    LM = UdpControlProtocol.OFF
    RM = UdpControlProtocol.OFF 
    JM = UdpControlProtocol.OFF 
     
