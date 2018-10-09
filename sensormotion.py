import RPi.GPIO as GPIO
import paho.mqtt.client as paho
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)

#val = GPIO.input(17)
#client.publish("xiaomi/to/write",'{"cmd": "write",  "model": "plug",  "sid": "158d0002365abb",  "data": {"status": "off"}}', qos=0)
# def my_callback(channel):
#     if GPIO.input(17):     # if port 25 == 1
#         print("Rising edge detected on 17 __________")
#     else:                  # if port 25 != 1
#         print("Falling edge detected on 17 __________")
#         #client.publish("xiaomi/to/write",'{"cmd": "write",  "model": "plug",  "sid": "158d0002365abb",  "data": {"status": "off"}}', qos=0)
# GPIO.add_event_detect(17, GPIO.BOTH, callback=my_callback)
# while True:
#    #print(val)

#    time.sleep(0.2)
val = [0,0]
while True:
    val[0] = GPIO.input(18)
    if val[0] == 1:
        if val[1] == val[0]:
            pass
        else:
            broker="192.168.1.151"
            port=1883
            client1= paho.Client("control2")                           #create client object
            client1.connect(broker,port)                                 #establish connection
            client1.publish("alpr/mqtt","1")

    elif val[0] == 0:
        if val[1] == val[0]:
            pass
        else:
            # client.publish("xiaomi/to/write",'{"cmd": "write",  "model": "plug",  "sid": "158d0002365abb",  "data": {"status": "on"}}', qos=0)
            pass
    print(GPIO.input(18))
    val[1]=val[0]
    time.sleep(0.2)

#
# try:
#     print("When pressed, you'll see: Rising Edge detected on 25")
#     print("When released, you'll see: Falling Edge detected on 25")
#     time.sleep(30)         # wait 30 seconds
#     print("Time's up. Finished!")
#
# finally:                   # this block will run no matter how the try block exits
#     GPIO.cleanup()
