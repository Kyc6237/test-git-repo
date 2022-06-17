import paho.mqtt.client as mqtt  
import RPi.GPIO as GPIO


def on_connect(client, userdata, flag, rc):
   print("Connect rc:" + str(rc))
   client.subscribe("dragon")


def on_message(client, userdata, msg):
   if 1 in msg.payload:      
      print("led On")
      GPIO.output(22, True)   
   else :
      print("led Off")        
      GPIO.output(22, False) 


client = mqtt.Client()  
client.on_connect = on_connect   
client.on_message = on_message
client.connect("localhost", 1883, 60)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

client.loop_forever()
