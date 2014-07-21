#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from TwitterAPI import TwitterAPI


TWEET_TEXT = "What do you Want to Tweet?"


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''


api = TwitterAPI(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET)
    
sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

while True:
	time.sleep(.1)
	prevState = currState
	currState = GPIO.input(sensorPin)
	if currState != prevState:
		print "GPIO pin {0} is {1}".format(sensorPin, "HIGH" if currState else "LOW")
		r = api.request('statuses/update', {'status': TWEET_TEXT})
		print('SUCCESS' if r.status_code == 200 else 'FAILURE')
