from peewee import *
proxy = Proxy()

class devicedata(Model):
    id = TextField(primary_key=True)
    nodeid = TextField()
    gatewayid = TextField()
    orgid = TextField()
    nodetype = TextField()
    sensortype = TextField()
    payload = TextField()
    datestamp = TextField()
    timestamp = TextField()
    timestamp = TextField()
    appname = TextField()
    msgtype = TextField()
    authtoken = TextField()
    synced = IntegerField(default=0)
    class Meta:
        database = proxy

class controldata(Model):
    id = TextField(primary_key=True)
    nodeid = TextField()
    gatewayid = TextField()
    orgid = TextField()
    From = TextField()
    nodetype = TextField()
    sensortype = TextField()
    payload = TextField()
    datestamp = TextField()
    timestamp = TextField()
    appname = TextField()
    msgtype = TextField()
    authtoken = TextField()
    synced = IntegerField(default=0)

    class Meta:
        database = proxy
