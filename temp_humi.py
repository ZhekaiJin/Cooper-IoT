import Adafruit_DHT as dht
import time


time.sleep(2)
h,t = dht.read_retry(dht.DHT22,4)

# convert temperature to Fahrenheit
t = t*9/5.0 + 32
print 'Temp={0:0.1f}F Humidity={1:0.1f}%'.format(t,h)




