#------------------------------------------
#--- Author: Muhammad Sya'roni Mujahidin
#--- Date: 16 juni 2020
#--- Version: 1.0
#--- Python Ver: 3.6
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------

import paho.mqtt.client as mqtt
from store_Sensor_Data_to_DB import sensor_Data_Handler

# MQTT Settings 
MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
#Keep_Alive_Interval = 60
MQTT_Topic_Tegangan = "smartpju/tegangan"

#Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj, rc):
	mqtt.subscribe(MQTT_Topic_Tegangan, 0)

#Save Data into DB Table
def on_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	print ("MQTT Data Received...")
	print ("MQTT Topic: " + msg.topic)
	print ("Data: " + msg.payload)
	sensor_Data_Handler(msg.topic, msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port))

# Continue the network loop
mqttc.loop_forever()
