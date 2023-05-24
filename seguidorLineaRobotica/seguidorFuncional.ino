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

#define carSpeed 95
//90 //100 //120 //150

#define echo A4    //Echo pin
#define trigger A5 //Trigger pin
#define servo A0

int Set=15;
int distanciaLeft = 0, distanciaForward = 0, distanciaRight = 0; 

void forward(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("go forward!");
}

void back(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
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
  digitalWrite(IN4, LOW);
  Serial.println("go left!");
}

void right(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH); 
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
  pinMode(echo, INPUT );// declare ultrasonic sensor Echo pin as input
  pinMode(trigger, OUTPUT); // declare ultrasonic sensor Trigger pin as Output
  pinMode(servo, OUTPUT);

  moverServo();
}

void servoPulse (int pin, int angle){
  int pwm = (angle*11) + 500;      // Convert angle to microseconds
  digitalWrite(pin, HIGH);
  delayMicroseconds(pwm);
  digitalWrite(pin, LOW);
  delay(50); // Refresh cycle of servo
}

void moverServo(){
  for (int angle = 130; angle <= 190; angle += 5)
  {
    servoPulse(servo, angle);  
  }
  for (int angle = 190; angle >= 70; angle -= 5)  
  {
    servoPulse(servo, angle);  
  }
  
  for (int angle = 70; angle <= 130; angle += 5)  
  {
    servoPulse(servo, angle);  
  }
}

// ================== Ultrasonic_read ==================
long medirDistancia(){
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  long time = pulseIn (echo, HIGH);
  return time / 29 / 2;
}

void compararDistancia(int distanciaLeft, int distanciaRight){
  if(distanciaLeft > distanciaRight)
  {
    left();
    delay(500);
    forward();
    delay(600);
    right();
    delay(500);
    forward();
    delay(600);
    right();
    delay(400);
  }
  else
  {
    right();
    delay(500);
    forward();
    delay(600);
    left();
    delay(500);
    forward();
    delay(600);  
    left();
    delay(400);
  }
}

void checkLado(){
  stop();
  delay(100);
  for (int angle = 130; angle <= 190; angle += 5)
  {
    servoPulse(servo, angle);  
  }
  delay(300);
  distanciaLeft = medirDistancia();
  Serial.print("Dist Izquierda: ");
  Serial.println(distanciaRight);
  delay(100);
  for (int angle = 190; angle >= 70; angle -= 5)
  {
    servoPulse(servo, angle); 
  }
  delay(500);
  distanciaRight = medirDistancia();
  Serial.print("Dist Derecha: ");
  Serial.println(distanciaLeft);
  delay(100);
  for (int angle = 70; angle <= 130; angle += 5)
  {
    servoPulse(servo, angle);  
  }
  delay(300);
  compararDistancia(distanciaLeft, distanciaRight);
}

void seguirLinea() {
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

void loop(){
  //right(); YA
  //left(); YA
  // forward(); YA
  // back(); YA
  //seguirLinea(); BIEN
  distanciaForward = medirDistancia();
  Serial.print("Dist Forward: ");
  Serial.println(distanciaForward);
  checkLado();
}
