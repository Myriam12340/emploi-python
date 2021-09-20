# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!



import sys
sys.path.append('../')

from PyQt5 import QtCore, QtGui, QtWidgets


import BD



class Ui_MainWindow(object):
    form=None
    def setupUi(self, MainWindow):
        Ui_MainWindow.form=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 561, 641))
        self.frame_2.setStyleSheet("QFrame\n"
" {\n"
"border-radius:5px;\n"
"background-color:linear-gradient(to right top, #3cc6da, #5bc7e4, #77c8ea, #90c8ee, #a6c9ee, #a5c1e7, #a4bae0, #a3b2d9, #8fa0cc, #7c8ebe, #697db1, #566ca4;)\n"
"}\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        font = QtGui.QFont()
        self.frame_2.setProperty("image", font)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(100, 80, 371, 461))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"background:rgba(0,0,0,0);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 231, 41))
        self.label_2.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font: 75 italic 12pt 'Book Antiqua';"
"font-size:40px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color: rgb(35, 91, 113);\n"
"}")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setObjectName("label_2")
        self.buttonlogin = QtWidgets.QPushButton(self.frame)
        self.buttonlogin.setGeometry(QtCore.QRect(150, 320, 41, 41))
        self.buttonlogin.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:15px;\n"
"background:rgba(200,50,0,0.5);\n"
"    background-color: rgb(0, 0, 0);\n"
"font-size:17px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:#56655e1;\n"
"\n"
"}\n"
"")
        self.buttonlogin.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/logiiin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonlogin.setIcon(icon)
     
        self.buttonlogin.setObjectName("buttonlogin")
        #login event
        self.buttonlogin.clicked.connect(self.login)
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(70, 180, 241, 37))
        self.username.setStyleSheet("QLineEdit\n"
"{\n"

"border:none;\n"
"background:rgba(200,50,0,0.5);\n"
" border-radius: 1;"
"background-color: rgb(255, 255, 243);"
"color:rgb(184, 179, 174);\n"
"border-bottom:5px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}")
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(70, 260, 251, 37))
        self.password.setStyleSheet("QLineEdit\n"
"{\n"

"border:none;\n"
"background:rgba(200,50,0,0.5);\n"
" border-radius: 4;"
"background-color: rgb(255, 255, 243);"
"color:rgb(184, 179, 174);\n"
"border-bottom:2px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
       
       
       
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(60, 290, 311, 31))
        self.label_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:15px;\n"
"}\n"
"QLabel\n"
"background:rgba(200,50,0,0.5);\n""{\n"
"background:transparent;\n"
"color:red;\n"
"font-size:15px;\n"
"}")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.buttoninscription = QtWidgets.QPushButton(self.frame)
        self.buttoninscription.setGeometry(QtCore.QRect(0, 400, 371, 41))
        self.buttoninscription.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(252, 252, 252);"
"color:rgb(83, 83, 83);\n"
"border-radius:15px;\n"
"\n"
"font-size:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:#56655e1;\n"
"\n"
"}\n"
"")
        self.buttoninscription.setObjectName("buttoninscription")
        #incrire event
        self.buttoninscription.clicked.connect(self.inscrire)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 561, 641))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/log2.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Bienvenue"))

        self.username.setPlaceholderText(_translate("MainWindow", "Login"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
  
    
        self.buttoninscription.setText(_translate("MainWindow", "Inscrivez-vous"))
        
    def login(self):  
       conn= BD.connect_user(self.username.text(),self.password.text())
       if conn==False :
           self.label_5.setText("verifiez votre login ou mot de passe")
       else :
          from main import Ui_MainWindowM
          self.window2=QtWidgets.QMainWindow()
         
          Ui_MainWindowM.user=conn
          self.ui= Ui_MainWindowM()
          self.ui.setupUi(self.window2)
          self.window2.show() 
          Ui_MainWindow.form.close()
            
    def inscrire(self):
          from inscription import Ui_MainWindowi
          self.window2=QtWidgets.QMainWindow()
          self.ui= Ui_MainWindowi()
          self.ui.setupUi(self.window2)
          self.window2.show() 
          Ui_MainWindow.form.close()
          

       
         


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

