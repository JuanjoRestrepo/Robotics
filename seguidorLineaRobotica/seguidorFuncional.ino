
 //Line Tracking IO define
#define LT_R digitalRead(11)
#define LT_M digitalRead(4)
#define LT_L digitalRead(2)
 
#define ENA 10
#define ENB 5
#define IN1 9
#define IN2 8
#define IN3 7
#define IN4 6
 
#define carSpeed 80//120 //150
 
void forward(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("go forward!");
}
 
void back(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  Serial.println("go back!");
}
 
void left(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("go left!");
}
 
void right(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW); 
  Serial.println("go right!");
} 
 
void stop(){
   digitalWrite(ENA, LOW);
   digitalWrite(ENB, LOW);
   Serial.println("Stop!");
} 
 
void setup(){
  Serial.begin(9600);
  pinMode(LT_R,INPUT);
  pinMode(LT_M,INPUT);
  pinMode(LT_L,INPUT);
}
 
void loop() {
  if(LT_M){
    forward();
    Serial.println("Centro Encedido");
  }
  else if(LT_R) { 
    right();
    Serial.println("Derecha Encedido");
    while(LT_R);                             
  }   
  else if(LT_L) {
    left();
    Serial.println("Izquierda Encedido");
    while(LT_L);  
  }
}
