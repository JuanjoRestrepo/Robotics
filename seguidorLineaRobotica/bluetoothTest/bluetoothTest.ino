
#include <SoftwareSerial.h>

/* Programa el modulo bluetooth HC-06 con un nuevo: 
  NOMBRE  (Nombre de 20 caracteres)
  PIN     (Clave de cuatro numeros)
  BPS     (Velocidad de conexion en baudios)
  
  Tienda donde se compro el modulo: http://dinastiatecnologica.com/producto/modulo-bluetooth-hc-05/
  By: http://elprofegarcia.com
  
  CONEXIONES:
  ARDUINO   BLUETOOTH
  5V        VCC
  GND       GND
  PIN 2     TX
  PIN 3     RX
  
 */

SoftwareSerial blue(10, 11);   //Crea conexion al bluetooth - PIN 2 a TX y PIN 3 a RX

void setup()
{
    
    Serial.begin(9600);
    Serial.println("Enter AT commands: ");
    blue.begin(9600); // inicialmente la comunicacion serial a 9600 Baudios (velocidad de fabrica)
    
}
 
void loop()
{
    if (blue.available() ){
      Serial.write(blue.read() );
    }
    if(Serial.available() ){
      blue.write(Serial.read() );
    }
}
