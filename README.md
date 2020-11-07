# RatNet

The goal of this project is to create a RATNET. Similar to a botnet, A RatNet is a series of mechanical rats all controlled by some central system with a goal of taking over the world.

much of the hardware design was taken from this tutorial: https://www.engineersgarage.com/esp8266/nodemcu-and-l293d-motor-driver-controlling-dc-motor/ 

The UDP implementation is based on this: https://siytek.com/esp8266-udp-send-receive/#:~:text=You%20can%20use%20UDP%20to,or%20many%20other%20WiFi%20devices.

**Implementation:**
+ Pygame based control system with either keyboard or game controller input
+ wireless communication with esp chip on rat board through TCP connection over local network

**Future:**
+ clean up message sending protocol
+ switch to UDP connection
+ control multiple rats
