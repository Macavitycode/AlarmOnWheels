
from time import sleep, time
import RPi.GPIO as GPIO


class DifferentialDrive:
    """
    Class to control simple differential drive using the L289N motor driver;
    needs to be expanded with pwm support later
    """

    def stop(self):
        """
        Method to stop all movement
        """
        GPIO.output(self.l_1, 0)
        GPIO.output(self.l_2, 0)
        GPIO.output(self.r_1, 0)
        GPIO.output(self.r_2, 0)

        sleep(0.75)

    def move_forward(self, hold_time):
        """
        Method to move forward without pwm for a set amount of time
        """

        GPIO.output(self.l_1, 1)
        GPIO.output(self.l_2, 0)
        GPIO.output(self.r_1, 0)
        GPIO.output(self.r_2, 1)

        sleep(hold_time)

        self.stop()

    def move_backward(self, hold_time):
        """
        Method to move backwards without pwm for a set amount of time
        """

        GPIO.output(self.l_1, 0)
        GPIO.output(self.l_2, 1)
        GPIO.output(self.r_1, 1)
        GPIO.output(self.r_2, 0)

        sleep(hold_time)

        self.stop()

    def turn_left(self, hold_time):
        """
        Method to turn left without pwm for a set amount of time
        """

        GPIO.output(self.l_1, 1)
        GPIO.output(self.l_2, 0)
        GPIO.output(self.r_1, 1)
        GPIO.output(self.r_2, 0)

        sleep(hold_time)

        self.stop()

    def turn_right(self, hold_time):
        """
        Method to turn right without pwm for a set amount of time
        """

        GPIO.output(self.l_1, 0)
        GPIO.output(self.l_2, 1)
        GPIO.output(self.r_1, 0)
        GPIO.output(self.r_2, 1)

        sleep(hold_time)

        self.stop()

    def move_square(self, side, hold_time):
        """
        Method to move in roughly a square
        """

        print('Moving in a square started')
        t_end = time() + hold_time
        while time() < t_end:
            self.move_backward(side)
            self.turn_right(0.25)
            self.move_backward(side)
            self.turn_right(0.25)
            self.move_backward(side)
            self.turn_right(0.25)
            self.move_backward(side)
            self.turn_right(0.25)

        print('Moving in a square done')

    def __init__(self, l_1, l_2, r_1, r_2, l_pwm=0, r_pwm=0):
        """
        Requires gpio pins connected to IN1~IN4 respectively
        If pwm is required input the GPIO pins for INA and INB
        There is no pwm support for now
        """

        self.l_1 = l_1
        self.l_2 = l_2
        self.r_1 = r_1
        self.r_2 = r_2

        self.l_pwm = l_pwm
        self.r_pwm = r_pwm

        GPIO.setup(l_1, GPIO.OUT, initial=0)
        GPIO.setup(l_2, GPIO.OUT, initial=0)
        GPIO.setup(r_1, GPIO.OUT, initial=0)
        GPIO.setup(r_2, GPIO.OUT, initial=0)

        self.stop()
        print('DifferentialDrive is setup')
