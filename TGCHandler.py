import socket
import json
import threading
import time
import sys

class TGCHandler:
    'Class for dealing with the ThinkGear Connector Application'


    def __init__(self,host = '127.0.0.1',port = 13854):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = socket.socket()
        self.socket.setblocking(1)
        self.dic = {}

    def connect(self):
        try:
            print("Connecting...")
            self.socket.connect((self.host,self.port))
            self.connected = True
            print("Succesfully Connected")
        except:
            print("Unable to Connect" + str(sys.exc_info()[0]))

    def send(self,dic):
        try:
            st = json.dumps(dic)
            self.socket.sendall(st.encode())
            return True
        except:
            return False


    def recieve(self,pcktSize = 2048):
        if self.configured:
            try:
                st = self.socket.recv(pcktSize).decode()
                st = st.strip()
                star = st.split('\r')
                dics = []
                for s in star:
                    dic = json.loads(s)
                    dics.append(dic)
                return dics
            except:
                return
        else:
            raise NameError('NotConfigured')
    
    def get(self, key):
        if key in self.dic.keys():
            return self.dic[key]
        else:
            return


    def configure(self,flag = True):
        if self.connected:
            if flag:
                if self.send({"enableRawOutput":True,"format":"Json"}):
                    self.configured = True
                    self.rawEnabled = True
                    print("Succesfully Configured with Raw Output")
                else:
                    print("Configuration not successfull" + sys.exc_info()[0])
            else:
                if self.send({"enableRawOutput":False,"format":"Json"}):
                    self.configured = True
                    self.rawEnabled = False
                    print("Succesfully Configured without Raw Output")
                else:
                    print("Configuration not successfull" + sys.exc_info()[0])
        else:
            raise NameError('NotConnected') 
    def continuousMeasuring(self):
        while self.reading:
            dics = self.recieve()
            if dics != None:
                for dic in dics:
                    for k in dic.keys():
                        if k in ['eegPower','eSense']:
                            for k2 in dic[k].keys():
                                self.dic[k2] = dic[k][k2]
                        else:
                            self.dic[k] = dic[k]

    def startMeasuring(self):
        self.reading = True
        x = threading.Thread(target=self.continuousMeasuring)
        x.start()
        time.sleep(2)
        print("Measuring Started")

    def stopMeasuring(self):
        self.reading = False
        print("Measuring Stopped")

        