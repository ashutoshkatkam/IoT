# Import Sensor Module

import Adafruit_DHT

 

try:

            while True:

                        # Read sensor data

                        humidity, temperature = Adafruit_DHT.read_retry(11,3)  # GPIO3 (BCM notation)

                        # Print the sensorn data

                        print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature))

 

except KeyboardInterrupt:

            print ("Aborted by user")