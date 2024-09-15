const int analogInPin = A0;  // ESP8266 Analog Pin ADC0 = A0
  // 10 - bit ADC -> analogRead -> (0 -> 1023) <=> (0 -> 3.3V)
  // Vin = 3.3/1023 * ADC_Value 

int sensorValue = 0;  // value read from the pot

void setup() {
  // initialize serial communication at 115200
  // analogReference(INTERNAL);    // 1V Vref
}

void loop() {
  // read the analog in value
  sensorValue = analogRead(analogInPin);
  analogWrite(2, sensorValue);
  // print the readings in the Serial Monitor
  delay(100);
}
