#include <NewPing.h>
int Echo = A4;  
int Trig = A5;  
int maxDist = 20;
#define servo A1

NewPing sonar (Trig, Echo, maxDist);


int ENA = 10; 
int IN1 = 9;
int IN2 = 8;
int IN3 = 7;
int IN4 = 6;
int ENB = 5;

/* LLANTAS IZQUIERDA 
 * IN1 
 * IN2 
 * 
 * LLANTAS DERECHA
 * IN3
 * IN4
 * 
 */

// VELOCIDAD Duty Cycle de los motores 0-255
int velocidad = 80; //120;//150 

// DISTANCIAS
int distanciaDerecha = 0, distanciaIzquierda = 0, distanciaMitad = 0;

void setup()
{

  Serial.begin(9600);
  pinMode(Echo, INPUT);    
  pinMode(Trig, OUTPUT); 
    
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);

  pinMode(servo, OUTPUT);

  servoPulse(servo, 90);
}

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
  for (int angle = 90; angle <= 170; angle += 5)  
  {
    servoPulse(servo, angle);  
  }
  
  for (int angle = 170; angle >= 0; angle -= 5)  
  {
    servoPulse(servo, angle);  
  }
  
  for (int angle = 10; angle <= 90; angle += 5)  
  {
    servoPulse(servo, angle);  
  }
}

void moveForward()
{
  analogWrite(ENA,velocidad);
  analogWrite(ENB,velocidad);  
  digitalWrite(IN1,LOW);      
  digitalWrite(IN2,HIGH);    // llantas derecha hacia adelante (forward)

  digitalWrite(IN3,LOW);     
  digitalWrite(IN4,HIGH);    // llantas izquierda hacia adelante (forward)
}

void moveBackwards()
{
  analogWrite(ENA,velocidad);
  analogWrite(ENB,velocidad);
  digitalWrite(IN1,HIGH);      
  digitalWrite(IN2,LOW);    // llantas derecha hacia atras (backwards)
  
  digitalWrite(IN3,HIGH);     
  digitalWrite(IN4,LOW);    // llantas izquierda hacia atras (backwards)

}

void turnRight()
{
  analogWrite(ENA,velocidad);
  analogWrite(ENB,velocidad);
  digitalWrite(IN1, LOW); 
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW); 
  digitalWrite(IN4, LOW); 
}

void turnLeft()
{
  analogWrite(ENA,velocidad);
  analogWrite(ENB,velocidad);
  digitalWrite(IN1, LOW); 
  digitalWrite(IN2, LOW); 
  digitalWrite(IN3, LOW); 
  digitalWrite(IN4, HIGH); 
}

void Stop()
{
  analogWrite(ENA, LOW);
  analogWrite(ENB, LOW);
} 

// ULTRASONIDO
int medirDistancia()   
{
  return sonar.ping_cm();  
} 


void checkSide(){
    Stop();
    delay(100);
    for (int angle = 90; angle <= 170; angle += 5)  {
      servoPulse(servo, angle);  }
      delay(300);
      distanciaIzquierda = medirDistancia();
      Serial.print("Dist Izquierda: ");
      Serial.println(distanciaIzquierda);
      delay(100);
    for (int angle = 170; angle >= 10; angle -= 5)  {
      servoPulse(servo, angle);  }
      delay(500);
      distanciaDerecha = medirDistancia();
      Serial.print("Dist Derecha: ");
      Serial.println(distanciaDerecha);
      delay(100);
    for (int angle = 10; angle <= 90; angle += 5)  {
      servoPulse(servo, angle);  }
      delay(300);
      compareDistance(distanciaDerecha, distanciaIzquierda);
}

void compareDistance(int distDer, int distIzq){
  if(distIzq > distDer)
  {
    turnLeft();
    delay(500);
    moveForward();
    delay(600);
    turnRight();
    delay(500);
    moveForward();
    delay(600);
    turnRight();
    delay(400);
  }
  else
  {
    turnRight();
    delay(500);
    moveForward();
    delay(600);
    turnLeft();
    delay(500);
    moveForward();
    delay(600);  
    turnLeft();
    delay(400);
  }
}

void Run()
{
  Stop();
  delay(3000);
  distanciaMitad = medirDistancia();
  Serial.print("Distancia Mitad: ");
  Serial.println(distanciaMitad);
  delay(100);
  moveForward();
  if (distanciaMitad <= 10)
  {
    Stop();
    delay(100);
    moveBackwards();
    delay(1500);
    Stop();
  }
  else
  {
    moveForward();
    delay(5000);
  }
}

void loop()
{
  delay(1000);
  checkSide();
}

