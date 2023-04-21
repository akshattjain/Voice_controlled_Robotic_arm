import RPi.GPIO as GPIO
import speech_recognition as sr
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

signal=GPIO.PWM(3,50) # servo for up down movement 
signal=GPIO.PWM(4,50) # servo for right to left movement
signal=GPIO.PWM(5,50) # servo for holding 

signal.start(0)

r = sr.Recognizer()

def cmd():
    with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
			
    try:
       MyText = r.recognize_google(audio2)
       MyText = MyText.lower()
    except sr.RequestError as e:
  
        MyText='None'
		
    except sr.UnknownValueError:
        
        MyText='None'
    return MyText


def SetAngle(angle):
	duty = (angle / 18) + 2
	GPIO.output(3, True)
	signal.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(3, False)
	signal.ChangeDutyCycle(0)
    signal.stop()
    GPIO.cleanup()


def SetAngle2(angle):
	duty = angle / 18 + 2
	GPIO.output(4, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(4, False)
	pwm.ChangeDutyCycle(0)
    signal.stop()
    GPIO.cleaup()

def SetAngle3(angle):
	duty = angle / 18 + 2
	GPIO.output(4, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(4, False)
	pwm.ChangeDutyCycle(0)
    signal.stop()
    GPIO.cleaup()
    
    
if __name__=='__main__':
    while (True):
        query=cmd()
        if query=='go fifteen degree down':
            angle=15
            SetAngle(angle)
        elif query=='go thirty degree down':
            angle=30
            SetAngle(angle)
        elif query=='go fourty five degree down':
            angle=45
            SetAngle(angle)
        
        elif query=='go sixty degree down':
            angle=60
            SetAngle(angle)
        
        elif query=='go ninty degree down':
            angle=90
            SetAngle(angle)
        elif query=='rotate fifteen degree':
            angle=15
            SetAngle2(angle)
        elif query=='rotate thirty degree':
            angle=30
            SetAngle2(angle)
        elif query=='rotate foutry five degree':
            angle=45
            SetAngle2(angle)
        elif query=='rotate sixty degree':
            angle=60
            SetAngle2(angle)
        elif query=='rotate ninty degree':
            angle=90
            SetAngle2(angle)
        elif query=='rotate one hundred and thirty five degree':
            angle=135
            SetAngle2(angle)
        elif query=='rotate one hundred and fifty degree':
            angle=150
            SetAngle2(angle)
        elif query=='rotate one hundred and sixty five degree':
            angle=165
            SetAngle2(angle)
        elif query=='rotate one hundred and eighty degree':
            angle=180
            SetAngle2(angle)
        elif query=='hold it':
            angle=90
            SetAngle3(angle)
        
    
    
    
    
    
    
    
    
    
