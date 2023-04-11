#include <Servo.h> //servo library
#include <NewPing.h>
int Echo = A4;  
int Trig = A5;  
int maxDist = 20;

//NewPing sonar (A5, A4, maxDist);
//Servo myServo; // creamos nuestro Objeto "myServo"

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
  //myServo.attach(3);
  Serial.begin(9600);
  //pinMode(Echo, INPUT);    
  //pinMode(Trig, OUTPUT); 
    
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

void Run()
{
  moveForward();
  delay(3000);
  Stop();
  delay(3000);
  moveBackwards();
  delay(3000);
  Stop();
  delay(3000);

  turnLeft();
  delay(3000);
  Stop();
  delay(3000);
  turnRight();
  delay(3000);
  Stop();
  delay(3000);
}


// ULTRASONIDO
int medirDistancia()   
{
  //return sonar.ping_cm();  
} 

void compararDistancia()
{
  if(distanciaIzquierda > distanciaDerecha){
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
  else{
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


void chequearLados()
{
  Stop();
  delay(500);

  // Lado Izquierdo
  for(int i=90; i<=170; i+=5){
    //myServo.write(i);
  }
  delay(1000);
  //distanciaDerecha = medirDistancia();
  Serial.print("distanciaDerecha: ");
  Serial.println(distanciaDerecha);
  delay(100);

  // Lado Derecho
  for(int i=170; i>=0; i-=5){
    //myServo.write(i);
  }
  delay(1000);
  //distanciaIzquierda = medirDistancia();
  Serial.print("distanciaIzquierda: ");
  Serial.println(distanciaIzquierda);
  delay(100);

  //Volver al centro y comparar lados
  for(int i=0; i<=90; i+=5){
    //myServo.write(i);
  }
  delay(1000);
  compararDistancia();
  
}


void loop()
{
  //chequearLados();
  /*
  myServo.write(90);//setservo position according to scaled value
  delay(500); 
  distanciaMedia = Distancia();

  #ifdef send
  Serial.print("distanciaMedia=");
  Serial.println(distanciaMedia);
  #endif*/
  delay(3000); 
  Run();
  /*
  myServo.write(90); //Rango Servo: 10°- 180° 
  delay(500); 
  distanciaMitad = medirDistancia();
  Serial.print("\ndistanciaMitad: ");
  Serial.println(distanciaMitad);
  
  if(distanciaMitad <= 10)
  {
    Stop();
    delay(500);
    myServo.write(10);
    delay(1000);      
    distanciaDerecha = medirDistancia();

    Serial.print("distanciaDerecha: ");
    Serial.println(distanciaDerecha);

    delay(500);
    myServo.write(90);              
    delay(1000);                                                  
    myServo.write(180);              
    delay(1000); 
    distanciaIzquierda = medirDistancia();

    Serial.print("distanciaIzquierda: ");
    Serial.println(distanciaIzquierda);

    delay(500);
    myServo.write(90);              
    delay(1000);
  }*/

}
