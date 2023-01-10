import keyboard
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


pins = [17, 22, 23, 24, 26, 27]

wasDict = {
    "w": ["HIGH", "LOW", "HIGH", "LOW"],
    "s": ["LOW", "HIGH", "LOW", "HIGH"],
    "a": ["LOW", "HIGH", "HIGH", "LOW"],
    "d": ["HIGH", "LOW", "LOW", "HIGH"],
    "e": ["LOW", "LOW", "LOW", "LOW"]
}


def execution(command):
    in1 = command[0]
    in2 = command[1]
    in3 = command[2]
    in4 = command[3]



while True:
    if keyboard. in wasDict:
        command = wasDict[keyboard]

        execution(command)
    elif keyboard == ("h"):
        print("exit")
        break