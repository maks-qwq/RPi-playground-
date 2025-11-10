
import RPi.GPIO as GPIO
import time

# Define GPIO pins
CLK = 17
DT = 27
counter = 0
last_state = None

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Read initial state
last_state = GPIO.input(CLK)

try:
    while True:
        current_state = GPIO.input(CLK)
        if current_state != last_state:
            if GPIO.input(DT) != current_state:
                counter += 1
                direction = "Clockwise"
            else:
                counter -= 1
                direction = "Counterclockwise"
            print(f"Position: {counter}, Direction: {direction}")
        last_state = current_state
        time.sleep(0.01)  # Debounce delay
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()


# Define button pin
SW = 22
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_pressed(channel):
    print("Button Pressed!")

# Add event detection for button press
GPIO.add_event_detect(SW, GPIO.FALLING, callback=button_pressed, bouncetime=300)
