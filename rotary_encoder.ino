#define outputA 6
#define outputB 7
int counter = 0; 
int aState;
int aLastState;  

void setup() { 
   pinMode (outputA,INPUT);
   pinMode (outputB,INPUT);
   
   Serial.begin (9600);
   // Reads the initial state of the outputA
   aLastState = digitalRead(outputA);   
} 
 
void loop() { 
   aState = digitalRead(outputA); // Reads the "current" state of the outputA
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(outputB) != aState) { 
       counter ++;
     } else {
       counter --;
     }

     if (abs(counter) >= 40){
      counter = counter % 40;
     }

  //0 empty, 1 drawer, 2 book, 3 lamp, 4 chair
     
     if (counter < -3){
      Serial.println(0);
     }
     if (counter <-1){
      Serial.println(1);
     }
     else if (counter <1){
      Serial.println(4);
     }
     else if (counter <2){
      Serial.println(3);
     }
     else if (counter <4){
      Serial.println(2);
     }
     else {
      Serial.println(0);
     }
     


   aLastState = aState; // Updates the previous state of the outputA with the current state

 }
}
