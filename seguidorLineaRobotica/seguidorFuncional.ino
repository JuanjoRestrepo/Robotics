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
volatile bool lineDetected = false;

// ================== INTERRUPT SERVICE ROUTINE ==================
void lineInterrupt() {
  lineDetected = true;
}

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
  
  for (int angle = 110; angle <= 190; angle += 5)
  {
    servoPulse(servo, angle);  
  }
  for (int angle = 190; angle >= 30; angle -= 5)  
  {
    servoPulse(servo, angle);  
  }
  
  for (int angle = 30; angle <= 110; angle += 5)  
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
void evadirObstaculo(){
 
  // Girar hacia la izquierda para rodear el obstáculo
  left();
  delay(900);

  // Avanzar para rodear el obstáculo
  forward();
  delay(100);

  // Girar hacia la derecha para reorientarse después de rodear el obstáculo
  right();
  delay(900);

  // Avanzar hasta encontrar la línea
  forward();
  delay(150);
  //while (!lineDetected); // Esperar a que se detecte la línea
  //lineDetected = false;
  

  // Ajustar la posición del robot en la línea (puedes modificar esta parte según tus necesidades)
  //delay(670);
  stop();
  delay(100);
}

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
  Serial.println("Distancias Comparadas Correctamente!");
 
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

  // Configurar interrupciones para los sensores infrarrojos
  //attachInterrupt(digitalPinToInterrupt(LT_R), lineInterrupt, CHANGE);
  //attachInterrupt(digitalPinToInterrupt(LT_M), lineInterrupt, CHANGE);
  //attachInterrupt(digitalPinToInterrupt(LT_L), lineInterrupt, CHANGE);
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
  
  if (distanciaCenter > maxDist || distanciaCenter == 0) {
    seguirLinea();
  } else if (distanciaCenter == maxDist) {
    stop();
    Serial.print("OBSTACULO A: ");
    Serial.print(distanciaCenter);
    Serial.print(" CM");
    delay(1000);
    evadirObstaculo();
  } 
  else {
    seguirLinea();
  }
  //moverServo();
  //servoPulse(servo, 90);
  
}
