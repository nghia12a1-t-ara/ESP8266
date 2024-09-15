from machine import Pin, ADC
from time import sleep

adc_obj = ADC(0)

while True:
    value = adc_obj.read()
    print("ADC reading is: ", value)
    sleep(1)