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

#define echo A4    //Echo pin
#define trigger A5 //Trigger pin
#define servo A0

#define maxDist 15

int carSpeed = 100;
int distanciaLeft = 0, distanciaCenter = 0, distanciaRight = 0; 

// ================== DESPLAZAMIENTOS ==================
void forward(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  //Serial.println("\ngo forward!");
}

void back(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  //Serial.println("\ngo back!");
}

void left(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  //Serial.println("\ngo left!");
}

void right(){
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH); 
  //Serial.println("\ngo right!");
} 

void stop(){
   digitalWrite(ENA, LOW);
   digitalWrite(ENB, LOW);
   //Serial.println("\nStop!");
} 

// ================== SERVO ==================
void servoPulse (int pin, int angle){
  int PWM = (angle * 11) + 500;      // Convert angle to microseconds
  digitalWrite(pin, HIGH);
  delayMicroseconds(PWM);
  digitalWrite(pin, LOW);
  delay(50); // Refresh cycle of servo
}

void moverServo(){
  for (int angle = 130; angle <= 190; angle += 5)
  {
    servoPulse(servo, angle);  
  }
  for (int angle = 190; angle >= 60; angle -= 5)  
  {
    servoPulse(servo, angle);  
  }
  
  for (int angle = 60; angle <= 130; angle += 5)  
  {
    servoPulse(servo, angle);  
  }
}

// ================== ULTRASONIDO ==================
long medirDistancia(){
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  long time = pulseIn (echo, HIGH);
  return time / 29 / 2;
}

// ================== EVADIR OBSTACULOS ==================
void checkLado(){

  for (int angle = 130; angle <= 190; angle += 5)
  {
    servoPulse(servo, angle);  
  }
  delay(300);
  distanciaLeft = medirDistancia();
  Serial.print("\nDist Izquierda: ");
  Serial.println(distanciaLeft);
  delay(100);
  for (int angle = 190; angle >= 60; angle -= 5)
  {
    servoPulse(servo, angle); 
  }
  delay(500);
  distanciaRight = medirDistancia();
  Serial.print("Dist Derecha: ");
  Serial.println(distanciaRight);
  delay(100);
  for (int angle = 60; angle <= 130; angle += 5)
  {
    servoPulse(servo, angle);  
  }
  delay(300);
  compararDistancia(distanciaLeft, distanciaRight);
  Serial.println("Distancias Comparadas Correctamente!");
 
}

void compararDistancia(int distanciaLeft, int distanciaRight){
 
  if(distanciaLeft > distanciaRight)
  {
    left();
    Serial.print("A la Izquierda");
    delay(1500);
    forward();
    delay(300);
    right();
    delay(2000);
    forward();
    delay(670);
    stop();
    delay(1000);
  }
}

// ================== FOLLOW LINE ==================
void seguirLinea(){
  if(LT_M){
    forward();
  }
  else if(LT_R) { 
    right();
    while(LT_R);                             
  }   
  else if(LT_L) {
    left();
    while(LT_L);  
  }
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

// ================== MAIN LOOP ==================
void loop(){
  //right(); //YA
  //left(); //YA
  //forward(); //YA
  // back(); //YA
  //seguirLinea(); //BIEN
  
  distanciaCenter = medirDistancia();
  Serial.print("Dist Forward: ");
  Serial.println(distanciaCenter);
  if(distanciaCenter > maxDist || distanciaCenter == 0)
  {
    seguirLinea();
  }
  else if(distanciaCenter == maxDist )
  {
    stop();
    Serial.print("OBSTACULO A: ");
    Serial.print(distanciaCenter);
    Serial.print(" CM");
    delay(1000);
    checkLado();
    Serial.println("\nSIGO!");
  }
  else{
    seguirLinea();
  }
  
}
