// Define motor control pins
const int motor1A = 2;
const int motor1B = 3;
const int motor2A = 4;
const int motor2B = 7;

// Define IR sensor pins
const int sensor1 = 8;  // Replace with your digital pin numbers
const int sensor2 = 9;
const int sensor3 = 10;
const int sensor4 = 11;

// Define speed control pins
const int speedControl1 = 6;
const int speedControl2 = 5;

// Define speed variables
int baseSpeed = 110;  // Base speed for both motors
int speedDifference = 0;  // Speed difference for turning

void setup() {
  // Set motor control pins as output
  pinMode(motor1A, OUTPUT);
  pinMode(motor1B, OUTPUT);
  pinMode(motor2A, OUTPUT);
  pinMode(motor2B, OUTPUT);

  // Set speed control pins as output
  pinMode(speedControl1, OUTPUT);
  pinMode(speedControl2, OUTPUT);

  // Set IR sensor pins as input
  pinMode(sensor1, INPUT);
  pinMode(sensor2, INPUT);
  pinMode(sensor3, INPUT);
  pinMode(sensor4, INPUT);

}

// Path Mode 

// Mode 0 : black background white strip 
// Mode 1 : white background black strip 
// Mode 2 : left black and right white 
// Mode 3 : left white and right black

int mode = 0;

int checkDelay = 200;

int first = 0;
long allSameTime = 0;

int loopMode = 0 ;

void loop() {

  // delay(checkDelay);

  // Read sensor values
  int val1 = digitalRead(sensor1);
  int val2 = digitalRead(sensor2);
  int val3 = digitalRead(sensor3);
  int val4 = digitalRead(sensor4);

  if (!((val1 == LOW && val2 == LOW && val3 == LOW && val4 == LOW)||(val1 == HIGH && val2 == HIGH && val3 == HIGH && val4 == HIGH))){
    first = 0;
  }

  if (!((val1 == HIGH && val2 == LOW && val3 == LOW && val4 == HIGH)||(val1 == LOW && val2 == HIGH && val3 == HIGH && val4 == LOW))){
    loopMode = 0;
  }

  // Implement line following logic
  if (val1 == LOW && val2 == LOW && val3 == LOW && val4 == LOW) {
    // delay(checkDelay);
    // continue;

    loopMode = 1;
    
    if (first == 0){
      allSameTime = millis();
      first = 1;
    }
    else if (first == 1){
      if (millis() - allSameTime < 1000){
        moveForward();   
      }
      else{
        stopMotors();
      }
    }

     
    mode = 0;

  } else if (val1 == LOW && val2 == LOW && val3 == LOW && val4 == HIGH) {
    // Case 2: Only sensor4 on the line
    // delay(checkDelay);
    // continue;

    if (mode == 1){
      turnLeft();
    }else if (mode == 2){
      turnRight();
    }

  } else if (val1 == LOW && val2 == LOW && val3 == HIGH && val4 == LOW) {
    // Case 3: Only sensor3 on the line
    // delay(checkDelay);
    // continue;

    turnRight();
    mode = 0;
    
  } else if (val1 == LOW && val2 == LOW && val3 == HIGH && val4 == HIGH) {
    // Case 4: Sensors 3 and 4 on the line
    // delay(checkDelay);
    // continue;

    moveForward();
    mode = 2 ;

  } else if (val1 == LOW && val2 == HIGH && val3 == LOW && val4 == LOW) {
    // Case 5: Only sensor2 on the line
    // delay(checkDelay);
    // continue;

    turnLeft();
    mode = 0;

  } else if (val1 == LOW && val2 == HIGH && val3 == LOW && val4 == HIGH) {
    // Case 6: Sensors 2 and 4 on the line
    // delay(checkDelay);
    // continue;

  } else if (val1 == LOW && val2 == HIGH && val3 == HIGH && val4 == LOW) {
    // Case 7: Sensors 2 and 3 on the line
    // delay(checkDelay);
    // continue;

    if (loopMode == 1){
      turnLeft();
      mode = 1;
    }else{
      moveForward();
      mode = 0;
    }

    

  } else if (val1 == LOW && val2 == HIGH && val3 == HIGH && val4 == HIGH) {
    // Case 8: Sensors 2, 3, and 4 on the line
    // delay(checkDelay);
    // continue;

    if (mode == 0){
      turnRight();
    }else if (mode == 2){
      turnLeft();
    }

  } else if (val1 == HIGH && val2 == LOW && val3 == LOW && val4 == LOW) {
    // Case 9: Only sensor1 on the line
    // delay(checkDelay);
    // continue;

    if (mode == 1){
      turnRight();
    }else if (mode == 3){
      turnLeft();
    }

  } else if (val1 == HIGH && val2 == LOW && val3 == LOW && val4 == HIGH) {
    // Case 10: Sensors 1 and 4 on the line
    // delay(checkDelay);
    // continue;

    if (loopMode == 1){
      turnLeft();
      mode = 0;
    }else{
      moveForward();
      mode = 1;
    }

    

  } else if (val1 == HIGH && val2 == LOW && val3 == HIGH && val4 == LOW) {
    // Case 11: Sensors 1 and 3 on the line
    // delay(checkDelay);
    // continue;

  } else if (val1 == HIGH && val2 == LOW && val3 == HIGH && val4 == HIGH) {
    // Case 12: Sensors 1, 3, and 4 on the line
    // delay(checkDelay);
    // continue;

    turnLeft();
    mode = 1;

  } else if (val1 == HIGH && val2 == HIGH && val3 == LOW && val4 == LOW) {
    // Case 13: Sensors 1 and 2 on the line
    // delay(checkDelay);
    // continue;

    moveForward();
    mode = 3;
  } else if (val1 == HIGH && val2 == HIGH && val3 == LOW && val4 == HIGH) {
    // Case 14: Sensors 1, 2, and 4 on the line
    // delay(checkDelay);
    // continue;

    turnRight();
    mode = 1;

  } else if (val1 == HIGH && val2 == HIGH && val3 == HIGH && val4 == LOW) {
    // Case 15: Sensors 1, 2, and 3 on the line
    // delay(checkDelay);
    // continue;

    if (mode == 0){
      turnLeft();
    }else if (mode == 3){
      turnRight();
    }

  } else if (val1 == HIGH && val2 == HIGH && val3 == HIGH && val4 == HIGH) {
  //  case 16:
    // delay(checkDelay);
    // continue;

    loopMode = 1;
    
    if (first == 0){
      allSameTime = millis();
      first = 1;
    }
    else if (first == 1){
      if (millis() - allSameTime < 1000){
        moveForward();   
      }
      else{
        stopMotors();
      }
    }

     mode = 1;

  }

}



// Function to move the robot forward
void moveForward() {
  digitalWrite(motor1A, HIGH);
  digitalWrite(motor1B, LOW);
  digitalWrite(motor2A, HIGH);
  digitalWrite(motor2B, LOW);
  
  analogWrite(speedControl1, baseSpeed);
  analogWrite(speedControl2, baseSpeed);
}

// Function to turn the robot left
void turnLeft() {
  digitalWrite(motor1A, HIGH);
  digitalWrite(motor1B, LOW);
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, HIGH);
  
  analogWrite(speedControl1, baseSpeed);
  analogWrite(speedControl2, baseSpeed - speedDifference);
}

// Function to turn the robot right
void turnRight() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, HIGH);
  digitalWrite(motor2A, HIGH);
  digitalWrite(motor2B, LOW);
  
  analogWrite(speedControl1, baseSpeed - speedDifference);
  analogWrite(speedControl2, baseSpeed);
}

// Function to stop the motors
void stopMotors() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, LOW);
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, LOW);
}
