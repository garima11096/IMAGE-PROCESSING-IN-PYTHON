char nothing = 'N';
char left = 'L';
char right = 'R';  
char incomingByte;

//sn754410
void setup()
{
  Serial.begin(9600);
  Serial.println("Ready"); // print "Ready" once
  pinMode(5,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(11,OUTPUT);
  digitalWrite(8,HIGH);
digitalWrite(11,LOW);
 

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
        digitalWrite(5,HIGH);
      digitalWrite(7,LOW);
      delay(20);
      } 
    }
    if(incomingByte == left)
    {
      while (incomingByte == left)
      {
      digitalWrite(7,HIGH);
      digitalWrite(5,LOW);
      delay(20);
      }   
    }
    if
     (incomingByte == nothing);
    {
       while (incomingByte == nothing)
      {
        digitalWrite(7,LOW);
      digitalWrite(5,LOW);
      delay(20);
      }    
    }
    }

}
   
