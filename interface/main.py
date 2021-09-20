# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('../')

import manipulerfichier
from offre import offre
import BD

class Ui_MainWindowM(object):
     user=None
     form=None
     offre=[]
     indice_offre=0
     def setupUi(self, MainWindowM):
        Ui_MainWindowM.form=MainWindowM
        MainWindowM.setObjectName("MainWindow")
        MainWindowM.resize(1229, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindowM)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 9, 1200, 1191))
        self.frame_2.setMinimumSize(QtCore.QSize(1200, 0))
        self.frame_2.setStyleSheet("QFrame\n"
" {\n"
"border-radius:5px;\n"
"background-color:white;\n"
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
        self.frame.setGeometry(QtCore.QRect(0, 0, 211, 711))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background-color: rgb(169, 195, 255);\n"
"\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(-10, -20, 221, 111))
        self.frame_3.setStyleSheet("QFrame\n"
"\n"
"{\n"
"background-color: rgb(160, 168, 187);\n"
"border-radius:60px;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 211, 91))
        self.label_2.setStyleSheet("\n"
"\n"
"background-color: rgb(169, 195, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../image/inscrit.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(20, 30, 191, 51))
        self.label.setStyleSheet("font: 87 9pt \"Arial Black\";\n"
"color: rgb(90, 94, 122);\n"
"background-color: rgb(169, 195, 255);")
        self.label.setObjectName("label")
        self.nom = QtWidgets.QLabel(self.frame_3)
        self.nom.setGeometry(QtCore.QRect(40, 70, 151, 31))
        self.nom.setStyleSheet("*{\n"
"\n"
"font-family:century gothic;\n"
"font-size:14px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(0, 0, 127);\n"
"}")
        self.nom.setLineWidth(-1)
        self.nom.setText("")
        self.nom.setObjectName("nom")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 130, 201, 41))
        self.label_4.setStyleSheet("font: 9pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(160, 168, 187);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_img_user = QtWidgets.QLabel(self.frame)
        self.label_img_user.setGeometry(QtCore.QRect(130, 132, 41, 31))
        self.label_img_user.setStyleSheet("background-color: rgb(160, 168, 187);")
        self.label_img_user.setText("")
        self.label_img_user.setPixmap(QtGui.QPixmap("image/user.png"))
        self.label_img_user.setScaledContents(True)
        self.label_img_user.setObjectName("label_img_user")
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setGeometry(QtCore.QRect(10, 180, 191, 501))
        self.frame_10.setStyleSheet("*{ border: 1px solid white }")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_domaine = QtWidgets.QLabel(self.frame_10)
        self.label_domaine.setGeometry(QtCore.QRect(20, 350, 151, 31))
        self.label_domaine.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(0, 0, 127);\n"
"border:none;\n"
"}")
        self.label_domaine.setLineWidth(-1)
        self.label_domaine.setText("")
        self.label_domaine.setObjectName("label_domaine")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.label_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(85, 85, 255);\n"
"}")
        self.label_5.setLineWidth(-1)
        self.label_5.setObjectName("label_5")
        self.ville = QtWidgets.QLabel(self.frame_10)
        self.ville.setGeometry(QtCore.QRect(20, 150, 131, 31))
        self.ville.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(0, 0, 127);\n"
"border:none;\n"
"}")
        self.ville.setLineWidth(-1)
        self.ville.setText("")
        self.ville.setObjectName("ville")
        self.label_7 = QtWidgets.QLabel(self.frame_10)
        self.label_7.setGeometry(QtCore.QRect(10, 210, 151, 31))
        self.label_7.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:11px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(85, 85, 255);\n"
"}")
        self.label_7.setLineWidth(-1)
        self.label_7.setObjectName("label_7")
        self.age = QtWidgets.QLabel(self.frame_10)
        self.age.setGeometry(QtCore.QRect(10, 260, 151, 31))
        self.age.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(0, 0, 127);\n"
"border:none;\n"
"}")
        self.age.setLineWidth(-1)
        self.age.setText("")
        self.age.setObjectName("age")
        self.label_9 = QtWidgets.QLabel(self.frame_10)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 151, 31))
        self.label_9.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(85, 85, 255);\n"
"}")
        self.label_9.setLineWidth(-1)
        self.label_9.setObjectName("label_9")
        self.mail = QtWidgets.QLabel(self.frame_10)
        self.mail.setGeometry(QtCore.QRect(20, 60, 151, 31))
        self.mail.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:11px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(0, 0, 127);\n"
"border:none;\n"
"}")
        self.mail.setLineWidth(-1)
        self.mail.setText("")
        self.mail.setObjectName("mail")
        self.label_11 = QtWidgets.QLabel(self.frame_10)
        self.label_11.setGeometry(QtCore.QRect(10, 410, 151, 31))
        self.label_11.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(85, 85, 255);\n"
"}")
        self.label_11.setLineWidth(-1)
        self.label_11.setObjectName("label_11")
        self.centre = QtWidgets.QLabel(self.frame_10)
        self.centre.setGeometry(QtCore.QRect(10, 450, 151, 31))
        self.centre.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(0, 0, 127);\n"
"border:none;\n"
"}")
        self.centre.setLineWidth(-1)
        self.centre.setText("")
        
        
        self.centre.setObjectName("centre")
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 161, 31))
        self.label_6.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(85, 85, 255);\n"
" \n"
"\n"
"}")
        self.label_6.setLineWidth(-1)
        self.label_6.setObjectName("label_6")
        self.frame_10.raise_()
        self.frame_3.raise_()
        self.label_4.raise_()
        self.label_img_user.raise_()
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(220, 0, 971, 81))
        self.frame_5.setStyleSheet("QFrame\n"
"\n"
"\n"
"{\n"
"\n"
"\n"
"     border: 1px solid r rgb(170, 170, 255);\n"
"    background-color: rgb(213, 178, 255);\n"
"}\n"
"\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.logout = QtWidgets.QPushButton(self.frame_5)
        self.logout.setGeometry(QtCore.QRect(860, 30, 91, 31))
        self.logout.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:15px;\n"
"font-size:17px;\n"
"\n"
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
        self.logout.setText("")
        #event deconecter
        self.logout.clicked.connect(self.deconnecter)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon)
        self.logout.setIconSize(QtCore.QSize(50, 50))
        self.logout.setCheckable(False)
        self.logout.setObjectName("logout")
        self.label_32 = QtWidgets.QLabel(self.frame_5)
        self.label_32.setGeometry(QtCore.QRect(880, 30, 51, 31))
        self.label_32.setStyleSheet("QLabel\n"
"{\n"
"background:rgb(0, 0, 0,0);\n"
"}")
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("../../.designer/backup/in.png"))
        self.label_32.setObjectName("label_32")
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        self.frame_11.setGeometry(QtCore.QRect(20, 10, 751, 61))
        self.frame_11.setStyleSheet("QFrame\n"
"{\n"
"    background-color: rgb(213, 178, 255);\n"
"border-radius:20px;\n"
"border-color:none;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.lieu = QtWidgets.QLineEdit(self.frame_11)
        self.lieu.setGeometry(QtCore.QRect(160, 10, 141, 31))
        self.lieu.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
" border: 1px solid white \n"
"color:white;\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.lieu.setText("")
        self.lieu.setObjectName("lieu")
        self.domaine = QtWidgets.QLineEdit(self.frame_11)
        self.domaine.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.domaine.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
" border: 1px solid white \n"
"color:white;\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.domaine.setText("")
        self.domaine.setObjectName("domaine")
        self.type_stage = QtWidgets.QLineEdit(self.frame_11)
        self.type_stage.setGeometry(QtCore.QRect(350, 10, 171, 31))
        self.type_stage.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
" border: 1px solid white\n"
"color:white;\n"
"border-bottom:1px solide #717072;\n"
"font-family:century gothic;\n"
"font-size:13px;\n"
"}\n"
"")
        self.type_stage.setText("")
        self.type_stage.setObjectName("type_stage")
        self.recherche = QtWidgets.QPushButton(self.frame_11)
        self.recherche.setGeometry(QtCore.QRect(630, 10, 61, 31))
        self.recherche.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:15px;\n"
"background:rgba(0,0,0,0.0);\n"
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
        self.recherche.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/loupe (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recherche.setIcon(icon1)
        self.recherche.setObjectName("recherche")
        #event rehcercher
        self.recherche.clicked.connect(self.recherche_offre)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setGeometry(QtCore.QRect(20, 90, 961, 721))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_32.raise_()
        self.logout.raise_()
        self.frame_11.raise_()
        self.frame_7.raise_()
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(4220, 190, 261, 41))
        self.label_16.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:40px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(247, 135, 79);\n"
"}")
        self.label_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_16.setObjectName("label_16")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(3290, 160, 1661, 1021))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../../.designer/backup/oumaima.jpg"))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(430, 930, 4841, 1781))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../../.designer/backup/unsplash.jpg"))
        self.label_10.setObjectName("label_10")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(4700, 170, 261, 41))
        self.label_17.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:40px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:rgb(247, 135, 79);\n"
"}")
        self.label_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_17.setObjectName("label_17")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(3770, 140, 1661, 1021))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("../../.designer/backup/oumaima.jpg"))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(910, 910, 4841, 1781))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("../../.designer/backup/unsplash.jpg"))
        self.label_14.setObjectName("label_14")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(220, 90, 971, 521))
        self.frame_6.setStyleSheet("QFrame\n"
"{\n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_86 = QtWidgets.QLabel(self.frame_6)
        self.label_86.setGeometry(QtCore.QRect(30, 18, 121, 31))
        self.label_86.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:20px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"border: 1px solid white \n"
"}")
        self.label_86.setLineWidth(-1)
        self.label_86.setScaledContents(False)
        self.label_86.setAlignment(QtCore.Qt.AlignCenter)
        self.label_86.setWordWrap(False)
        self.label_86.setObjectName("label_86")
        self.label_88 = QtWidgets.QLabel(self.frame_6)
        self.label_88.setGeometry(QtCore.QRect(30, 260, 311, 31))
        self.label_88.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:12px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:red;\n"
"font-size:14px;\n"
"}")
        self.label_88.setText("")
        self.label_88.setObjectName("label_88")
        self.Titre_5 = QtWidgets.QLabel(self.frame_6)
        self.Titre_5.setGeometry(QtCore.QRect(160, 20, 611, 31))
        self.Titre_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.Titre_5.setLineWidth(-1)
        self.Titre_5.setText("")
        self.Titre_5.setObjectName("Titre_5")
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setGeometry(QtCore.QRect(20, 60, 771, 301))
        self.frame_4.setStyleSheet("*{ border: 1px solid white }")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.Date_debut_5 = QtWidgets.QLabel(self.frame_4)
        self.Date_debut_5.setGeometry(QtCore.QRect(540, 110, 191, 31))
        self.Date_debut_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.Date_debut_5.setLineWidth(-1)
        self.Date_debut_5.setText("")
        self.Date_debut_5.setObjectName("Date_debut_5")
        self.label_90 = QtWidgets.QLabel(self.frame_4)
        self.label_90.setGeometry(QtCore.QRect(390, 110, 121, 31))
        self.label_90.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_90.setLineWidth(-1)
        self.label_90.setObjectName("label_90")
        self.region_5 = QtWidgets.QLabel(self.frame_4)
        self.region_5.setGeometry(QtCore.QRect(540, 10, 191, 31))
        self.region_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.region_5.setText("")
        self.region_5.setObjectName("region_5")
        self.label_92 = QtWidgets.QLabel(self.frame_4)
        self.label_92.setGeometry(QtCore.QRect(390, 10, 101, 31))
        self.label_92.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_92.setObjectName("label_92")
        self.REMUNERATION_5 = QtWidgets.QLabel(self.frame_4)
        self.REMUNERATION_5.setGeometry(QtCore.QRect(540, 230, 191, 31))
        self.REMUNERATION_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.REMUNERATION_5.setLineWidth(-1)
        self.REMUNERATION_5.setText("")
        self.REMUNERATION_5.setObjectName("REMUNERATION_5")
        self.label_89 = QtWidgets.QLabel(self.frame_4)
        self.label_89.setGeometry(QtCore.QRect(10, 120, 121, 31))
        self.label_89.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_89.setLineWidth(-1)
        self.label_89.setObjectName("label_89")
        self.Experience_5 = QtWidgets.QLabel(self.frame_4)
        self.Experience_5.setGeometry(QtCore.QRect(170, 120, 151, 31))
        self.Experience_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.Experience_5.setLineWidth(-1)
        self.Experience_5.setText("")
        self.Experience_5.setObjectName("Experience_5")
        self.type_offre_5 = QtWidgets.QLabel(self.frame_4)
        self.type_offre_5.setGeometry(QtCore.QRect(170, 70, 151, 31))
        self.type_offre_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.type_offre_5.setLineWidth(-1)
        self.type_offre_5.setText("")
        self.type_offre_5.setObjectName("type_offre_5")
        self.label_94 = QtWidgets.QLabel(self.frame_4)
        self.label_94.setGeometry(QtCore.QRect(10, 70, 121, 31))
        self.label_94.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_94.setLineWidth(-1)
        self.label_94.setObjectName("label_94")
        self.Domaine_5 = QtWidgets.QLabel(self.frame_4)
        self.Domaine_5.setGeometry(QtCore.QRect(170, 20, 151, 31))
        self.Domaine_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.Domaine_5.setText("")
        self.Domaine_5.setObjectName("Domaine_5")
        self.label_91 = QtWidgets.QLabel(self.frame_4)
        self.label_91.setGeometry(QtCore.QRect(390, 180, 121, 31))
        self.label_91.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_91.setLineWidth(-1)
        self.label_91.setObjectName("label_91")
        self.duree_5 = QtWidgets.QLabel(self.frame_4)
        self.duree_5.setGeometry(QtCore.QRect(540, 180, 181, 31))
        self.duree_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.duree_5.setLineWidth(-1)
        self.duree_5.setText("")
        self.duree_5.setObjectName("duree_5")
        self.label_96 = QtWidgets.QLabel(self.frame_4)
        self.label_96.setGeometry(QtCore.QRect(10, 180, 151, 31))
        self.label_96.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_96.setLineWidth(-1)
        self.label_96.setObjectName("label_96")
        self.niveau_etude_5 = QtWidgets.QLabel(self.frame_4)
        self.niveau_etude_5.setGeometry(QtCore.QRect(170, 180, 151, 31))
        self.niveau_etude_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.niveau_etude_5.setLineWidth(-1)
        self.niveau_etude_5.setText("")
        self.niveau_etude_5.setObjectName("niveau_etude_5")
        self.label_95 = QtWidgets.QLabel(self.frame_4)
        self.label_95.setGeometry(QtCore.QRect(390, 230, 121, 31))
        self.label_95.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_95.setLineWidth(-1)
        self.label_95.setObjectName("label_95")
        self.label_98 = QtWidgets.QLabel(self.frame_4)
        self.label_98.setGeometry(QtCore.QRect(390, 60, 111, 31))
        self.label_98.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_98.setLineWidth(-1)
        self.label_98.setObjectName("label_98")
        self.pays_5 = QtWidgets.QLabel(self.frame_4)
        self.pays_5.setGeometry(QtCore.QRect(540, 50, 191, 31))
        self.pays_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.pays_5.setLineWidth(-1)
        self.pays_5.setText("")
        self.pays_5.setObjectName("pays_5")
        self.label_93 = QtWidgets.QLabel(self.frame_4)
        self.label_93.setGeometry(QtCore.QRect(10, 230, 161, 31))
        self.label_93.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"\n"
"}")
        self.label_93.setLineWidth(-1)
        self.label_93.setObjectName("label_93")
        self.nb_poste_5 = QtWidgets.QLabel(self.frame_4)
        self.nb_poste_5.setGeometry(QtCore.QRect(180, 230, 141, 31))
        self.nb_poste_5.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"\n"
"}")
        self.nb_poste_5.setLineWidth(-1)
        self.nb_poste_5.setText("")
        self.nb_poste_5.setObjectName("nb_poste_5")
        self.label_87 = QtWidgets.QLabel(self.frame_4)
        self.label_87.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.label_87.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.label_87.setObjectName("label_87")
        self.label_97 = QtWidgets.QLabel(self.frame_6)
        self.label_97.setGeometry(QtCore.QRect(30, 370, 201, 21))
        self.label_97.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:17px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"border: 1px solid white \n"
"}")
        self.label_97.setLineWidth(-1)
        self.label_97.setObjectName("label_97")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(20, 410, 771, 81))
        self.label_3.setStyleSheet("*{ border: 1px solid white ;color:white; }")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.frame_4.raise_()
        self.label_86.raise_()
        self.label_88.raise_()
        self.Titre_5.raise_()
        self.label_97.raise_()
        self.label_3.raise_()
        self.frame_12 = QtWidgets.QFrame(self.frame_2)
        self.frame_12.setGeometry(QtCore.QRect(480, 640, 261, 51))
        self.frame_12.setStyleSheet("QFrame\n"
"{\n"
"background:rgba(0,0,0,00.3);\n"
"border-radius:20px;\n"
"color:white;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.suivant = QtWidgets.QPushButton(self.frame_12)
        self.suivant.setGeometry(QtCore.QRect(160, 10, 101, 31))
        self.suivant.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:15px;\n"
"\n"
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
        self.suivant.setObjectName("suivant")
        #event suivant
        self.suivant.clicked.connect(self.suivant_button)
        self.president = QtWidgets.QPushButton(self.frame_12)
        self.president.setGeometry(QtCore.QRect(0, 10, 101, 31))
        self.president.setStyleSheet("QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:15px;\n"
"\n"
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
        self.president.setObjectName("president")
        self.president.clicked.connect(self.president_button)
        self.num_offre = QtWidgets.QLabel(self.frame_12)
        self.num_offre.setGeometry(QtCore.QRect(120, 20, 21, 20))
        self.num_offre.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:12px;\n"
"}\n"
"QLabel\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.num_offre.setText("")
        self.num_offre.setObjectName("num_offre")
        self.frame_5.raise_()
        self.frame.raise_()
        self.label_16.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_17.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.frame_6.raise_()
        self.frame_12.raise_()
        MainWindowM.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowM)
        self.statusbar.setObjectName("statusbar")
        MainWindowM.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowM)
        QtCore.QMetaObject.connectSlotsByName(MainWindowM)
#remplire les label
        self.nom.setText(Ui_MainWindowM.user[0][1]+" "+Ui_MainWindowM.user[0][2])
        self.age.setText(Ui_MainWindowM.user[0][3])
        self.ville.setText(Ui_MainWindowM.user[0][5])
        self.mail.setText(Ui_MainWindowM.user[0][11])
        self.centre.setText(Ui_MainWindowM.user[0][7])
        self.label_domaine.setText(Ui_MainWindowM.user[0][4])
        
        #remplir premier offre
        self.intialisation()

     def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Binvenue dans votre session"))
        self.label_4.setText(_translate("MainWindow", " Votre profil :"))
        self.label_5.setText(_translate("MainWindow", "Ville :"))
        self.label_7.setText(_translate("MainWindow", "Date de naissance:"))
        self.label_9.setText(_translate("MainWindow", "Email"))
        self.label_11.setText(_translate("MainWindow", "centre d\'intere"))
        self.label_6.setText(_translate("MainWindow", "votre Domaine :"))
        self.lieu.setPlaceholderText(_translate("MainWindow", "Lieu"))
        self.domaine.setPlaceholderText(_translate("MainWindow", "Domaine"))
        self.type_stage.setPlaceholderText(_translate("MainWindow", " Type de stage"))
        self.label_16.setText(_translate("MainWindow", "ACTIA"))
        self.label_17.setText(_translate("MainWindow", "ACTIA"))
        self.label_86.setText(_translate("MainWindow", "Titre:"))
        self.label_90.setText(_translate("MainWindow", "Date debut:"))
        self.label_92.setText(_translate("MainWindow", "Region:"))
        self.label_89.setText(_translate("MainWindow", "Experience:"))
        self.label_94.setText(_translate("MainWindow", "Type d\'offre:"))
        self.label_91.setText(_translate("MainWindow", "Duree:"))
        self.label_96.setText(_translate("MainWindow", "NiveAu d\'etude:"))
        self.label_95.setText(_translate("MainWindow", "Rémunération :"))
        self.label_98.setText(_translate("MainWindow", "Pays :"))
        self.label_93.setText(_translate("MainWindow", "Nombre de poste:"))
        self.label_87.setText(_translate("MainWindow", "Domaine:"))
        self.label_97.setText(_translate("MainWindow", "Description de l\'offre :"))
        self.suivant.setText(_translate("MainWindow", "Suivant"))
        self.president.setText(_translate("MainWindow", "Précédente"))
     def deconnecter(self):
            from login import Ui_MainWindow
            self.window2=QtWidgets.QMainWindow()
            self.ui= Ui_MainWindow()
            self.ui.setupUi(self.window2)
            self.window2.show() 
            Ui_MainWindowM.form.close() 
     def remplire_les_offre(self,i):
        self.Titre_5.setText(Ui_MainWindowM.offre[i].titre)
        self.Domaine_5.setText(Ui_MainWindowM.offre[i].domaine)
        self.Experience_5.setText(Ui_MainWindowM.offre[i].experience)
        self.Date_debut_5.setText(Ui_MainWindowM.offre[i].date_debut)
        self.duree_5.setText(Ui_MainWindowM.offre[i].dureé)
        self.label_3.setText(Ui_MainWindowM.offre[i].description)
        self.pays_5.setText(Ui_MainWindowM.offre[i].pays)
        self.region_5.setText(Ui_MainWindowM.offre[i].region)
        self.REMUNERATION_5.setText(str(Ui_MainWindowM.offre[i].remunerationproposee))
        self.nb_poste_5.setText(str(Ui_MainWindowM.offre[i].nombre_de_poste))
        self.type_offre_5.setText(Ui_MainWindowM.offre[i].typeoffre)
        self.niveau_etude_5.setText(Ui_MainWindowM.offre[i].niveao_etude)
        self.num_offre.setText(str(i+1)+"/"+str(len(Ui_MainWindowM.offre))) 
     def vider_les_offre(self):
        self.Titre_5.clear()
        self.Domaine_5.clear()
        self.Experience_5.clear()
        self.Date_debut_5.clear()
        self.duree_5.clear()
        self.label_3.clear()
        self.pays_5.clear()
        self.region_5.clear()
        self.REMUNERATION_5.clear()
        self.nb_poste_5.clear()
        self.type_offre_5.clear()
        self.niveau_etude_5.clear()
        self.num_offre.setText(str(0)+"/"+str(0))
     def suivant_button(self)  :
        if Ui_MainWindowM.indice_offre+1<len(Ui_MainWindowM.offre):
             Ui_MainWindowM.indice_offre+=1
             self.remplire_les_offre(Ui_MainWindowM.indice_offre)
             
     def president_button(self)  :
        if Ui_MainWindowM.indice_offre-1>=0:
             Ui_MainWindowM.indice_offre-=1
             self.remplire_les_offre(Ui_MainWindowM.indice_offre)
             
     def recherche_offre(self):

          if self.domaine.text()=="" and self.lieu.text()==""and self.type_stage.text()=="" :
              Ui_MainWindowM.offre.clear()
              self.intialisation()
              
          elif self.domaine.text()!="" and self.lieu.text()=="" and self.type_stage.text()=="" :
              Ui_MainWindowM.offre.clear()
              l=[]
              l.extend(manipulerfichier.lire_les_fichiers())
              for off in l :
                  if  self.domaine.text() == off.domaine :
                       Ui_MainWindowM.offre.append(off)
              Ui_MainWindowM.offre.extend(BD.offre_bd_domaine(self.domaine.text()))  
              
              if len(Ui_MainWindowM.offre)>0 :
               Ui_MainWindowM.indice_offre=0   
               self.remplire_les_offre(Ui_MainWindowM().indice_offre)
              else :
                  self.vider_les_offre()

              
          elif self.domaine.text()=="" and self.lieu.text()=="" and self.type_stage.text()!="" :
              Ui_MainWindowM.offre.clear()
              l=[]
              l.extend(manipulerfichier.lire_les_fichiers())
              for off in l :
                  if  off.typeoffre == self.type_stage.text() :     
                       Ui_MainWindowM.offre.append(off)
              Ui_MainWindowM.offre.extend(BD.offre_bd_type(self.type_stage.text()))  
              
              if len(Ui_MainWindowM.offre)>0 :
               Ui_MainWindowM.indice_offre=0   
               self.remplire_les_offre(Ui_MainWindowM().indice_offre)
              else :
                  self.vider_les_offre()  
              
          elif self.domaine.text()=="" and self.lieu.text()!="" and self.type_stage.text()=="" :
              
              Ui_MainWindowM.offre.clear()
              l=[]
              l.extend(manipulerfichier.lire_les_fichiers())
              for off in l :
               
                  if  self.lieu.text().lower() in off.pays.lower() or self.lieu.text().lower() in  off.region.lower() :
                       Ui_MainWindowM.offre.append(off)        
              Ui_MainWindowM.offre.extend(BD.offre_bd_pays(self.lieu.text()))
              Ui_MainWindowM.offre.extend(BD.offre_bd_region(self.lieu.text()))  
             
              if len(Ui_MainWindowM.offre)>0 :
               Ui_MainWindowM.indice_offre=0   
               self.remplire_les_offre(Ui_MainWindowM().indice_offre)  
               
              else :
                  self.vider_les_offre()      
              
              
              
              
                       
                       
              
     def intialisation(self):
          Ui_MainWindowM.offre.clear()
          l= [] 
          l.extend(BD.offre_bd_all())
          l.extend(manipulerfichier.lire_les_fichiers())
       
      
          for off in l :
              
              if Ui_MainWindowM.user[0][7]==off.domaine or Ui_MainWindowM.user[0][8]==off.domaine  or Ui_MainWindowM.user[0][7] in  off.description or Ui_MainWindowM.user[0][8] in off.description:
                    Ui_MainWindowM.offre.append(off)
          if len(Ui_MainWindowM.offre) >0:
              
             Ui_MainWindowM.indice_offre=0        
             self.remplire_les_offre(Ui_MainWindowM.indice_offre)                        
                   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowM()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
