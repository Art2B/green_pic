from gpiozero import PWMLED
from time import sleep

red = PWMLED(17)
green = PWMLED(22)
blue = PWMLED(27)

INIT_ON_TIME = 0.4
INIT_OFF_TIME = 0.2
INIT_NB_BLINK = 5

COUNTDOWN_ON_TIME = 0.8
COUNTDOWN_OFF_TIME = 0.2
COUNTDOWN_SLEEP_TIME = 1.4

def reset():
    red.value = 1
    green.value = 1
    blue.value = 1
    red.off()
    green.off()
    blue.off()

def blink_init(led):
    led.blink(INIT_ON_TIME, INIT_OFF_TIME, 0, 0, INIT_NB_BLINK)

def blink_countdown(led):
    led.blink(COUNTDOWN_ON_TIME, COUNTDOWN_OFF_TIME, 0, 0, 1)

def countdown():
    # Red
    blink_countdown(red)
    sleep(COUNTDOWN_SLEEP_TIME)
    # Orange
    red.value = 0.9
    green.value = 0.5
    blink_countdown(red)
    blink_countdown(green)
    # Green
    sleep(COUNTDOWN_SLEEP_TIME)
    green.value = 1
    blink_countdown(green)

def display_error():
    reset()
    red.on()

def display_init():
    reset()
    blink_init(blue)
    sleep(4)
    blink_init(green)
    sleep(4)
    blink_init(red)
