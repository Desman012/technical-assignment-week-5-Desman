import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
gpio = 4

while True:
    humidity, temp = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temp is not None :
        print("Temperature: {}*C   Humidity: {}%".format(temp, humidity))

        #Logic tambahan :
        if temp > 30 :
            print("suhu terasa panas")
        elif temp <= 30 and temp >= 24 :
            print("suhu terasa sejuk")
        else :
            print("suhu terasa dingin")
            
    else :
        print("Gagal Membaca")
    time.sleep(2)