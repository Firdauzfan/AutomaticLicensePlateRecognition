import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
client=mqtt.Client()
client.connect("192.168.8.120", 1883, 60)
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

count=0
while True:
    if  GPIO.input(17):
        print(GPIO.input(17))
        pass
    else:
        continue
        if GPIO.input(17):
            count+=1
            if count>=30:
                client.publish("xiaomi/to/write",'{"cmd": "write",  "model": "plug",  "sid": "158d0002365abb",  "data": {"status": "off"}}', qos=0)

# #    time.sleep(0.2)
# val = [0,0]
# while True:
#     val[0] = GPIO.input(17)
#     if val[0] == 1:
#         if val[1] == val[0]:
#             pass
#         else:
#             client.publish("xiaomi/to/write",'{"cmd": "write",  "model": "plug",  "sid": "158d0002365abb",  "data": {"status": "off"}}', qos=0)
#     elif val[0] == 0:
#         if val[1] == val[0]:
#             pass
#         else:
#             client.publish("xiaomi/to/write",'{"cmd": "write",  "model": "plug",  "sid": "158d0002365abb",  "data": {"status": "on"}}', qos=0)
#     print(GPIO.input(17))
#     val[1]=val[0]
#     time.sleep(0.2)

#
# try:
#     print("When pressed, you'll see: Rising Edge detected on 25")
#     print("When released, you'll see: Falling Edge detected on 25")
#     time.sleep(30)         # wait 30 seconds
#     print("Time's up. Finished!")
#
# finally:                   # this block will run no matter how the try block exits
#     GPIO.cleanup()
