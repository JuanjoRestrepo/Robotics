//www.elegoo.com
//2016.09.23

#include <Servo.h> //servo library
Servo myServo; // creamos nuestro Objeto "myServo"
int Echo = A4;  
int Trig = A5; 


int ENA=10; 
int IN1=9;
int IN2=8;
int IN3=7;
int IN4=6;
int ENB=5; 

/* LLANTAS DERECHA
 * IN3
 * IN4
 *   
 * LLANTAS IZQUIERDA 
 * IN1 
 * IN2 
 */

// VELOCIDAD
int velocidad = 120;//150

// DISTANCIAS
int distanciaDerecha = 0, distanciaIzquierda = 0, distanciaMedia = 0;

void setup()
{
  myServo.attach(3);// attach servo on pin 3 to servo object
  Serial.begin(9600);
  pinMode(Echo, INPUT);    
  pinMode(Trig, OUTPUT); 
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
   
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
  digitalWrite(IN2,LOW);    // llantas derecha hacia adelante (forward)

  digitalWrite(IN3,HIGH);     
  digitalWrite(IN4,LOW);    // llantas izquierda hacia adelante (forward)

}

void turnRight(){ //turnRight
  digitalWrite(IN1, LOW); //Left Motor backword Pin 
  digitalWrite(IN2, HIGH); //Left Motor forword Pin 
  digitalWrite(IN3, LOW); //Right Motor forword Pin 
  digitalWrite(IN4, HIGH); //Right Motor backword Pin 
}

void turnLeft(){ //turnLeft
  digitalWrite(IN1, HIGH); //Left Motor backword Pin 
  digitalWrite(IN2, LOW); //Left Motor forword Pin 
  digitalWrite(IN3, HIGH); //Right Motor forword Pin 
  digitalWrite(IN4, LOW); //Right Motor backword Pin 
}

void Stop()
{
  analogWrite(ENA,LOW);
  analogWrite(ENB,LOW);
  Serial.println("Stop!");
} 

void Run()
{
  moveForward();
  delay(1000);
  Stop();
  delay(1000);
  moveBackwards();
  delay(1000);
  Stop();
  delay(1000);
  turnLeft();
  delay(1000);
  turnRight();
  delay(1000);
}

int Distancia()   
{
  digitalWrite(Trig, LOW);   
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);  
  delayMicroseconds(20);
  digitalWrite(Trig, LOW);   
  float Fdistance = pulseIn(Echo, HIGH);  
  Fdistance= Fdistance/58;       
  return (int)Fdistance;
} 

void loop()
{
  /*
  myServo.write(90);//setservo position according to scaled value
  delay(500); 
  distanciaMedia = Distancia();

  #ifdef send
  Serial.print("distanciaMedia=");
  Serial.println(distanciaMedia);
  #endif*/
  moveForward();
}
