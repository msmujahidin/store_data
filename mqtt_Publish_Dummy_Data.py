

import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime
from time import time
from random import random

#====================================================
# MQTT Settings 
#mqtt_username = ""
#mqtt_password = ""
MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
#Keep_Alive_Interval = 5
MQTT_Topic_Tegangan = "topic/baru"
MQTT_Topic_Arus = "PLN3"


def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print ("Unable to connect to MQTT Broker...")
	else:
		print ("Connected with MQTT Broker: " + str(MQTT_Broker))

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass
		
mqttc = mqtt.Client()
#mqttc.username_pw_set(mqtt_username, mqtt_password)
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port))	
	

		
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print ("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print ("")


#====================================================
# FAKE SENSOR 
# Dummy code used as Fake Sensor to publish some random values
# to MQTT Broker

toggle = 0

def publish_Fake_Sensor_Values_to_MQTT():
	threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()
	global toggle
	if toggle == 0:
		#Kemiringan_fake_value = float("{0:.2f}".format(random.uniform(50, 100)))
		kemiringan_fake_value = random()
		#Kemiringan = {}
		#Kemiringan['Sensor_ID'] = "Dummy-1"
		#Kemiringan['humadity'] = kemiringan_fake_value
		#Kemiringan['kemiringan_y'] = Kemiringan_fake_value
		#Kemiringan['kemiringan_z'] = Kemiringan_fake_value
		#Kemiringan['waktu_kirim'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		#kemiringan_json_data = json.dumps(Kemiringan)

		print("Publishing fake kemiringan Value: " +str(kemiringan_fake_value)+ "...")
			# print(kemiringan_fake_value)

		publish_To_Topic (MQTT_Topic_Tegangan, kemiringan_fake_value)
		toggle = 1

	else:
		#temperature_Fake_Value = float("{0:.2f}".format(random.uniform(1, 30)))
		Temperature_Fake_Value = [time() * 1000, random() * 100]

		Temperature_Data = {}
		Temperature_Data['Sensor_ID'] = "Dummy-2"
		Temperature_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		Temperature_Data['Temperature'] = Temperature_Fake_Value
		temperature_json_data = json.dumps(Temperature_Data)

		print ("Publishing fake Temperature Value: " + str(Temperature_Fake_Value) + "...")
		publish_To_Topic (MQTT_Topic_Arus, temperature_json_data)
		toggle = 0


publish_Fake_Sensor_Values_to_MQTT()

#====================================================
