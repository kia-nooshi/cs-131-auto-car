
// C++ code
//


const int b2 = 2;
const int b3 = 3;
const int b4 = 4;
const int b5 = 5;
const int b6 = 6;
const int b7 = 7;
const int echoPin = 10;
const int trigPin = 9;
const int b11 = 11;
const int b12 = 12;
int a = 0x00;
int a0, a1, a2, a3, a4, a5, a6, a7;


void setup()
{
Serial.begin(9600);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);

pinMode(b2, OUTPUT);
pinMode(b3, OUTPUT);
pinMode(b4, OUTPUT);
pinMode(b5, OUTPUT);
pinMode(b6, OUTPUT);
pinMode(b7, OUTPUT);
pinMode(A0, INPUT);

const int trigPin = 9;
const int echoPin = 8;






}

typedef struct task {
  int state;
  unsigned long period;
  unsigned long elapsedTime;
  int (*TickFct)(int);
} task;



int count;
long duration, inches, cm;


long microsecondsToInches(long microseconds) {
  return microseconds / 74 / 2;
}


enum LS2_States { LS2_Start, green1, yellow1, red1, green2, yellow2, red2 } state = LS2_Start;
int TickFct_LS2(){
  switch(state){
    case LS2_Start:
      count = 0;
      state = green1;
      break;
    case green1:
      Serial.println("Green Light");
      digitalWrite(b3, HIGH);
      digitalWrite(b5, LOW);
      digitalWrite(b7, LOW);
      
      digitalWrite(b2, LOW);
      digitalWrite(b4, LOW);
      digitalWrite(b6, HIGH);

      /*if(inches < 6){
        count = count + 4;
      }*/
      if(count >= 8){
        count = 0;
        state = yellow1;
      }
      else{
        count++;
        state = green1;
      }
     break;

    case yellow1:
      Serial.println("Yellow Light");
      digitalWrite(b3, LOW);
      digitalWrite(b5, HIGH);
      digitalWrite(b7, LOW);

      digitalWrite(b2, LOW);
      digitalWrite(b4, LOW);
      digitalWrite(b6, HIGH);
      if(count == 4){
        count = 0;
        state = red1;
      }
      else{
        count++;
        state = yellow1;
      }
     break;

    case red1:
      Serial.println("Red Light");
      digitalWrite(b3, LOW);
      digitalWrite(b5, LOW);
      digitalWrite(b7, HIGH);

      digitalWrite(b2, LOW);
      digitalWrite(b4, LOW);
      digitalWrite(b6, HIGH);
      if(count == 1){
        count = 0;
        state = green2;
      }
      else{
        count++;
        state = red1;
      }
     break;


    case green2:
      //Serial.println("Green Light");
      digitalWrite(b3, LOW);
      digitalWrite(b5, LOW);
      digitalWrite(b7, HIGH);

      digitalWrite(b2, HIGH);
      digitalWrite(b4, LOW);
      digitalWrite(b6, LOW);
      if(count >= 8){
        count = 0;
        state = yellow2;
      }
      else{
        count++;
        state = green2;
      }
     break;

    case yellow2:
      //Serial.println("Yellow Light");
      digitalWrite(b3, LOW);
      digitalWrite(b5, LOW);
      digitalWrite(b7, HIGH);

      digitalWrite(b2, LOW);
      digitalWrite(b4, HIGH);
      digitalWrite(b6, LOW);
      if(count == 4){
        count = 0;
        state = red2;
      }
      else{
        count++;
        state = yellow2;
      }
     break;

    case red2:
      //Serial.println("Red Light");
      digitalWrite(b3, LOW);
      digitalWrite(b5, LOW);
      digitalWrite(b7, HIGH);

      digitalWrite(b2, LOW);
      digitalWrite(b4, LOW);
      digitalWrite(b6, HIGH);
      if(count == 1){
        count = 0;
        state = green1;
      }
      else{
        count++;
        state = red2;
      }
     break;

    
     

    default:
      state = LS2_Start;
  }
  switch(state){
    case LS2_Start:
      break;

    

    default:
      break;
  }
}
  
  
  
enum States2{START, READ} state2 = START;//All the states are declared here} state;
//Some G;pba; Variables
void Tick2(){
    //Read thing
    switch(state2){ // State transitions
      
      case START:
         state2 = READ;
        break;

      case READ:
         
        break;
      
     default:
        state2 = START;
         break;
    }
    switch(state2){ // State Action
      case START:
         break;
      case READ:
         digitalWrite(trigPin, LOW);
         delayMicroseconds(2);
         digitalWrite(trigPin, HIGH);
         delayMicroseconds(10);
         digitalWrite(trigPin, LOW);
         duration = pulseIn(echoPin, HIGH);
         inches = microsecondsToInches(duration);
        break;
        
      default:
      break;
    }
}










void loop() {
  // put your main code here, to run repeatedly:

  TickFct_LS2();
  Tick2();
  delay(250);
}
