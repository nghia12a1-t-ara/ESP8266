from machine import Pin
from time import sleep
import dht

dht_obj =dht.DHT11(Pin(12))

while True:
    try:
        dht_obj.measure()
        temp = dht_obj.temperature()
        humi = dht_obj.humidity()
        print("Temperature = ", temp)
        print("Humidity = ", humi)
        sleep(1)
    except OSError as e:
        print("Fail to read dht11 data")
        