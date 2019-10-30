/*
 * Date: 10/29/2019
 * earthtowalt
 * much of the motor control code is based off: https://www.engineersgarage.com/esp8266/nodemcu-and-l293d-motor-driver-controlling-dc-motor/ 
 * 
 */

#include <ESP8266WiFi.h>

const char* ssid = "vummiv";
const char* password = "";

//Seven segment pins attachecd with nodemcu pins  
const int a0 = 15;  //Gpio-15 of nodemcu esp8266  
const int a1 = 13;  //Gpio-13 of nodemcu esp8266    
const int a2 = 12;  //Gpio-12 of nodemcu esp8266   
const int a3 = 14;  //Gpio-14 of nodemcu esp8266 

const int ledPin = 2;
WifiServer server(80);

void setup() {
  Serial.begin(115200);
  delay(10);
  // declaring l293d control pins.
  pinMode(a0, OUTPUT);     
  pinMode(a1, OUTPUT);     
  pinMode(a2, OUTPUT);
  pinMode(a3, OUTPUT); 

  // connect to wifi network
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");

  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
  
}


 
