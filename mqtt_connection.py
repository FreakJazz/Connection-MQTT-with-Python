
# In this project the MQTT connection with 
# the HiveMQ server will be visualized'''

import ssl                          # Establish secure connection
import sys
import paho.mqtt.client as mqtt    # Connect with the MQTT Library
import time                         # Time Library

# Config MQTT
host = "broker.mqttdashboard.com"        #'broker.mqttdashboard.com';
port = 1883
keepalive = 60
clientid = "Clientjazz23"
username = "jazz23"                     # Give your own username
password = "12345"                      # Give your own password
topic = "dom/#"

####### FUNCTION ON CONNECT ######
def on_connect(client, userdata, flags, rc):
    print('Connected(%s)',client._client_id)
    client.subscribe(topic, qos=0) 
    client.publish(topic,'Connected')

####### FUNCTION ON MESSAGE ######
def on_message(client, userdata, message):
    print('----------------------')
    print('topic: %s',  message.topic)
    print('payload: %s', message.payload)
    print('qos: %d', message.qos)
    print(message.payload.decode("utf-8"))

##### FUNCTION PRINCIPAL #####
client = mqtt.Client()     # Client Identifier
client.on_connect = on_connect      # Conecction Function 
client.on_message = on_message      # Message Function
client.connect(host, port, keepalive)     # Host, terminal, keep alive
client.username_pw_set(username,password)    # Username and Password
#client.loop_forever()

if __name__ == "__main__":
    topic = str(input("Topic:   "))     # Input the topic in ""
    estado = str(input("Data:   "))     # Input the data in ""
    print(topic)
    print(estado)
    client.subscribe(topic, qos=0) 
    client.publish(topic, estado)
    client.loop()
