
const int ledPin = 13;// the pin that the LED is attached to
int data;      // a variable to read incoming serial data into

const byte OC1A_PIN = 9;
const byte OC1B_PIN = 10;

const word PWM_FREQ_HZ = 25000; //Adjust this value to adjust the frequency (Frequency in HZ!) (Set currently to 25kHZ)
const word TCNT1_TOP = 16000000 / (2 * PWM_FREQ_HZ);


void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);

  //MOTOR PWN SIGNAL
  pinMode(OC1A_PIN, OUTPUT);

  // Clear Timer1 control and count registers
  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1  = 0;

  TCCR1A |= (1 << COM1A1) | (1 << WGM11);
  TCCR1B |= (1 << WGM13) | (1 << CS10);
  ICR1 = TCNT1_TOP;
}

void setPwmDuty(byte duty) {
  OCR1A = (word) (duty * TCNT1_TOP) / 100;
}

void loop() {
  /*
      //testing the motor
      setPwmDuty(10);
      delay(3000);
      setPwmDuty(50); //Change this value 0-100 to adjust duty cycle
      delay(3000);
  */

  if (Serial.available() > 0)
  {
    data = Serial.read();
    digitalWrite(ledPin, HIGH);

    //-------------------秦皇岛-------------------
    //https://aqicn.org/city/hebei/qinhuangdaoshi/shijiancezhan/cn/
    if (data == 'A') {
      Serial.println("AQI in QinHuangDao is GREEN(0-50)");
      setPwmDuty(25);

    }
    if (data == 'B') {
      Serial.println("AQI in qinhuangdao is YELLOW(50-100)");
      setPwmDuty(35);
    }

    if (data == 'C') {
      Serial.println("AQI in qinhuangdao is ORANGE(100-150)");
      setPwmDuty(70);
    }

    if (data == 'D') {
      Serial.println("AQI in qinhuangdao is RED(150-200)");
      setPwmDuty(90);
    }

    if (data == 'E') {
      Serial.println("AQI in qinhuangdao is PURPLE(above200)");
      setPwmDuty(100);
    }

    //-------------------山海关-------------------
    //https://aqicn.org/city/hebei/qinhuangdaoshi/diyiguan/cn/
    if (data == 'F') {
      Serial.println("AQI in shanhaiguan is GREEN(0-50)");
    }
    if (data == 'G') {
      Serial.println("AQI in shanhaiguan is YELLOW(50-100)");
    }

    if (data == 'H') {
      Serial.println("AQI in shanhaiguan is ORANGE(100-150)");
    }

    if (data == 'I') {
      Serial.println("AQI in shanhaiguan is RED(150-200)");
    }

    if (data == 'J') {
      Serial.println("AQI in shanhaiguan is PURPLE(above200)");
    }

    //-------------------昌黎县-------------------
    //https://aqicn.org/city/hebei/qinhuangdaoshi/changlihuanbaoju/cn/
    if (data == 'K') {
      Serial.println("AQI in changlixian is GREEN(0-50)");
    }
    if (data == 'L') {
      Serial.println("AQI in changlixian is YELLOW(50-100)");
    }

    if (data == 'M') {
      Serial.println("AQI in changlixian is ORANGE(100-150)");
    }

    if (data == 'N') {
      Serial.println("AQI in changlixian is RED(150-200)");
    }

    if (data == 'O') {
      Serial.println("AQI in changlixian is PURPLE(above200)");
    }

    //-------------------抚宁党校-------------------
    //https://aqicn.org/city/hebei/qinhuangdaoshi/funingdangxiao/cn/
    if (data == 'P') {
      Serial.println("AQI in funing is GREEN(0-50)");
    }
    if (data == 'Q') {
      Serial.println("AQI in funing is YELLOW(50-100)");
    }

    if (data == 'R') {
      Serial.println("AQI in funing is ORANGE(100-150)");
    }

    if (data == 'S') {
      Serial.println("AQI in funing is RED(150-200)");
    }

    if (data == 'T') {
      Serial.println("AQI in funing is PURPLE(above200)");
    }

    //-------------------北戴河-------------------
    //https://aqicn.org/city/hebei/qinhuangdaoshi/beidaihe/cn/
    if (data == 'U') {
      Serial.println("AQI in beiedaihe is GREEN(0-50)");
    }
    if (data == 'V') {
      Serial.println("AQI in beiedaihe is YELLOW(50-100)");
    }

    if (data == 'W') {
      Serial.println("AQI in beiedaihe is ORANGE(100-150)");
    }

    if (data == 'X') {
      Serial.println("AQI in beiedaihe is RED(150-200)");
    }

    if (data == 'Y') {
      Serial.println("AQI in beiedaihe is PURPLE(above200)");
    }

    //-------------------卢龙县-------------------
    //https://aqicn.org/city/hebei/qinhuangdaoshi/lulongxianqixiangju/cn/
    if (data == 'Z') {
      Serial.println("AQI in lulongxian is GREEN(0-50)");
    }
    if (data == '0') {
      Serial.println("AQI in lulongxian is YELLOW(50-100)");
    }

    if (data == '1') {
      Serial.println("AQI in lulongxian is ORANGE(100-150)");
    }

    if (data == '2') {
      Serial.println("AQI in lulongxian is RED(150-200)");
    }

    if (data == '3') {
      Serial.println("AQI in lulongxian is PURPLE(above200)");
    }

    //-------------------山海关区政府-------------------
    //https://aqicn.org/city/hebei/qinhuangdaoshi/shanhaiguanquzhengfu
        if (data == '4') {
      Serial.println("AQI in shanhaiguanquzhengfu is GREEN(0-50)");
    }
    if (data == '5') {
      Serial.println("AQI in shanhaiguanquzhengfu is YELLOW(50-100)");
    }

    if (data == '6') {
      Serial.println("AQI in shanhaiguanquzhengfu is ORANGE(100-150)");
    }

    if (data == '7') {
      Serial.println("AQI in shanhaiguanquzhengfu is RED(150-200)");
    }

    if (data == '8') {
      Serial.println("AQI in shanhaiguanquzhengfu is PURPLE(above200)");
    }


  }

}
