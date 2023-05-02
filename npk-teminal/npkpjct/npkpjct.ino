
#include <DFRobot_DHT11.h>
DFRobot_DHT11 DHT;
#define DHT11_PIN 10
const int potPin=A0;
float ph;
float Value=0;
float temp;
float hum;














void setup()

{

  
    // Starts the serial communication
  Serial.begin(9600);
  pinMode(potPin,INPUT);
  
  randomSeed(analogRead(5));
}
int flag=0;
void header(){

Serial.println("N,P,K,TEMPERATURE,HUMIDITY,PH");
flag=1;
}

void loop(void)

{
if(flag == 0){
  header();
}
  int randNumber;
   // Clears the trigPin
  Value= analogRead(potPin);
   // Serial.print(Value);
    randNumber = random(10,140);
    Serial.print(randNumber);
    Serial.print(",");
    randNumber = random(5,145);
    Serial.print(randNumber);
    Serial.print(",");
    randNumber = random(5,205);
    Serial.print(randNumber);
    Serial.print(",");
    float voltage=Value*(3.3/4095.0);
    ph=(3.3*voltage);
    
     DHT.read(DHT11_PIN);
  //Serial.print(" temp:");
  temp = DHT.temperature;
  Serial.print(DHT.temperature);
  Serial.print(",");
  hum = DHT.humidity;
  Serial.print(DHT.humidity);
    Serial.print(",");
    Serial.println(ph+4);
    
    
  delay(10000);
  
}








