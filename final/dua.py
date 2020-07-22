"""
Python MQTT Subscription client
Thomas Varnish (https://github.com/tvarnish), (https://www.instructables.com/member/Tango172)
Written for my Instructable - "How to use MQTT with the Raspberry Pi and ESP8266"
"""
import paho.mqtt.client as mqtt
import psycopg2
from datetime import datetime
global str

# Don't forget to change the variables for the MQTT broker!
mqtt_username = "mqtt"
mqtt_password = "mqtt"
mqtt_topic = "smartpju/data3"
mqtt_status = "smartpju/led"
mqtt_broker_ip = "mqtt.danova.id"

client = mqtt.Client()
# Set the username and password for the MQTT client
client.username_pw_set(mqtt_username, mqtt_password)

# These functions handle what happens when the MQTT client connects
# to the broker, and what happens then the topic receives a message
def on_connect(client, userdata, flags, rc):
    # rc is the error code returned when connecting to the broker
    print ("Connected!", str(rc))
    
    # Once the client has connected to the broker, subscribe to the topic
    client.subscribe(mqtt_status)
       
def on_message(client, userdata, msg):
    data = msg.payload
    baru = data.decode()
   
    cur = conn.cursor()
    post = """INSERT INTO status ("status")VALUES(%s)"""
    
    cur.execute(post, baru)

    conn.commit()
    print ("Records created successfully")
    print(x)
    print ("Topic: ", msg.topic + "\nMessage: " + str(baru))
    conn.loop_forever()
    conn.close()

    

# Here, we are telling the client which functions are to be run
# on connecting, and on receiving a message
client.connect(mqtt_broker_ip, 1883)
print("connect mqqt")
conn = psycopg2.connect(database="smartpju_v1", user = "postgres", password = "D4n0v4@2020", host = "danova.id", port = "5432")
print ("Opened database successfully")
client.on_connect = on_connect
client.on_message = on_message


# Once everything has been set up, we can (finally) connect to the broker
# 1883 is the listener port that the MQTT broker is using


# Once we have told the client to connect, let the client object run itself
client.loop_forever()

client.disconnect()






