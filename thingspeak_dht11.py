import thingspeak

import time

import Adafruit_DHT

 

channel_id = 337694 # PUT CHANNEL ID HERE

write_key  = '1U7S57YRHU7ZMJ2H' # PUT YOUR WRITE KEY HERE

#read_key   = 'IE2OR54QVDSC653P' # PUT YOUR READ KEY HERE

pin = 3

#sensor = Adafruit_DHT.DHT11

 

def measure(channel):

    try:

        humidity, temperature = Adafruit_DHT.read_retry(11, 3)

        # write

        response = channel.update({'field1': temperature, 'field2': humidity})

       

        # read

        #read = channel.get({})

        print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature))


       

    except:

        print("connection failed")

 

 

if __name__ == "__main__":

    channel = thingspeak.Channel(id=channel_id, api_key=write_key)

    while True:

        measure(channel)

        # free account has an api limit of 15sec

        time.sleep(15)

 

##https://tutorials-raspberrypi.com/log-raspberry-pi-sensor-data-with-thingspeak-and-analyze-it/