#include <NewPing.h>
int Echo = A4;  
int Trig = A5;  
int maxDist = 15;
#define servo A0
NewPing sonar (Trig, Echo, maxDist);
 
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
 
#define velocidad 100//120 //150
int distanciaDerecha = 0, distanciaIzquierda = 0, distanciaMitad = 0;
 
void forward(){
  analogWrite(ENA, velocidad);
  analogWrite(ENB, velocidad);
  digitalWrite(IN1, LOW); //HIGH ORIGINAL
  digitalWrite(IN2, HIGH);  //LOW ORIGINAL
  digitalWrite(IN3, LOW);  //LOW ORIGINAL
  digitalWrite(IN4, HIGH); //HIGH ORIGINAL
  Serial.println("go forward!");
}
 
void back(){
  analogWrite(ENA, velocidad);
  analogWrite(ENB, velocidad);
  digitalWrite(IN1, LOW); //LOW ORIGINAL
  digitalWrite(IN2, HIGH); //HIGH ORIGINAL
  digitalWrite(IN3, HIGH); //HIGH ORIGINAL
  digitalWrite(IN4, LOW); //LOW ORIGINAL
  Serial.println("go back!");
}
 
void right(){
  analogWrite(ENA, velocidad);
  analogWrite(ENB, velocidad);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW); //HIGH ORIGINAL
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("go left!");
}
 
void left(){
  analogWrite(ENA, velocidad);
  analogWrite(ENB, velocidad);
  digitalWrite(IN1, LOW); //HIGH ORIGINAL
  digitalWrite(IN2, HIGH); //LOW ORIGINAL
  digitalWrite(IN3, LOW); //HIGH ORIGINAL
  digitalWrite(IN4, LOW); //LOW ORIGINAL
  Serial.println("go right!");
} 
 
void Stop(){
   digitalWrite(ENA, LOW);
   digitalWrite(ENB, LOW);
   Serial.println("Stop!");
}

//  ------------------ SERVO --------------------

// Enviar Pulsos PWM al servo para moverlo
void servoPulse(int pin, int angle)
{
  int pwm = (angle*11) + 500;      // Convert angle to microseconds
  digitalWrite(pin, HIGH);
  delayMicroseconds(pwm);
  digitalWrite(pin, LOW);
  delay(50); // Refresh cycle of servo
}
void moveServo()
{
  //Rango Servo: 10°- 180° 
  for (int angle = 130; angle <= 180; angle += 5)  
  {
    servoPulse(servo, angle);  
  }
  
  for (int angle = 180; angle >= 60; angle -= 5)  
  {
    servoPulse(servo, angle);  
  }
  
  for (int angle = 60; angle <= 130; angle += 5)  
  {
    servoPulse(servo, angle);  
  }
}

// ------------------ ULTRASONIDO -----------------
int medirDistancia()   
{
  //return sonar.ping_cm();
  digitalWrite(Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  long time = pulseIn (Echo, HIGH);
  return time / 29 / 2;  
} 


void followLine() {
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


// ------------------ SETUP and MAIN LOOP -----------------
 
void setup(){
  Serial.begin(9600);
  pinMode(LT_R,INPUT);
  pinMode(LT_M,INPUT);
  pinMode(LT_L,INPUT);
  pinMode(Echo, INPUT);    
  pinMode(Trig, OUTPUT);
  pinMode(servo, OUTPUT);

  moveServo();
  //distanciaMitad = medirDistancia();
  //delay(500);
}
 

void loop(){
  followLine();
}
