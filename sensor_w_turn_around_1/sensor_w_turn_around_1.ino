#include <SoftwareSerial.h>

//1st bridge (motor 1)
int enB = A2;
int input1 = 12;
int input2 = 11;
//1st bridge (motor 3)
int enA = A3;
int input3 = 10;
int input4 = 9;

//2nd bridge (motor 2)
int enB_2 = A4;
int input5 = 6;
int input6 = 5;
//2nd bridge (motor 4)
int input7 = 4;
int input8 = 3;
int enA_2 = A5; 

const int trigPin1 = 46;
const int echoPin1 = 44;
long duration1;

const int trigPin2 = 40;
const int echoPin2 = 42;
long duration2;

const int trigPin3 = 38;
const int echoPin3 = 36;
long duration3;

int side = 1;
double distance1 = 0.0;
double distance2 = 0.0;
double distance3 = 0.0;


void turnAround(int& side){
  if( (distance2 <= 0.20) && (distance2 >= 0.15) ){
    digitalWrite(input1, HIGH);
    digitalWrite(input2, LOW);  
    digitalWrite(input3, LOW);
    digitalWrite(input4, HIGH); 
    digitalWrite(input5, HIGH); //wheels spin opposite directions (clockwise)
    digitalWrite(input6, LOW);  
    digitalWrite(input7, LOW);
    digitalWrite(input8, HIGH); 

    analogWrite(enA, 200);
    analogWrite(enB, 200);
    analogWrite(enA_2, 200);
    analogWrite(enB_2, 200);
    delay(500);    //arbitrary time delay - TODO: trial and error
    
    side++;
  }
}

void setup() {
  //bridge 1
  pinMode(enA, OUTPUT);
  pinMode(input1, OUTPUT);
  pinMode(input2, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(input3, OUTPUT);
  pinMode(input4, OUTPUT);
  //bridge 2
  pinMode(enA_2, OUTPUT);
  pinMode(input5, OUTPUT);
  pinMode(input6, OUTPUT);
  pinMode(enB_2, OUTPUT);
  pinMode(input7, OUTPUT);
  pinMode(input8, OUTPUT);  
  //sensor pins
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
  
  Serial.begin(9600);

  delay(10000);
}

void loop() {
  digitalWrite(input1, HIGH);
  digitalWrite(input2, LOW);  
  digitalWrite(input3, LOW);
  digitalWrite(input4, HIGH); 
  digitalWrite(input5, LOW); //all wheels in the same direction
  digitalWrite(input6, HIGH);  
  digitalWrite(input7, HIGH);
  digitalWrite(input8, LOW); 

  analogWrite(enA, 200);
  analogWrite(enB, 200);
  analogWrite(enA_2, 200);
  analogWrite(enB_2, 200);
  //delay(5000);
  
    //using first sensor
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);

  duration1 = pulseIn(echoPin1, HIGH);
  distance1 = (double)duration1 * 345 / 2 / 1000000;

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
  distance2 = (double)duration2 * 345 / 2 / 1000000;

  Serial.print(distance2); //in meters
  Serial.print(',');

  // Third Sensor
  digitalWrite(trigPin3, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin3, LOW);

  duration3 = pulseIn(echoPin3, HIGH);
  distance3 = (double)duration3 * 345 / 2 / 1000000;

  Serial.print(distance3); // in meters
  Serial.print(',');

  Serial.println(side);//side of arena (1-4)

  if( (distance2 <= 0.05) && (distance2 >= 0.02) ){
    side++;
    digitalWrite(input1, HIGH);
    digitalWrite(input2, LOW);  
    digitalWrite(input3, LOW);
    digitalWrite(input4, HIGH); 
    digitalWrite(input5, HIGH); //wheels spin opposite directions (clockwise)
    digitalWrite(input6, LOW);  
    digitalWrite(input7, LOW);
    digitalWrite(input8, HIGH); 

    analogWrite(enA, 150);
    analogWrite(enB, 150);
    analogWrite(enA_2, 150);
    analogWrite(enB_2, 150);
    delay(2000);    //arbitrary time delay - TODO: trial and error
  }
  
  //function call determines which side of arena car is on
  //turnAround(side);
  
  //if full lap is completed, shut down motors
  while(side >= 5){
    digitalWrite(input1, LOW);
    digitalWrite(input2, LOW);  
    digitalWrite(input3, LOW);
    digitalWrite(input4, LOW);
    digitalWrite(input5, LOW);
    digitalWrite(input6, LOW);
    digitalWrite(input7, LOW);  
    digitalWrite(input8, LOW);
  }
  
}
