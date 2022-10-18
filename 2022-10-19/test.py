import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 17
trig = 2
echo = 3

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

try:
	while True:
		GPIO.output(trig, False)
		time.sleep(0.1)
	
		GPIO.output(trig, True)
		time.sleep(0.1)
		GPIO.output(trig, False)

		while GPIO.input(echo) == 0:
			pulse_start = time.time()

		while GPIO.input(echo) == 1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17000
		distance = round(distance, 2)
		
		if distance < 10:
			GPIO.output(LED, GPIO.HIGH)
		else:
			GPIO.output(LED, GPIO.LOW)
		print("distance: ", distance, "cm")
except Keyboardinterrupt:
	GPIO.cleanup()
