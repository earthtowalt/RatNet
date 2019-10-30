/*
 * Date: 10/29/2019
 * earthtowalt
 * much of the motor control code is based off: https://www.engineersgarage.com/esp8266/nodemcu-and-l293d-motor-driver-controlling-dc-motor/ 
 * 
 */

#include <ESP8266WiFi.h>

const char* ssid = "David's iPhone";
const char* password = "projectwifi";

const uint8_t Pwm1 = D1; //Nodemcu PWM pin 
const uint8_t Pwm2 = D2; //Nodemcu PWM pin

//Seven segment pins attachecd with nodemcu pins  
const int a0 = 15;  //Gpio-15 of nodemcu esp8266  
const int a1 = 13;  //Gpio-13 of nodemcu esp8266    
const int a2 = 12;  //Gpio-12 of nodemcu esp8266   
const int a3 = 14;  //Gpio-14 of nodemcu esp8266 

const int ledPin = 2;
WiFiServer server(80);

void printWiFiStatus();

void setup() {
  
  Serial.begin(115200);
  Serial.println("program uploaded");
  WiFi.begin(ssid,password);

  // Configure GPIO2 as OUTPUT.
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);  // Initialize LED HIGH = OFF

  // Start TCP server.
  server.begin();

  
}

void loop() {
  //
  delay(100);
  //
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Connecting to Wifi...");
  
    while (WiFi.status() != WL_CONNECTED) {
      blinkLED();
    }
    // Print the new IP to Serial.
    printWiFiStatus();
  }

  
  WiFiClient client = server.available();
  if (client) {
    
    Serial.println("Client connected.");
    while (client.connected()) {
      
      if (client.available()) {
        
        char command = client.read();
        //Serial.println(command);
        if (command == 'H') {
          analogWrite(Pwm1, 512); // default to 50% duty
          analogWrite(Pwm2, 512);
          
          digitalWrite(LED_BUILTIN, LOW);     // LED LOW IS ON
          
          digitalWrite(a0, HIGH); // start first motor
          digitalWrite(a1, LOW);
          
          digitalWrite(a2, HIGH); // start second motor
          digitalWrite(a3, LOW);
        }
        else if (command == 'L') {
          digitalWrite(LED_BUILTIN, HIGH);    // LED HIGH IS OFF

          digitalWrite(a0, LOW); // stop first motor
          digitalWrite(a1, HIGH);
          
          digitalWrite(a2, LOW); // stop second motor
          digitalWrite(a3, HIGH);
        }
      }
    }
    
    Serial.println("Client disconnected.");
    client.stop();
  }  
  //blinkLED();
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
 
