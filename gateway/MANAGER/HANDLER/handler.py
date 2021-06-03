import json
import os
import peewee as pw
import socket
import sys
import time
import uuid
from datetime import datetime
from playhouse.shortcuts import model_to_dict
from termcolor import colored

from CONFIGURATION.config import confi
from DATABASE.models import *
from LOGS.logmanager import log
class database():
    def __init__(self):
        try:
            self.records = 0
            self.new_batch = 0
            self.reetry = 0
            self.LOG = log()
            self.config = confi()
            self.localdb = pw.SqliteDatabase(self.config.DATABASE_PATH)
            proxy.initialize(self.localdb)
            controldata.create_table(True)
            devicedata.create_table(True)
            self.devicedata = devicedata()
            self.controldata = controldata()
        except:
            e = sys.exc_info()[0]
            self.LOG.ERROR("FAILLED TO INIT DB" + str(os.path.basename(__file__)) + str(e))  # error logs
            print(colored("EXCEPTION IN INIT DB - " + str(e), "red"))
            pass

    def Save_In_DataBase(self, payload, nodeid, nodetype, sensortype):
        try:
            self.devicedata.id = uuid.uuid4()
            self.devicedata.nodeid = nodeid
            self.devicedata.gatewayid = self.config.GATEWAY_ID
            self.devicedata.orgid = self.config.ORG_ID
            self.devicedata.nodetype = nodetype
            self.devicedata.sensortype = sensortype
            self.devicedata.payload = json.dumps(payload)
            self.devicedata.datestamp = self.get_datetime()[0]
            self.devicedata.timestamp = self.get_datetime()[1]
            self.devicedata.appname = self.config.APP_NAME
            self.devicedata.msgtype = "NODES_DATA"
            self.devicedata.authtoken = self.config.AUTH_TOKEN
            self.devicedata.save(force_insert=True)
            return True
        except:
            e = sys.exc_info()[0]
            self.LOG.ERROR("FAILLED TO SAVE DEVICE DATA IN DATABASE ,DATABASE ERROR" + str(os.path.basename(__file__)) + str(
                e))  # error logs
            print(colored("EXCEPTION IN SAVE DEVICE DATA IN DATABSE CHECK DATABASE MODELS- " + str(e), "red"))
            return False

    def Save_CMD_In_DataBase(self, payload, nodeid, nodetype, sensortype, command_from):
        try:
            self.controldata.id = uuid.uuid4()
            self.controldata.nodeid = nodeid
            self.controldata.gatewayid = self.config.GATEWAY_ID
            self.controldata.orgid = self.config.ORG_ID
            self.controldata.nodetype = nodetype
            self.controldata.sensortype = sensortype
            self.controldata.payload = payload
            self.controldata.datestamp = self.get_datetime()[0]
            self.controldata.timestamp = self.get_datetime()[1]
            self.controldata.From = command_from
            self.controldata.appname = self.config.APP_NAME
            self.controldata.msgtype = "CLOUD_COMMANDS"
            self.controldata.authtoken = self.config.AUTH_TOKEN
            self.controldata.save(force_insert=True)
            return True
        except:
            e = sys.exc_info()[0]
            self.LOG.ERROR("FAILLED TO SAVE CMD DATA IN DATABASE ,DATABASE ERROR" + str(os.path.basename(__file__)) + str(
                e))  # error logs
            print(colored("EXCEPTION IN SAVE CMD DATA IN DATABSE CHECK DATABASE MODELS- " + str(e), "red"))
            return False

    def get_datetime(self):
        DateString = "%Y-%m-%d"
        TimeString = "%H:%M:%S"
        date = str(datetime.now().strftime(DateString))
        time = str(datetime.now().strftime(TimeString))
        return date, time

    def update_synced(self, msg_id):
        try:
            query = devicedata.update(synced=1).where((devicedata.id == msg_id))
            query.execute()

            return True
        except:
            e = sys.exc_info()[0]
            self.LOG.ERROR(
                "FAILLED TO UPDATE SYNCED DATA TO 0---1" + str(os.path.basename(__file__)) + str(e))  # error logs
            print(colored("EXCEPTION IN UPDATING SYNCED DATA- " + str(e), "red"))
            return False

    def Connect_to_cloud(self):
        if self.config.GENERIC_MQTT == "ENABLE":
            from MANAGER.CLOUD.MQTT_GEN.GENERIC_MQTT import Generic_Mqtt
            self.gen_mqtt = Generic_Mqtt()
            self.retry = 0
            return True
        if self.config.GENERIC_HTTP == "ENABLE":
            from MANAGER.CLOUD.HTTP_GEN.GENERIC_HTTP import Generic_Http
            self.gen_http = Generic_Http()
            self.retry = 0
            return True
        if self.config.GENERIC_AMQP == "ENABLE":
            from MANAGER.CLOUD.AMQP_GEN.GENERIC_AMQP import Generic_Amqp
            self.gen_amqp = Generic_Amqp()
            self.retry = 0
            return True
        if self.config.AWS_IOT == "ENABLE":
            from MANAGER.CLOUD.AWS.AWS_IOT import AWS_IOT
            self.aws_iot = AWS_IOT()
            self.retry = 0
            return True

    def send_data(self):
        if self.is_connected() == True:
            if self.retry == 1:
                print(colored("CONNECTIVITY FOUND, CONNECTING WITH SERVER WAIT ...- ", "red"))
                self.Connect_to_cloud()
            if self.retry == 0:
                self.records = self.check_data_base()
                # print(self.records)
                if self.records < 15:
                    self.new_batch = self.config.BATCH_SIZE
                if self.records > 15 and self.records < 50:
                    self.new_batch = 10
                if self.records > 50 and self.records < 200:
                    self.new_batch = 20
                if self.records > 200 and self.records < 500:
                    self.new_batch = 30
                if self.records > 500 and self.records < 1000:
                    self.new_batch = 50
                if self.records > 1000 and self.records < 5000:
                    self.new_batch = 200

                for data in devicedata().select().order_by(
                        devicedata.datestamp.desc() and devicedata.timestamp.asc()).where(devicedata.synced == 0).limit(
                    self.new_batch):
                    try:
                        if self.config.GENERIC_MQTT == "ENABLE":
                            confirmation_mqtt = self.gen_mqtt.MQTT_Send_Data(json.dumps(model_to_dict(data)))
                            if confirmation_mqtt:
                                msg_id = data.id
                                self.update_synced(msg_id)

                        if self.config.GENERIC_HTTP == "ENABLE":
                            confirmation_http = self.gen_http.HTTP_Send_data(json.dumps(model_to_dict(data)))
                            if confirmation_http:
                                msg_id = data.id
                                self.update_synced(msg_id)
                        if self.config.GENERIC_AMQP == "ENABLE":
                            confirmation_amqp = self.gen_amqp.AMQP_Send_data(json.dumps(model_to_dict(data)))
                            if confirmation_amqp:
                                msg_id = data.id
                                self.update_synced(msg_id)
                        if self.config.AWS_IOT == "ENABLE":
                            confirmation_aws = self.aws_iot.Aws_Iot_Send(json.dumps(model_to_dict(data)))
                            if confirmation_aws:
                                msg_id = data.id
                                self.update_synced(msg_id)

                    except:
                        e = sys.exc_info()[0]
                        self.LOG.ERROR(
                            "FAILLED TO SEND DATA TO THE SERVER" + str(os.path.basename(__file__)) + str(e))  # error logs
                        print(colored("EXCEPTION IN SENDING DATA TO  SERVER - " + str(e), "red"))
                        continue
            time.sleep(self.config.SYNC_TIME)
        if self.is_connected() == False:
            print(colored("DISSCONNECTED WITH SERVER, CLIENT RETRY IN FEW SEC", "red"))
            self.LOG.ERROR("DISSCONNECTED WITH SERVER, CLIENT RETRY IN FEW SEC" + str(os.path.basename(__file__)))
            time.sleep(self.config.RETRY_TIME)

    def is_connected(self):
        try:
            socket.create_connection((self.config.PING_SERVER, self.config.SERVER_PORT))
            return True
        except OSError:
            pass
            self.retry=1
            return False

    def check_data_base(self):
        records_list = []
        for data in devicedata().select().order_by(devicedata.datestamp.desc() and devicedata.timestamp.asc()).where(
                devicedata.synced == 0):
            records_list.append(data)
        return len(records_list)
