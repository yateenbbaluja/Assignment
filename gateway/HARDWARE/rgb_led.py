import RPi.GPIO as GPIO
from CONFIGURATION.config import confi
from termcolor import colored

class LED:
    def __init__(self):
        self.config = confi()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.config.RED_LED, GPIO.OUT)
        GPIO.setup(self.config.GREEN_LED, GPIO.OUT)
        print(colored("GPIO INIT SUCCESS", "red"))

    def red_led_on(self):
        GPIO.output(self.config.RED_LED, True)
        print(colored("RED_LED IS TURN ON", "green"))


    def green_led_on(self):
        GPIO.output(self.config.GREEN_LED, True)
        print(colored("GREEN_LED IS TURN ON", "green"))

    def red_led_off(self):
        GPIO.output(self.config.RED_LED, False)
        print(colored("RED_LED IS TURN OFF", "green"))


    def green_led_off(self):
        GPIO.output(self.config.GREEN_LED, False)
        print(colored("GREEN_LED IS TURN ON", "green"))