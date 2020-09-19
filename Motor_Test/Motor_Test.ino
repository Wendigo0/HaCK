
//1st bridge motor 1
int enB = 13;
int input1 = 12;
int input2 = 11;

//1st bridge motor 2
int enA = 8;
int input3 = 10;
int input4 = 9;


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
