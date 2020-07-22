import time
import paho.mqtt.client as mqtt

topic = "smartpju/siapa"

# Callback Function on Connection with MQTT Server
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    client.subscribe(topic)

# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    # print the message received from the subscribed topic
    print ( str(msg.payload) )



# mqttc = mqtt.Client()
# mqttc.on_connect = on_connect
# mqttc.on_disconnect = on_disconnect
# mqttc.on_publish = on_publish
# mqttc.connect(MQTT_Broker)	  



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.danova.id", 1883)
client.username_pw_set("mqtt", "mqtt")

def publish_To_Topic(topic, message):
    client.publish(topic,message)
    print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
    print("")

publish_To_Topic(topic, "Makanan")

# client.loop_forever()
client.loop_start()
time.sleep(1)


client.loop_stop()
client.disconnect()