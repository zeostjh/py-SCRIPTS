from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin=16, echo_pin=0)

distance = sensor.distance_cm()

print('Distance:', distance, 'cm')



//

distance = sensor.distance_mm()

print('Distance:', distance, 'mm')

//
