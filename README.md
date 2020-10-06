# RatNet

The goal of this project is to create a RATNET. Similar to a botnet, A RatNet is a series of mechanical rats all controlled by some central system with a goal of taking over the world.

much of the hardware design was taken from this tutorial: https://www.engineersgarage.com/esp8266/nodemcu-and-l293d-motor-driver-controlling-dc-motor/ 

**Implementation:**
+ Pygame based control system with either keyboard or game controller input
+ wireless communication with esp chip on rat board through TCP connection over local network

**Future:**
+ clean up message sending protocol
+ switch to UDP connection
+ control multiple rats
