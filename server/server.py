import json
import paho.mqtt.client as mqttClient
import time
import csv
Connected = False   #global variable for the state of the connection
broker_address= "m16.cloudmqtt.com"  #Broker address
port = 13515                         #Broker port
user = "zlyqkxph"                    #Connection username
password = "AlHB2h-GaIVX"            #Connection password

#*** on_connect: to verify broker connection ***
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")
#*** publishMeasurements: Create device if device is not present and sends measurements ***
def on_message(client, userdata, message):
    #print ("Message received:"  + message.payload.decode("utf-8"))
    data_temp = json.loads(message.payload.decode("utf-8"))
    print(data_temp["payload"][15:17])
    print(data_temp["timestamp"])
    print(data_temp["nodetype"]) # this is a json object you will get all fields like that
    with open('data.csv', mode='a') as data_file:
        fieldnames=['DateTime', 'Value', 'Sensor']
        write = csv.DictWriter(data_file, fieldnames=fieldnames)
        write.writerow({'Value':str(message.payload.decode("utf-8"))})
client = mqttClient.Client("testing")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
client.loop_start()        #start the loop
while Connected != True:    #Wait for connection
    time.sleep(0.1)
client.subscribe("mytopic2k1")
while 1:
     time.sleep(1)


