char nothing = 'N';
char left = 'L';
char right = 'R';  
char incomingByte;

void setup()
{
  Serial.begin(9600);
  Serial.println("Ready"); // print "Ready" once
  pinMode(3,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(13,OUTPUT);
  digitalWrite(10,HIGH);
  digitalWrite(13,LOW);

}
void loop()
{
  
  if(Serial.available())
  {
     incomingByte=Serial.read();
    Serial.println(incomingByte);
  if(incomingByte == right)
    {
      while (incomingByte == right)
      {
      digitalWrite(3,HIGH);
      digitalWrite(6,LOW);
      delay(20);
      }
    }
    else
    if(incomingByte == left)
    {
      while (incomingByte == right)
      {
      digitalWrite(6,HIGH);
      digitalWrite(3,LOW);
      delay(20);
      }
    }
    else
     (incomingByte == nothing);
    {  
      while (incomingByte == right)
      {
      digitalWrite(6,LOW);
      digitalWrite(3,LOW);
      delay(20);
      }
    }
    }

}
   
