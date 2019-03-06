# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_principal.ui'
#
# Created: Wed Apr  4 13:12:57 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!



from PyQt4 import QtCore, QtGui

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



class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(674, 445)
     
        self.btn_on_rele_1 = QtGui.QPushButton(MainWindow)
        self.btn_on_rele_1.setGeometry(QtCore.QRect(20, 20, 300, 100))
        self.btn_on_rele_1.setAutoRepeatDelay(300)
        self.btn_on_rele_1.setObjectName(_fromUtf8("btn_on_rele_1"))
        
        self.btn_on_rele_2 = QtGui.QPushButton(MainWindow)
        self.btn_on_rele_2.setGeometry(QtCore.QRect(20, 120, 300, 100))
        self.btn_on_rele_2.setAutoRepeatDelay(300)
        self.btn_on_rele_2.setObjectName(_fromUtf8("btn_on_rele_2"))
        
        self.btn_on_rele_3 = QtGui.QPushButton(MainWindow)
        self.btn_on_rele_3.setGeometry(QtCore.QRect(20, 220, 300, 100))
        self.btn_on_rele_3.setAutoRepeatDelay(300)
        self.btn_on_rele_3.setObjectName(_fromUtf8("btn_on_rele_3"))
        
        self.btn_on_rele_4 = QtGui.QPushButton(MainWindow)
        self.btn_on_rele_4.setGeometry(QtCore.QRect(20, 320, 300, 100))
        self.btn_on_rele_4.setAutoRepeatDelay(300)
        self.btn_on_rele_4.setObjectName(_fromUtf8("btn_on_rele_4"))
        
        self.btn_off_rele_1 = QtGui.QPushButton(MainWindow)
        self.btn_off_rele_1.setGeometry(QtCore.QRect(350, 20, 300, 100))
        self.btn_off_rele_1.setObjectName(_fromUtf8("btn_off_rele_1"))
        
        self.btn_off_rele_2 = QtGui.QPushButton(MainWindow)
        self.btn_off_rele_2.setGeometry(QtCore.QRect(350, 120, 300, 100))
        self.btn_off_rele_2.setObjectName(_fromUtf8("btn_off_rele_2"))
        
        self.btn_off_rele_3 = QtGui.QPushButton(MainWindow)
        self.btn_off_rele_3.setGeometry(QtCore.QRect(350, 220, 300, 100))
        self.btn_off_rele_3.setObjectName(_fromUtf8("btn_off_rele_3"))
        
        self.btn_off_rele_4 = QtGui.QPushButton(MainWindow)
        self.btn_off_rele_4.setGeometry(QtCore.QRect(350, 320, 300, 100))
        self.btn_off_rele_4.setObjectName(_fromUtf8("btn_off_rele_4"))
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "Controle de Reles", None))

        self.btn_on_rele_1.setText(_translate("MainWindow", "Rele 1 - ON", None))
        self.btn_on_rele_2.setText(_translate("MainWindow", "Rele 2 - ON ", None))
        self.btn_on_rele_3.setText(_translate("MainWindow", "Rele 3 - ON", None))
        self.btn_on_rele_4.setText(_translate("MainWindow", "Rele 4 - ON", None))

        self.btn_off_rele_1.setText(_translate("MainWindow", "Rele 1 - OFF", None))
        self.btn_off_rele_2.setText(_translate("MainWindow", "Rele 2 - OFF", None))
        self.btn_off_rele_3.setText(_translate("MainWindow", "Rele 3 - OFF", None))
        self.btn_off_rele_4.setText(_translate("MainWindow", "Rele 4 - OFF", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

