import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.OUT)
while(1):
        print("LED ACESO\n")
        GPIO.output(14, 1)
        time.sleep(1)
        print("LED APAGADO\n")
        GPIO.output(14, 0)
        time.sleep(1)


