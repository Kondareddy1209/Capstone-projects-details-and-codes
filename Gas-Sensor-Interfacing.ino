int Led = 13;         // conncet led here
int sensorpin = A0;         //connect sensor analog output
int sensorThres = 150;    // Your threshold value  (chnage threshold value according to your input)

void setup() {
  pinMode(Led, OUTPUT);
  pinMode(sensorpin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int analogSensor = analogRead(sensorpin);

  Serial.print("Input Level : ");    // sensor data will display on serial monitor
  Serial.println(analogSensor);
  // Checks if it has reached the threshold value
  if (analogSensor > sensorThres)
  {
    digitalWrite(Led, HIGH);
  }
  else
  {
    digitalWrite(Led, LOW);
  }
  delay(50);
}
