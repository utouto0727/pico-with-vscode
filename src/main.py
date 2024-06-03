import machine
import utime

led_pin = machine.Pin("LED", machine.Pin.OUT)

while True:
    led_pin.toggle()
    utime.sleep(1)