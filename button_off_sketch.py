import RPi.GPIO as GPIO
import os


gpio_pin_number=23

gpio_pin_number_led=24


GPIO.setmode(GPIO.BCM)

GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_pin_number_led, GPIO.OUT)

try:
    GPIO.output(gpio_pin_number_led, True)
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    print("Shutdown is starting...")
    #os.system("sudo shutdown -h now")
except:
    pass

GPIO.cleanup()
