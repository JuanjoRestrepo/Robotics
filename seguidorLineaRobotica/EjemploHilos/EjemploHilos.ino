unsigned long tiempo1, tiempo2;
unsigned long tx = 0, ty = 0;
int estadoLed1 = LOW, estadoLed2 = LOW;

void setup() {
  Serial.begin(9600);
  pinMode(31, OUTPUT);
  pinMode(33, OUTPUT);
}

void loop() {
  digitalWrite(31, estadoLed1);
  digitalWrite(33, estadoLed2);
  tiempo1 = millis();
  tiempo2 = millis();
  
  if (tiempo1 - tx == 500){
    tx = tiempo1;
    estadoLed1 = !estadoLed1;
    Serial.print("\nTiempo 1: ");
    Serial.print(tiempo1);
    Serial.print(" ENCENDIDO 1");
  }
  if (tiempo2 - ty == 2000){
    ty = tiempo2;
    estadoLed2 = !estadoLed2;
    Serial.print("\nTiempo 2: ");
    Serial.print(tiempo2);
    Serial.print(" ENCENDIDO 2");
  }

}
