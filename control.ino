#include <Servo.h>

//Digital Pins
const int motorIn1 = 4;
const int motorIn2 = 5;
const int motorIn3 = 6;      
const int motorIn4 = 7;  
    
const int enA = 9; 
const int enB = 10; 
Servo myservo; 
String inByte;
int pos;
int degree;
int speed = 148; //max speed = 255
#define pos_ini 0

void setup() 
{
    Serial.begin(9600);     //  Make sure the baud rate is 9600
    pinMode(motorIn1, OUTPUT);
    pinMode(motorIn2, OUTPUT);
    pinMode(motorIn3, OUTPUT);
    pinMode(motorIn4, OUTPUT);
    pinMode(enA, OUTPUT);
    pinMode(enB, OUTPUT);
    myservo.attach(3);   // servo pin attach to Pin 3
    myservo.write(pos_ini);  //setup initial position  
}

void loop() 
{
    if(Serial.available())  //  If there are any data receieved
    {  
        char cmd = Serial.read();
        switch (cmd) 
        {
            case 'f':        // recieve 'r', go forward
            forward();
            break;

            case 'b':        // recieve 'r', go backward
            backward();
            break;

            case 'l':        // recieve 'l', turn left
            left();
            break;

            case 'r':        // recieve 'r', turn right
            right();
            break;

            case 's':
            motorstop();     // stop the motors
            break;

            case 't':
            servoturn(30);
            break;

            case 'u':
            servoturn(60);
            break;

            default:
            break;
        }
        
        Serial.flush();
    }
    delay(10); 
}  


void servoturn(int degree)
{
        //inByte = Serial.readStringUntil('\n'); // read data until newline
        //degree = inByte.toInt();
        
        for(pos = 0; pos <= 180; pos += degree)  // goes from 0 degrees to 180 degrees 
        {                                    
          int j = pos;
          for(int i = j; i <= pos + degree; i += 1){
            myservo.write(i);               
            delay(20);
          }
          delay(1800);                       
        } 
        for(int i =180; i>=0; i -= 1){
            myservo.write(i);               
            delay(15);
        }
}  

void motorstop()
{
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, LOW);
  digitalWrite(motorIn3, LOW);
  digitalWrite(motorIn4, LOW);
}

void forward() 
{
  //digitalWrite(motorIn1, HIGH);
  //digitalWrite(motorIn2, LOW);
  //digitalWrite(motorIn3, HIGH);
  //digitalWrite(motorIn4, LOW);

  analogWrite(motorIn1, speed); 
  analogWrite(motorIn2, 0);
  analogWrite(motorIn3, speed);
  analogWrite(motorIn4, 0);

  analogWrite(enB, 200);
  analogWrite(enA, 200);
}

void backward()  
{
  //digitalWrite(motorIn1, LOW);
  //digitalWrite(motorIn2, HIGH);
  //digitalWrite(motorIn3, LOW);
  //digitalWrite(motorIn4, HIGH);
  analogWrite(motorIn1, 0); 
  analogWrite(motorIn2, speed);
  analogWrite(motorIn3, 0);
  analogWrite(motorIn4, speed);
  analogWrite(enB, 200);
  analogWrite(enA, 200);
}

void right()
{
  //digitalWrite(motorIn1, LOW);
  //digitalWrite(motorIn2, HIGH);
  //digitalWrite(motorIn3, HIGH);
  //digitalWrite(motorIn4, LOW);
  analogWrite(motorIn1, 0); 
  analogWrite(motorIn2, speed);
  analogWrite(motorIn3, speed);
  analogWrite(motorIn4, 0);
  analogWrite(enB, 200);
  analogWrite(enA, 200);
}

void left()
{
  //digitalWrite(motorIn1, HIGH);
  //digitalWrite(motorIn2, LOW);
  //digitalWrite(motorIn3, LOW);
  //digitalWrite(motorIn4, HIGH);
  analogWrite(motorIn1, speed); 
  analogWrite(motorIn2, 0);
  analogWrite(motorIn3, 0);
  analogWrite(motorIn4, speed);
  analogWrite(enB, 200);
  analogWrite(enA, 200);
}
