# Assignment
# Do Check different folders 
* Gateway folder is to send the data to cloud after generating random values for the temperature and humidity along with node-id, organisation-id, sensor-name, sensor-type. Also, generating unique id's inside the payload with timestamp and datestamp.
* Server folder is reading the payload from the MQTT via subscribing to the topic and creating .csv file with the payload.
