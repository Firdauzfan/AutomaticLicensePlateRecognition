import paho.mqtt.client as mqttClient
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

def on_message(client, userdata, message):
    print ("Message received: " ,str(message.payload.decode("utf-8")))
    gpioVal=int(message.payload.decode("utf-8"))
    print("THE GPIO VAL IS ", gpioVal)
    GPIO.output(26, gpioVal)

Connected = False   #global variable for the state of the connection

broker_address= "192.168.1.151"  #Broker address
port = 1883                         #Broker port

client = mqttClient.Client("ALPR")               #create new instance
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback

client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("alpr/mqtt",qos=0)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()
