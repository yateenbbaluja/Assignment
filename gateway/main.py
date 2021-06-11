import multiprocessing
from termcolor import colored
from HARDWARE.lora import *
from MANAGER.HANDLER.handler import database

Data_base = database()

def get_data_lora(nodetype = "Sensor1"):
    #lora = LORA()
    while True:
        #data =lora.get_data()
        data = get_data()
        if data == None:
            pass
        else:
            #print(data)
            # print(DATA["DATA"])
            # print(DATA["NODE_ID"])
            # print(DATA["NODE_TYPE"])
            # print(DATA["SENSOR_TYPE"])
            if Data_base.Save_In_DataBase(
                data["data"], data["id"],nodetype, data["ST"]):
                print(colored("DATA SAVED IN OFFLINE DB :"+str(data),"blue"))
            else:
                print(colored("DATA CANT SAVED IN OFFLINE DB :", "red"))
        time.sleep(1)
def send_to_cloud():
    Data_base.Connect_to_cloud()
    while True:
        Data_base.send_data()


#get_data_lora()
#send_to_cloud()
#
if __name__ == '__main__':
    # if sys.platform.startswith('win'):
    #multiprocessing.freeze_support()
    thread1 = multiprocessing.Process(target=send_to_cloud)
    thread2 = multiprocessing.Process(target=get_data_lora)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

