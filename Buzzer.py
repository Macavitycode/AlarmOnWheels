
from time import sleep, time
import RPi.GPIO as GPIO

class Buzzer:
    """
    Class to control a buzzer
    """

    def b_off(self):
        """
        Switches the buzzer off
        """

        GPIO.output(self.p, 0)

    def b_on(self):
        """
        Switches the buzzer on
        """

        GPIO.output(self.p, 1)

    def b_beep(self, time_period):
        """
        Switches the buzzer on and off for the given time period for total
        of alarm_length seconds
        """

        print('Buzzing started')
        t_end = time() + self.alarm_length
        while time() < t_end:

            self.b_on()
            sleep(time_period)
            self.b_off()
            sleep(time_period)

        print('Buzzing done')

    def __init__(self, p, alarm_length=5):
        """
        Requires the pin connected to the buzzer
        """

        self.p = p
        self.alarm_length = alarm_length

        GPIO.setup(p, GPIO.OUT, initial=0)
        self.b_off()

        print('Buzzer is setup')

