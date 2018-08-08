
import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 17)  # GPIO27 (BCM notation)
    print("Humidity = {} %; Temperature = {} C".format(humidity, temperature))