/*
 * WEB_MOTOR_CONTROL.ino
 * Date: 11/6/2020
 * earthtowalt
 * much of the motor control code is based off: https://www.engineersgarage.com/esp8266/nodemcu-and-l293d-motor-driver-controlling-dc-motor/ 
 * Set up NodeMCU board to accept UDP packets from a central server to control the motors. 
 */

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

#define DEBUG true

const char* ssid = "Flatball Stars";
const char* password = "CrocNSocks?123";

#define UDP_PORT 4210

// UDP
WiFiUDP UDP;
char packet[256];
char reply[] = "control_ack";

const uint8_t Pwm1 = D1; //Nodemcu PWM pin 
const uint8_t Pwm2 = D2; //Nodemcu PWM pin

//Seven segment pins attachecd with nodemcu pins  
const int a0 = 15;  //Gpio-15 of nodemcu esp8266  
const int a1 = 13;  //Gpio-13 of nodemcu esp8266    
const int a2 = 12;  //Gpio-12 of nodemcu esp8266   
const int a3 = 14;  //Gpio-14 of nodemcu esp8266 
short lm = 0;
short rm = 0;

const int ledPin = 2;

void printWiFiStatus();

void setup() {
  
  Serial.begin(115200);
  Serial.println("program uploaded");
  WiFi.begin(ssid,password);

  // Configure GPIO2 as OUTPUT.
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);  // Initialize LED HIGH = OFF

  //Declaring l293d control pins as Output
  pinMode(a0, OUTPUT);     
  pinMode(a1, OUTPUT);     
  pinMode(a2, OUTPUT);
  pinMode(a3, OUTPUT); 

  analogWrite(Pwm1, 1200); // 777 is 50% duty
  analogWrite(Pwm2, 1200);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.println("Connecting to Wifi...");
  
    while (WiFi.status() != WL_CONNECTED) {
      blinkLED();
      delay(100);
    }
    // Print the new IP to Serial.
    printWiFiStatus();

    // Begin listening on UDP port
    UDP.begin(UDP_PORT);
    Serial.print("Listening on UDP port ");
    Serial.println(UDP_PORT);
  }
}

void loop() {

  // If packet received...
  int packetSize = UDP.parsePacket();
  if (packetSize) {
    Serial.print("Received packet! Size: ");
    Serial.println(packetSize); 
    int len = UDP.read(packet, 255);
    if (len > 0) {
      packet[len] = '\0';
    }

    Serial.print("Packet received: ");
    Serial.println(packet);

    // process packet

    // Send return packet
    UDP.beginPacket(UDP.remoteIP(), UDP.remotePort());
    UDP.write(reply);
    UDP.endPacket();
  }
  
//  WiFiClient client = server.available();
//  if (client) {
//    
//    Serial.println("Client connected.");
//    while (client.connected()) {
//      
//      if (client.available()) {
//        
//        String command = client.readStringUntil('\r');
//        //Serial.println(command);
//        if (command.indexOf('F') != -1) { // forward command
//          digitalWrite(LED_BUILTIN, LOW);     // LED LOW IS ON
//          if (command.indexOf('L') != -1 && lm != 1) {  // start left motor forward
//            digitalWrite(a0, HIGH); 
//            digitalWrite(a1, LOW);
//            lm = 1;
//          }
//          else if (command.indexOf('R') != -1 && rm != 1) { // start right motor forward
//            digitalWrite(a2, HIGH); 
//            digitalWrite(a3, LOW);
//            rm = 1;
//          }
//          
//        }
//        else if (command.indexOf('B') != -1) { // backward command
//          digitalWrite(LED_BUILTIN, LOW);    // LED LOW IS ON
//          if (command.indexOf('L') != -1 && lm != -1) {  // start left motor backward
//            digitalWrite(a0, LOW); 
//            digitalWrite(a1, HIGH); 
//            lm = -1;
//          }
//          else if (command.indexOf('R') != -1 && rm != -1) {  // start right motor backward
//            digitalWrite(a2, LOW); 
//            digitalWrite(a3, HIGH);
//            rm = -1;
//          }
//        }
//        else if (command.indexOf('O') != -1) { // motor off command
//          if (command.indexOf('L') != -1 && lm != 0) {  // stop left motor
//            digitalWrite(a0, LOW); 
//            digitalWrite(a1, LOW); 
//            lm = 0;
//          }
//          else if (command.indexOf('R') != -1 && rm != 0) {  // stop right motor
//            digitalWrite(a2, LOW); 
//            digitalWrite(a3, LOW);
//            rm = 0;
//          }
//        }
//        if (rm == 0 && lm == 0) digitalWrite(LED_BUILTIN, HIGH);
//      }
//    }
//    
//    Serial.println("Client disconnected.");
//    client.stop();
//  }  
  delay(200);
}
void printWiFiStatus() {
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void blinkLED() {
  digitalWrite(LED_BUILTIN, LOW);
  delay(200);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(200);
}
