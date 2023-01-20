int sensorPin = 10;
int ledPin = 12;

//int sensorPin1 = 0;
//int ledPin1 = //LEEG;
//y
//int sensorPin2 = //LEEG;
//int ledPin2 = //LEEG;

void setup() {
  pinMode(sensorPin, INPUT);
  pinMode(ledPin, OUTPUT);

  Serial.begin(9600);

//  pinMode(sensorPin1, INPUT);
//  pinMode(ledPin1, OUTPUT)
//
//  pinMode(sensorPin2, INPUT);
//  pinMode(ledPin2, OUTPUT)
}

void loop() {

  // LED STRIP 1 MET SENSOR
  int read = digitalRead(sensorPin);

  if (read == 0) {
    digitalWrite(ledPin, HIGH);
    delay(4000);
  }
  else {
    digitalWrite(ledPin, LOW);
  }


//  // LED STRIP 2 MET SENSOR
//  int read1 = digitalRead(sensorPin1);
//
//  if (read == LOW) {
//    digitalWrite(ledPin1, HIGH);
//    delay(10000);
//  }
//
//  else {
//    digitalWrite(ledPin1, LOW);
//  }
//
//  
//  // LED STRIP 3 MET SENSOR
//   int read2 = digitalRead(sensorPin2);
//
//  if (read == LOW) {
//    digitalWrite(ledPin2, HIGH);
//    delay(10000);
//  }
//
//  else {
//    digitalWrite(ledPin2, LOW);
//  }
}
