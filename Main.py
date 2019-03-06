# -*- coding: utf-8 -*-
# https://pythonspot.com/qt4-messagebox/

import sys
import time

import threading
import paho.mqtt.client as mqttClient

valor = 123

#******************************************************************************************************
#******************************************************************************************************
#******************************************************************************************************

def on_connect(client, userdata, flags, rc):
     if rc == 0:
        print("Connected to broker")
        global Connected                 
        Connected = True                 
 
     else:
         print("Connection failed", rc)

def on_message(client, userdata, message):
    global valor
    valor = message.payload
    print("Recebeu: " + valor)
 


    
Connected = False    

#broker = "test.mosquitto.org"
#broker = "iot.eclipse.org"
broker  = "broker.hivemq.com"

client = mqttClient.Client("controle_reles_1")               
client.on_connect = on_connect                       
client.on_message = on_message                       
client.connect(broker)          
client.loop_start()        
 
while Connected != True:     
    time.sleep(0.1)
 
client.subscribe("MQTT/RASPBERRY", 2)

#******************************************************************************************************
#******************************************************************************************************
#******************************************************************************************************


from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QApplication


#********************************************************************************************************
#******************************************************************************************************

from tela_principal import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig) 
    
#********************************************************************************************************
#******************************************************************************************************

class MainWindow(QtGui.QDialog):
    
    def __init__(self, parent = None):

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()  # <<<<<<<<<<<<<
        self.ui.setupUi(self)

        self.label = QtGui.QLabel(self)
        self.label.resize(120, 15)
        self.label.move(10,425)
        self.label.setText('---')

        QtCore.QObject.connect(self.ui.btn_on_rele_1, QtCore.SIGNAL("clicked()"), self.liga_rele_1)
        QtCore.QObject.connect(self.ui.btn_on_rele_2, QtCore.SIGNAL("clicked()"), self.liga_rele_2)
        QtCore.QObject.connect(self.ui.btn_on_rele_3, QtCore.SIGNAL("clicked()"), self.liga_rele_3)
        QtCore.QObject.connect(self.ui.btn_on_rele_4, QtCore.SIGNAL("clicked()"), self.liga_rele_4)


        QtCore.QObject.connect(self.ui.btn_off_rele_1, QtCore.SIGNAL("clicked()"), self.desliga_rele_1)
        QtCore.QObject.connect(self.ui.btn_off_rele_2, QtCore.SIGNAL("clicked()"), self.desliga_rele_2)
        QtCore.QObject.connect(self.ui.btn_off_rele_3, QtCore.SIGNAL("clicked()"), self.desliga_rele_3)
        QtCore.QObject.connect(self.ui.btn_off_rele_4, QtCore.SIGNAL("clicked()"), self.desliga_rele_4)


    #----------------------
    # ROTINA LIGAR RELES
    #----------------------
    def liga_rele_1(self):
         global valor
         print("ligando rele_1")
         client.publish("MQTT/RASPBERRY", "R1_ON")
         self.label.setText(valor)
         time.sleep(1)

    def liga_rele_2(self):
         print("ligando rele_2")
         client.publish("MQTT/RASPBERRY", "R2_ON")
         time.sleep(1)

    def liga_rele_3(self):
         print("ligando rele_3")
         client.publish("MQTT/RASPBERRY", "R3_ON")
         time.sleep(1)

    def liga_rele_4(self):
         print("ligando rele_4")
         client.publish("MQTT/RASPBERRY", "R4_ON")
         time.sleep(1)
            
    #----------------------
    # ROTINA DESLIGAR RELES
    #----------------------
    def desliga_rele_1(self):
         print("desligando rele_1")
         client.publish("MQTT/RASPBERRY", "R1_OFF")
         time.sleep(1)

    def desliga_rele_2(self):
         print("desligando rele_2")
         client.publish("MQTT/RASPBERRY", "R2_OFF")
         time.sleep(1)

    def desliga_rele_3(self):
         print("desligando rele_3")
         client.publish("MQTT/RASPBERRY", "R3_OFF")
         time.sleep(1)

    def desliga_rele_4(self):
         print("desligando rele_4")
         client.publish("MQTT/RASPBERRY", "R4_OFF")
         time.sleep(1)

         

#******************************************************************************************************
#******************************************************************************************************
     
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

#******************************************************************************************************
#******************************************************************************************************
