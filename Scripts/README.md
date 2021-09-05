# Working With L298N Motor Driver and a Buzzer for Raspberry Pi

The code base is split object-wise. Before running make sure you have the installed the following libraries (all available in pip3):

```
RPi.GPIO
datetime
threading
```

Also make sure all the files are in the same directory or are on path.

## To Use

```
python3 main.py
```

When prompted enter the time delay needed in minuets.

## [Differential Drive](DifferentialDrive.py)

Class for a differential drive with L298N. Class takes the pins for IN1 through IN4 as well as ENA and ENB if PWM is needed (not implemented yet). Methods are broken down logically and used as needed. PWM has not been implemented yet fully.

## [Buzzer](Buzzer.py)

Class for a buzzer. Has a beep method which takes in the pin, the frequency and  then beeps.

## [Main](main.py)

The main file to be run. Takes input as a float and sets an alarm for that much time. Once the time is up the movement function as well as the buzzer beeping function are run parallelly through the threading library. If you want to change what the bot does change the targets given to the treads.
