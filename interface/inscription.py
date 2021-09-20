# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inscription.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('../')

import BD
class Ui_MainWindowi(object):
    form=None
    def setupUi(self, MainWindow):
        Ui_MainWindowi.form=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-170, -160, 1191, 881))
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
        self.frame.setGeometry(QtCore.QRect(260, 180, 891, 681))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"\n"
"    \n"
"border-radius:25px;\n"
"\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(310, 30, 261, 41))
        self.label_16.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:40px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"    color: rgb(212, 223, 230);\n"
"}")
        self.label_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_16.setObjectName("label_16")
        self.buttonlogin_3 = QtWidgets.QPushButton(self.frame)
        self.buttonlogin_3.setGeometry(QtCore.QRect(150, 570, 141, 41))
        self.buttonlogin_3.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:15px;\n"
"background-color: rgb(163, 201, 199);font-size:17px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"\n"
"border-radius:15px;\n"
"background:#56655e1;\n"
"\n"
"}\n"
"")
        self.buttonlogin_3.setObjectName("buttonlogin_3")
		#event incription
        self.buttonlogin_3.clicked.connect(self.inscription)
        self.username_11 = QtWidgets.QLineEdit(self.frame)
        self.username_11.setGeometry(QtCore.QRect(80, 130, 241, 22))
        self.username_11.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.username_11.setText("")
        self.username_11.setObjectName("username_11")
        self.password_3 = QtWidgets.QLineEdit(self.frame)
        self.password_3.setGeometry(QtCore.QRect(550, 130, 241, 22))
        self.password_3.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.password_3.setText("")
      
        self.password_3.setObjectName("password_3")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(20, 120, 71, 41))
        self.label_17.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_17.setLineWidth(-1)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(440, 120, 81, 31))
        self.label_18.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(30, 290, 311, 31))
        self.label_19.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:12px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:red;\n"
"font-size:14px;\n"
"}")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.buttoninscription_2 = QtWidgets.QPushButton(self.frame)
        self.buttoninscription_2.setGeometry(QtCore.QRect(230, 630, 371, 41))
        self.buttoninscription_2.setStyleSheet("QPushButton\n"
"{\n"
"color:rgb(185, 226, 219);\n"
"border-radius:15px;\n"
"\n"
"font-size:15px;\n"
"}")
        self.buttoninscription_2.setObjectName("buttoninscription_2")
		#connect event 
        self.buttoninscription_2.clicked.connect(self.connecter)
        self.buttonlogin_4 = QtWidgets.QPushButton(self.frame)
        self.buttonlogin_4.setGeometry(QtCore.QRect(480, 570, 141, 41))
        self.buttonlogin_4.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:15px;\n"
"background-color: rgb(163, 201, 199);\n"
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
        self.buttonlogin_4.setObjectName("buttonlogin_4")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(20, 180, 61, 31))
        self.label_20.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        #annuler event 
        self.buttonlogin_4.clicked.connect(self.annuler)
        self.label_20.setLineWidth(-1)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(10, 320, 51, 31))
        self.label_21.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_21.setLineWidth(-1)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(410, 330, 131, 31))
        self.label_22.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_22.setLineWidth(-1)
        self.label_22.setObjectName("label_22")
        self.username_12 = QtWidgets.QLineEdit(self.frame)
        self.username_12.setGeometry(QtCore.QRect(80, 190, 241, 22))
        self.username_12.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.username_12.setText("")
        self.username_12.setObjectName("username_12")
        self.username_13 = QtWidgets.QLineEdit(self.frame)
        self.username_13.setGeometry(QtCore.QRect(80, 330, 241, 22))
        self.username_13.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.username_13.setText("")
        self.username_13.setObjectName("username_13")
        
        self.username_14 = QtWidgets.QLineEdit(self.frame)
        self.username_14.setGeometry(QtCore.QRect(570, 320, 241, 22))
        self.username_14.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.username_14.setText("")
        self.username_14.setEchoMode(QtWidgets.QLineEdit.Password)
        self.username_14.setObjectName("username_14")
        self.username_15 = QtWidgets.QLineEdit(self.frame)
        self.username_15.setGeometry(QtCore.QRect(130, 480, 241, 22))
        self.username_15.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.username_15.setText("")
        self.username_15.setObjectName("username_15")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(440, 230, 61, 31))
        self.label_23.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_23.setObjectName("label_23")
        self.password_4 = QtWidgets.QLineEdit(self.frame)
        self.password_4.setGeometry(QtCore.QRect(550, 240, 251, 22))
        self.password_4.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.password_4.setText("")
        
        self.password_4.setObjectName("password_4")
        self.username_16 = QtWidgets.QLineEdit(self.frame)
        self.username_16.setGeometry(QtCore.QRect(80, 250, 241, 22))
        self.username_16.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.username_16.setText("")
        self.username_16.setObjectName("username_16")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(20, 470, 81, 31))
        self.label_24.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_24.setLineWidth(-1)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(430, 470, 151, 31))
        self.label_25.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_25.setLineWidth(-1)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(20, 250, 41, 31))
        self.label_26.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_26.setLineWidth(-1)
        self.label_26.setObjectName("label_26")
        self.username_17 = QtWidgets.QLineEdit(self.frame)
        self.username_17.setGeometry(QtCore.QRect(610, 480, 241, 22))
        self.username_17.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.username_17.setText("")
        self.username_17.setObjectName("username_17")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(20, 370, 171, 31))
        self.label_27.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_27.setLineWidth(-1)
        self.label_27.setObjectName("label_27")
        self.username_18 = QtWidgets.QLineEdit(self.frame)
        self.username_18.setGeometry(QtCore.QRect(230, 380, 401, 22))
        self.username_18.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.username_18.setText("")
        self.username_18.setObjectName("username_18")
        self.username_19 = QtWidgets.QLineEdit(self.frame)
        self.username_19.setGeometry(QtCore.QRect(130, 530, 241, 22))
        self.username_19.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"\n"
"")
        self.username_19.setText("")
        self.username_19.setObjectName("username_19")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(30, 520, 151, 31))
        self.label_28.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_28.setLineWidth(-1)
        self.label_28.setObjectName("label_28")
        self.username_20 = QtWidgets.QLineEdit(self.frame)
        self.username_20.setGeometry(QtCore.QRect(550, 170, 251, 22))
        self.username_20.setStyleSheet("QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px;\n"
"border-radius:4px;\n"
"color:rgb(184, 179, 174);\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.username_20.setText("")
        self.username_20.setObjectName("username_20")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(440, 170, 61, 31))
        self.label_29.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_29.setLineWidth(-1)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(30, 80, 311, 41))
        self.label_30.setStyleSheet("*{\n"
"    font: 8pt \"Tw Cen MT Condensed Extra Bold\";\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"    color: rgb(127, 158, 178);\n"
"}")
        self.label_30.setLineWidth(-1)
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(190, 380, 21, 20))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("image/date.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(30, 430, 311, 41))
        self.label_31.setStyleSheet("*{\n"
"    font: 8pt \"Tw Cen MT Condensed Extra Bold\";\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"    color: rgb(127, 158, 178);\n"
"}")
        self.label_31.setLineWidth(-1)
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(490, 530, 271, 16))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1201, 1101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/inscrit.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_16.setText(_translate("MainWindow", "INSCRIPTION"))
        self.buttonlogin_3.setText(_translate("MainWindow", "Ajouter"))
        self.username_11.setPlaceholderText(_translate("MainWindow", "nom"))
        self.password_3.setPlaceholderText(_translate("MainWindow", "prenom"))
        self.label_17.setText(_translate("MainWindow", "Nom"))
        self.label_18.setText(_translate("MainWindow", "Prenom"))
        self.buttoninscription_2.setText(_translate("MainWindow", "Vous avez un compte ? Connectez-vous"))
        self.buttonlogin_4.setText(_translate("MainWindow", "ANNULER"))
        self.label_20.setText(_translate("MainWindow", "CIN"))
        self.label_21.setText(_translate("MainWindow", "Login"))
        self.label_22.setText(_translate("MainWindow", "Mot de passe"))
        self.username_12.setPlaceholderText(_translate("MainWindow", "XXXXXXXX"))
        self.username_13.setPlaceholderText(_translate("MainWindow", "login"))
        self.username_14.setPlaceholderText(_translate("MainWindow", "XXXXXXXXXXXXXXX"))
        self.username_15.setPlaceholderText(_translate("MainWindow", "informatique"))
        self.label_23.setText(_translate("MainWindow", "Region"))
        self.password_4.setPlaceholderText(_translate("MainWindow", "Tunis"))
        self.username_16.setPlaceholderText(_translate("MainWindow", "Tunisie"))
        self.label_24.setText(_translate("MainWindow", "Domaine"))
        self.label_25.setText(_translate("MainWindow", "Centre d\'intéret"))
        self.label_26.setText(_translate("MainWindow", "Pays"))
        self.username_17.setPlaceholderText(_translate("MainWindow", "Centre d\'intéret"))
        self.label_27.setText(_translate("MainWindow", "Date de naissance"))
        self.username_18.setPlaceholderText(_translate("MainWindow", "JJ/MM/AAAA"))
        self.username_19.setPlaceholderText(_translate("MainWindow", "Preferance"))
        self.label_28.setText(_translate("MainWindow", "Preferance"))
        self.username_20.setPlaceholderText(_translate("MainWindow", "XXXXXX@gmail.com"))
        self.label_29.setText(_translate("MainWindow", "Email"))
        self.label_30.setText(_translate("MainWindow", " Informations personnelle :"))
        self.label_31.setText(_translate("MainWindow", "Votre Profil"))

    def connecter(self):
          from login import Ui_MainWindow
          self.window2=QtWidgets.QMainWindow()
          self.ui= Ui_MainWindow()
          self.ui.setupUi(self.window2)
          self.window2.show() 
          Ui_MainWindowi.form.close()
    def annuler(self):
        self.username_11.clear()
        self.password_3.clear()
        self.username_12.clear()
        self.username_13.clear()
        self.username_14.clear()
        self.username_15.clear()
        self.username_16.clear()
        self.username_17.clear()
        self.username_18.clear()
        self.username_19.clear()
        self.username_20.clear()
        self.password_4.clear()
    def inscription (self):
           if self.username_12.text()not in (None, '') and self.username_11.text()  not in (None, '') and self.username_13.text()not in (None, '') and self.username_14.text()not in (None, '') and self.username_15.text() not in (None, '') and self.username_16.text()not in (None, '')  and self.username_17.text()not in (None, '')  and self.username_18.text()not in (None, '') and self.username_19.text()not in (None, '') and self.username_20.text()not in (None, '') and self.password_4.text()not in (None, '') and self.password_3.text()not in (None, '') :
              BD.ajouter_user(self.username_12.text(),self.username_11.text(),self.password_3.text(),self.username_18.text(),self.username_15.text(),self.password_4.text(),self.username_16.text(),self.username_17.text(),self.username_19.text(),self.username_13.text(),self.username_14.text(),self.username_20.text())
              from login import Ui_MainWindow
              self.window2=QtWidgets.QMainWindow()
              self.ui= Ui_MainWindow()
              self.ui.setupUi(self.window2)
              self.window2.show() 
              Ui_MainWindowi.form.close()  
           else :
              self.label_5.setText("remplire les champs")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

