import configparser
import os

from LOGS.logmanager import log

config = configparser.ConfigParser()
config.read('/Users/yatinbaluja/Desktop/gateway/CONFIGURATION/config.ini')
#config.read('CONFIGURATION\\config.ini')
class confi:
    def __init__(self):
        self.LOG = log()
        self.MQTT_URL = str(config['GENERIC_MQTT']['MQTT_URL'])
        self.MQTT_PORT = int(config['GENERIC_MQTT']['MQTT_PORT'])
        self.MQTT_USR = str(config['GENERIC_MQTT']['MQTT_USR'])
        self.MQTT_PASS = str(config['GENERIC_MQTT']['MQTT_PASS'])
        self.MQTT_QOS = int(config['GENERIC_MQTT']['MQTT_QOS'])
        self.TOPIC_SEND = str(config['GENERIC_MQTT']['TOPIC_SEND'])
        self.TOPIC_RECV = str(config['GENERIC_MQTT']['TOPIC_RECV'])
        # -------------------------DATASET CONFIGURATION------------------------------------------------
        self.DATABASE_PATH= str(config['DATABASE']['DATABASE_PATH'])
        self.SYNC_TIME = int(config['DATABASE']['SYNC_TIME'])
        self.BATCH_SIZE = int(config['DATABASE']['BATCH_SIZE'])


        #--------------------------GATEWAY CONFIGURATION--------------------------------------------------
        self.GATEWAY_ID = str(config['DEVICE']['GATEWAY_ID'])
        self.ORG_ID = str(config['DEVICE']['ORG_ID'])
        self.APP_NAME = str(config['DEVICE']['APP_NAME'])
        self.RETRY_TIME = int(config['DEVICE']['RETRY_TIME'])
        #self.MSG_TYPE = str(config['DEVICE']['MSG_TYPE'])
        self.CONNECTION_TYPE = str(config['DEVICE']['CONNECTION_TYPE'])
        self.PING_SERVER = str(config['DEVICE']['PING_SERVER'])
        self.SERVER_PORT = int(config['DEVICE']['SERVER_PORT'])
        self.DEBUG_MODE = str(config['DEVICE']['AUTH_TOKEN'])
        self.AUTH_TOKEN = str(config['DEVICE']['AUTH_TOKEN'])

        self.LOG.DEBUG("Config file loaded : " + str(os.path.basename(__file__)))
        # --------------------------TOPOLOGY CONFIGURATION--------------------------------------------------
        self.AWS_IOT = str(config['TOPOLOGY']['AWS_IOT'])
        self.IBM_WATSON_IOT = str(config['TOPOLOGY']['IBM_WATSON_IOT'])
        self.AZURE_IOT_HUB = str(config['TOPOLOGY']['AZURE_IOT_HUB'])
        self.GOOGLE_IOT = str(config['TOPOLOGY']['GOOGLE_IOT'])
        self.GENERIC_MQTT = str(config['TOPOLOGY']['GENERIC_MQTT'])
        self.GENERIC_HTTP = str(config['TOPOLOGY']['GENERIC_HTTP'])
        self.GENERIC_AMQP = str(config['TOPOLOGY']['GENERIC_AMQP'])
        # --------------------------GENERIC_HTTP CONFIGURATION--------------------------------------------------
        self.HTTP_URL = str(config['GENERIC_HTTP']['HTTP_URL'])
        self.HTTP_PORT = int(config['GENERIC_HTTP']['HTTP_PORT'])
        self.HTTP_RESPONSE = str(config['GENERIC_HTTP']['HTTP_RESPONSE'])
        self.HTTP_PASSWORD = str(config['GENERIC_HTTP']['HTTP_PASSWORD'])
        self.HTTP_API_KEY = str(config['GENERIC_HTTP']['HTTP_API_KEY'])
        self.HTTP_USERNAME = str(config['GENERIC_HTTP']['HTTP_USERNAME'])

        # --------------------------GENERIC_AMQP CONFIGURATION--------------------------------------------------
        self.AMQP_URL = str(config['GENERIC_AMQP']['AMQP_URL'])
        self.AMQP_PORT = int(config['GENERIC_AMQP']['AMQP_PORT'])
        self.AMQP_EXCHANGE = str(config['GENERIC_AMQP']['AMQP_EXCHANGE'])
        self.AMQP_ROUTING_KEY = str(config['GENERIC_AMQP']['AMQP_ROUTING_KEY'])
        self.AMQP_QUEUE = str(config['GENERIC_AMQP']['AMQP_QUEUE'])
        self.AMQP_USERNAME = str(config['GENERIC_AMQP']['AMQP_USERNAME'])
        self.AMQP_PASSWORD = str(config['GENERIC_AMQP']['AMQP_PASSWORD'])

        # --------------------------AWS_IOT CONFIGURATION--------------------------------------------------
        self.AWS_IOT_ARN = str(config['AWS_IOT']['AWS_IOT_ARN'])
        self.AWS_IOT_PORT = int(config['AWS_IOT']['AWS_IOT_PORT'])
        self.AWS_IOT_SEND_TOPIC = str(config['AWS_IOT']['AWS_IOT_SEND_TOPIC'])
        self.AWS_IOT_RECV_TOPIC = str(config['AWS_IOT']['AWS_IOT_RECV_TOPIC'])
        self.AWS_IOT_QOS = str(config['AWS_IOT']['AWS_IOT_QOS'])
        self.CERTIFICATES_PATH = str(config['AWS_IOT']['CERTIFICATES_PATH'])
        # --------------------------IBM_WATSON_IOT CONFIGURATION--------------------------------------------------
        self.IBM_ORGNIZATION = str(config['IBM_WATSON_IOT']['IBM_ORGNIZATION'])
        self.IBM_TYPE = str(config['IBM_WATSON_IOT']['IBM_TYPE'])
        self.IBM_ID = str(config['IBM_WATSON_IOT']['IBM_ID'])
        self.IBM_AUTH_TOKEN = str(config['IBM_WATSON_IOT']['IBM_AUTH_TOKEN'])
        self.IBM_CLEAN_SESSION = str(config['IBM_WATSON_IOT']['IBM_CLEAN_SESSION'])
        self.IBM_QOS = str(config['IBM_WATSON_IOT']['IBM_QOS'])
        self.IBM_AUTH_METHOD = str(config['IBM_WATSON_IOT']['IBM_AUTH_METHOD'])
        self.IBM_SEND_TOPIC = str(config['IBM_WATSON_IOT']['IBM_SEND_TOPIC'])
        self.IBM_RECV_TOPIC = str(config['IBM_WATSON_IOT']['IBM_RECV_TOPIC'])
        #-----------------------------LORA HARDWARE CONFIG --------------------------------------------------------
        self.LORA_PORT = str(config['LORA']['LORA_PORT'])
        self.LORA_TIMEOUT = int(config['LORA']['LORA_TIMEOUT'])
        self.LORA_PORT_BAUDRATE = int(config['LORA']['LORA_PORT_BAUDRATE'])
        self.LORA_DATA_FETCH_TIME = int(config['LORA']['LORA_DATA_FETCH_TIME'])
        self.LORA_PACK_LIM = int(config['LORA']['LORA_PACK_LIM'])
        self.LORA_DECODE = str(config['LORA']['LORA_DECODE'])
        #----------------------------GPIO HARDWARE CONFIG --------------------------------------------------------
