"""
Program to make the differential drive bot work like an alarm bot
"""

import threading
from time import sleep, time
from datetime import datetime

import RPi.GPIO as GPIO

from DifferentialDrive import DifferentialDrive
from Buzzer import Buzzer


if __name__=="__main__":

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    bot = DifferentialDrive(11, 7, 10, 8)
    buz = Buzzer(40)

    format_flag = 0

    while format_flag == 0:

        alarm_in = input(
                'How many minuets do you want the alarm in? (enter as float) :')
        try:
            alarm_in = float(alarm_in)
            format_flag = 1
            print('alarm set for ', alarm_in, ' minuets')

        except ValueError:
            print('format is wrong')


    sleep(alarm_in * 60)


    buzzer_thread = threading.Thread(target=buz.b_beep, args=(0.1,))
    driver_thread = thread = threading.Thread(target=bot.move_square, args=(0.5,4,))

    buzzer_thread.start()
    driver_thread.start()

    buzzer_thread.join()
    driver_thread.join()

    print('All Done! :)')

    GPIO.cleanup()

