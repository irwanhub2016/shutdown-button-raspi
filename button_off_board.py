import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
GPIO.setup(18, GPIO.OUT)  #LED to GPIO24

try:
    while True:
         button_state = GPIO.input(23)
         if button_state == False:
             GPIO.output(24, True)
             print('Button Pressed...')
             time.sleep(0.2)
         else:
             GPIO.output(24, False)
except:
    GPIO.cleanup()
