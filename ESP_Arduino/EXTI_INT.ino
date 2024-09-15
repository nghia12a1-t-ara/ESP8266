const int interruptPin = 0;   //GPIO 0 (Flash Button) 
const int LED=2;              //On board blue LED 

void setup() 
{ 
  Serial.begin(115200); 
  pinMode(LED,OUTPUT); 
  pinMode(interruptPin, INPUT_PULLUP); 
  attachInterrupt(digitalPinToInterrupt(interruptPin), handleInterrupt, FALLING); 
} 

void loop() 
{ 
} 

//This program get executed when interrupt is occures i.e.change of input state
void handleInterrupt() { 
    Serial.println("Interrupt Detected"); 
}
