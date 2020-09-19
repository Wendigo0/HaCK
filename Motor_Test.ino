
//1st bridge motor 1
int enA = 8;
int input1 = 10;
int input2 = 9;

//1st bridge motor 2
int enB = 13;
int input3 = 12;
int input4 = 11;


void setup() {
  pinMode(enA, OUTPUT);
  pinMode(input1, OUTPUT);
  pinMode(input2, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(input3, OUTPUT);
  pinMode(input4, OUTPUT);
}

void loop() {
  digitalWrite(input1, LOW);
  digitalWrite(input2, HIGH);  
  digitalWrite(input3, LOW);
  digitalWrite(input4, HIGH); 

  analogWrite(enA, 50);
  analogWrite(enB, 50);
  delay(5000);

  digitalWrite(input1, LOW);
  digitalWrite(input2, LOW);  
  digitalWrite(input3, LOW);
  digitalWrite(input4, LOW);
}
