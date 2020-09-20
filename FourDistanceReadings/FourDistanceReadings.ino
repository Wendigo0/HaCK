const int trigPin1 = 40;
const int echoPin1 = 42;
long duration1;

const int trigPin2 = 44;
const int echoPin2 = 46;
long duration2;

const int trigPin3 = 38;
const int echoPin3 = 36;
long duration3;

const int wall = 1;

void setup() {
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
  Serial.begin(9600);
  
}

void loop() {
  //using first sensor
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(100);
  digitalWrite(trigPin1, LOW);

  duration1 = pulseIn(echoPin1, HIGH);
  double distance1 = (double)duration1 * 345 / 2 / 1000000;

  Serial.print(distance1); // in meters
  Serial.print(',');
  delay(2);

  //Second Sensor
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);

  duration2 = pulseIn(echoPin2, HIGH);
  double distance2 = (double)duration2 * 345/2/1000000;

  Serial.print(distance2); //in meters
  Serial.print(',');

  // Third Sensor
  digitalWrite(trigPin3, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin3, LOW);

  duration3 = pulseIn(echoPin3, HIGH);
  double distance3 = (double)duration3 * 345 / 2 / 1000000;

  Serial.print(distance3); // in meters
  Serial.print(',');

  Serial.println(wall); // in meters
  delay(100);
  
}
