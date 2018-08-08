#coding=utf-8

import boto
import boto.s3
import sys
from boto.s3.key import Key
import time
import subprocess

import Adafruit_DHT
import time

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor = Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio = 17

# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
writeToFile = open('tempdata.txt', 'w')
# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.


if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    writeToFile.write(str(temperature))
else:
    print('Failed to get reading. Try again!')

writeToFile.close()


AWS_ACCESS_KEY_ID = 'AKIAIFLJD5E62EX35NRA'
#skriv in din access key inom ''

AWS_SECRET_ACCESS_KEY = '5rNYRMXfs2M9m6TmfAD9nsIkNDwfCRyJkj2GhhQB'
#skriv in din secret access key inom ''

bucket_name = 'fromrasp'
#din bucket i S3 (döp till vad du vill)
print("innan connection")
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
#nu connectar vi
#loc = boto.s3.connect_to_region('us-east-2')
print("innan bucket conn")
bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)
#skapar bucketen i S3, funkar när den är skapad också
print("Innan temp")
file = "tempdata.txt"
#här väljer vi fil vi ska skicka, bilden som togs i början av programmet
print("Innan print")
#print 'Uploading %s to Amazon S3 bucket %s' % \
#   (file, bucket_name)
#utskrift i terminalen

print("funktion för utskrift")
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()
#funktion för utskrift
print("innan key")
k = Key(bucket)
#k blir ett objekt i din bucket
print("innan k.key")
k.key = "tempdata.txt"
#som far en key som är din bild, keyn blir filnamnet i din S3-bucket
print("innan k.set")
k.set_contents_from_filename(file,
    cb=percent_cb, num_cb=10)
#har laddas filen till S3,
#cb-variablerna är bara skit för den dar funktionen för utskriften i terminalen,
#det som gor att punkterna laddas i funktionen
