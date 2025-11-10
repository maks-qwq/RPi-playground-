import RPi.GPIO as GPIO
import time

# Use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

# Set GPIO pin 17 as output
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)
i = 0 
try:
    while True:
        for i in range(10):
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
            time.sleep(1)                     # Wait for 1 second
            GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off
            time.sleep(1)                     # Wait for 1 second
        ans = input("Czy dalej?: \nzakończyc: no")
        if ans == "no":
            break
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  # Reset GPIO settings