import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
gpio = 4

while True:
    humidity, temp = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temp is not None :
        print("Temperature: {}*C   Humidity: {}%".format(temp, humidity))
    else :
        print("Gagal Membaca")
    time.sleep(2)