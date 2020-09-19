
//1st bridge (motor 1)
int enB = 13;
int input1 = 12;
int input2 = 11;
//1st bridge (motor 3)
int enA = 8;
int input3 = 10;
int input4 = 9;

//2nd bridge (motor 2)
int enB_2 = 7;
int input5 = 6;
int input6 = 5;
//2nd bridge (motor 4)
int input7 = 4;
int input8 = 3;
int enA_2 = 2; 


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
}

void loop() {
  digitalWrite(input1, LOW);
  digitalWrite(input2, HIGH);  
  digitalWrite(input3, HIGH);
  digitalWrite(input4, LOW); 
  digitalWrite(input5, HIGH); //all the same direction
  digitalWrite(input6, LOW);  
  digitalWrite(input7, LOW);
  digitalWrite(input8, HIGH); 

  analogWrite(enA, 200);
  analogWrite(enB, 200);
  analogWrite(enA_2, 200);
  analogWrite(enB_2, 200);
  delay(5000);


  digitalWrite(input1, LOW);
  digitalWrite(input2, LOW);  
  digitalWrite(input3, LOW);
  digitalWrite(input4, LOW);
}
