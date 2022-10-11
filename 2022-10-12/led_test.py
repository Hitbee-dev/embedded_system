import lgpio
import time

LED = 17

h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED)

try:
	while True:
		print('LED On!')
		lgpio.gpio_write(h, LED, 1)
		time.sleep(1)

		print('LED Off!')
		lgpio.gpio_write(h, LED, 0)
		time.sleep(1)
except KeyboardInterrupt:
	lgpio.gpio_write(h, LED, 0)
	lgpio.gpiochip_close(h)
