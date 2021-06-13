# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CBIR.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from os import environ
from db import *
import os 
from FeatureExtractor import *
import pickle
import cv2
from helpers.Evaluation import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtCore import QSize, Qt

imagepath = ''
videoname = ''
clickedItem = ''
database = DB("cbDatabase")

mycursor = database.get_cursor()
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

class Window2(object):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window22222")
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1284, 828)
        MainWindow.setStyleSheet("background-color: rgb(33, 37, 41);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --------------------Widget for buttons and image-------------------
        self.widget = QtWidgets.QLabel(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 50, 891, 351))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color: rgb(52, 58, 64);")
        self.widget.setObjectName("widget")

        #-----------------Upload buttons--------------------------

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(230, 140, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: transparent;\n"
"color: rgb(233, 236, 239);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/cloud_upload_white_192x192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.getImage)


        #-----------------button new video-----------------------
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 140, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: transparent;\n"
"color: rgb(233, 236, 239);")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.getVideo)
        
        
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(5, 140, 1000, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: transparent;\n"
"color: rgb(233, 236, 239);")
        
        self.pushButton_4.setObjectName("pushButton_3")
        
        self.pushButton_4.hide()


        #------------------/---------------
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(430, 150, 16, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(233, 236, 239);")
        self.label_6.setObjectName("label_6")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 400, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(233, 236, 239);")
        self.label_2.setObjectName("label_2")
        
        
        self.widget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(20, 440, 1241 , 341))
        self.widget_2.setStyleSheet("background-color: rgb(52, 58, 64);")
        self.widget_2.setObjectName("widget_2")
        self.widget_2.itemClicked.connect(self.item_click)
        
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(920, 40, 331, 341))
        self.widget_3.setObjectName("widget_3")
        
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(400, 300, 500, 200))
        self.widget_4.setStyleSheet("background-color: rgb(33, 37, 41);")
        self.widget_4.setObjectName("widget_4")
        self.label2 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color: rgb(233, 236, 239);")
        self.label2.setObjectName("label2")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setGeometry(QtCore.QRect(80, 1, 350, 200))
        self.widget_4.hide()
        
        
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(0, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(233, 236, 239);")
        self.label.setObjectName("label")
        
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 170, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: rgb(233, 236, 239);")
        self.radioButton_3.setObjectName("radioButton_3")
        
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_5.setGeometry(QtCore.QRect(50, 210, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("color: rgb(233, 236, 239);")
        self.radioButton_5.setObjectName("radioButton_3")
        
        self.radioButton = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton.setGeometry(QtCore.QRect(50, 130, 200, 33))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(233, 236, 239);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(233, 236, 239);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(233, 236, 239);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(233, 236, 239);")
        self.label_5.setObjectName("label_5")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_4.setGeometry(QtCore.QRect(50, 280, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color: rgb(233, 236, 239);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(233, 236, 239);")
        self.label_3.setObjectName("label_3")

        #---------------------new-----------
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 27, 61, 21))
        self.pushButton_2.setStyleSheet("color: rgb(233, 236, 239);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.New)
        self.pushButton_2.hide()


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #==radiobuttons====
        self.radioButton.toggled.connect(lambda: self.method(self.radioButton))
        self.radioButton_2.toggled.connect(lambda: self.method(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda: self.method(self.radioButton_3))
        self.radioButton_4.toggled.connect(lambda: self.method(self.radioButton_4))
        self.radioButton_5.toggled.connect(lambda: self.method(self.radioButton_5))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CBIR/CBVR"))
        self.pushButton.setText(_translate("MainWindow", "Upload Photo"))
        self.pushButton_3.setText(_translate("MainWindow", "Upload Video"))
        self.label_6.setText(_translate("MainWindow", "/"))
        self.label_2.setText(_translate("MainWindow", "Images/Videos Retrieved"))
        self.label.setText(_translate("MainWindow", "Choose Search Method:"))
        self.radioButton_3.setText(_translate("MainWindow", "Mean RGB"))
        self.radioButton.setText(_translate("MainWindow", "Histogram"))
        self.radioButton_2.setText(_translate("MainWindow", "Color Layout"))
        self.radioButton_5.setText(_translate("MainWindow", "Dominant Color"))
        self.label_4.setText(_translate("MainWindow", "Image:"))
        self.label_5.setText(_translate("MainWindow", "Video:"))
        self.radioButton_4.setText(_translate("MainWindow", "Video Histogram"))
        self.label_3.setText(_translate("MainWindow", "Content Based Image/Video Retrivel"))
        self.pushButton_2.setText(_translate("MainWindow", "New"))
        self.label2.setText(_translate("MainWindow", "Retrieving from Database..."))


    def getImage(self):
        global imagepath
        fname = QFileDialog.getOpenFileName()
        imagepath = fname[0]
        pixmap = QPixmap(imagepath)
        # self.widget.setScaledContents(True)
        print(imagepath)
        self.pushButton.hide()
        self.label_6.hide()
        self.pushButton_3.hide()
        self.widget.setAlignment(QtCore.Qt.AlignCenter)
        self.widget.setPixmap(pixmap.scaled(self.widget.width(),self.widget.height(),Qt.KeepAspectRatio))
        self.pushButton_2.show()
    
    def getVideo(self):
        global videoname
        fname = QFileDialog.getOpenFileName()
        videoname = fname[0]
        video = os.path.basename(videoname)
        self.pushButton.hide()
        self.label_6.hide()
        self.pushButton_3.hide()
        self.pushButton_4.setText(video + ' uploaded succefully!')
        self.pushButton_4.show()
        self.pushButton_4.clicked.connect(self.playvideo)
        self.pushButton_2.show()
        
    def playvideo(self):
        os.system('C:\\Users\\Lenovo\\Videos\\Captures\\a.mp4')
        # os.system(videoname)
        # vidcap = cv2.VideoCapture(videoname)
        # success, image = vidcap.read()
        # if success:
        #     cv2.imwrite("first_frame.jpg", image)
            


    def New(self):
        self.widget.clear()
        self.pushButton.show()
        self.label_6.show()
        self.pushButton_3.show()
        self.pushButton_2.hide()
        self.widget_2.clear()
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setChecked(False)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setAutoExclusive(False)
        self.radioButton_5.setChecked(False)
        self.pushButton_4.hide()




    def method(self, checked):
        query = FeatureExtractor(cv2.imread(imagepath))
        # self.widget_4.show()
        if checked.text() == "Mean RGB":
            if checked.isChecked() == True:
                c = query.mean_color()
                
                mycursor.execute("SELECT MeanColor, Path FROM ImagesDB")
                obj = Evaluation()
                # fetch all the matching rows 
                result = mycursor.fetchall()
                i=1  
                # print(result[0][0])
                for pic in result:
                    arr = pickle.loads(pic[0])
                    error = obj.meanColorDifference(c,arr)
                    
                    i+=1
                    if error <= 100:
                        pixmap = QPixmap(pic[1])
                        icon = QtGui.QIcon(pic[1])
                        self.widget_2.setIconSize(QtCore.QSize(self.widget_2.width(),self.widget_2.height()))
                        item = QtWidgets.QListWidgetItem(icon, '.')
                        self.widget_2.addItem(item)
                        
        if checked.text() == "Histogram":
            if checked.isChecked() == True:
                
                c = query.Histogram()
                mycursor.execute("SELECT Histogram, Path FROM ImagesDB")
                obj = Evaluation()
                # fetch all the matching rows 
                result = mycursor.fetchall()
                 
                # print(result[0][0])
                for pic in result:
                    arr = pickle.loads(pic[0])
                    error = obj.HistogramNormalizedDifference(c,arr,cv2.imread(pic[1]))
                    # print(i)
                    # print(error)
                    
                    if error >= 4.2e-06:
                        pixmap = QPixmap(pic[1])
                        icon = QtGui.QIcon(pic[1])
                        self.widget_2.setIconSize(QtCore.QSize(self.widget_2.width(),self.widget_2.height()))
                        item = QtWidgets.QListWidgetItem(icon, '.')
                        self.widget_2.addItem(item)
            # self.widget_4.hide()
                
        if checked.text() == "Color Layout":
            if checked.isChecked() == True:
                c = query.ColorLayout()
                mycursor.execute("SELECT ColorLayout, Path FROM ImagesDB")
                obj = Evaluation()
                # fetch all the matching rows 
                result = mycursor.fetchall()
                i=1  
                # print(result[0][0])
                for pic in result:
                    arr = pickle.loads(pic[0])
                    error = obj.colorLayoutDifference(c,arr)
                    # print(i)
                    # print(error)
                    i+=1
                    if error >= 1e-06:
                        pixmap = QPixmap(pic[1])
                        icon = QtGui.QIcon(pic[1])
                        self.widget_2.setIconSize(QtCore.QSize(self.widget_2.width(),self.widget_2.height()))
                        item = QtWidgets.QListWidgetItem(icon, '.')
                        self.widget_2.addItem(item)
                        
        if checked.text() == "Dominant Color":
            if checked.isChecked() == True:
                c = query.Dominant_color()
                
                mycursor.execute("SELECT MeanColor2, Path FROM ImagesDB")
                obj = Evaluation()
                # fetch all the matching rows 
                result = mycursor.fetchall()
                i=1  
                # print(result[0][0])
                for pic in result:
                    arr = pickle.loads(pic[0])
                    error = obj.compare(c,arr,cv2.imread(pic[1]))
                    
                    i+=1
                    if error >= 7e-9:
                        pixmap = QPixmap(pic[1])
                        icon = QtGui.QIcon(pic[1])
                        self.widget_2.setIconSize(QtCore.QSize(self.widget_2.width(),self.widget_2.height()))
                        item = QtWidgets.QListWidgetItem(icon, '.')
                        self.widget_2.addItem(item)
                
        if checked.text() == "Video Histogram":
            if checked.isChecked() == True:
                video_path = r'./videos/'
                # dir = r'./test/'  #to be changed to /video
                dir = os.path.dirname(videoname) + '/'
                # rec = ['good_fish.MP4','good_ear.mp4','airplane.mp4','bad_dog.MP4','beach.mp4','dog.mp4']
                # own = rec[5]

                f = FeatureExtractor()
                e= Evaluation()
                video = os.path.basename(videoname)
                print('video path', dir)
                print('video name', video)
                results,b2,g2,r2 = f.test_video(dir, video)
                res , vid = e.retrieve_video(results,b2,g2,r2,video)
                out = []
                for e in res:
                    out.append(e[0])
                for word in out:
                    list_item = QtWidgets.QListWidgetItem(word, self.widget_2)
                    list_item.setForeground(QtGui.QColor('white'))
                
    #omar
    def item_click(self):
        clickedItem =self.widget_2.currentItem().text()
        # clickedItem = clickedItem.lower()
        file = os.path.join(os.path.dirname(__file__)+'\\videos', clickedItem)
        print(file)
        os.system(file)
                
def suppress_qt_warnings():
        environ["QT_DEVICE_PIXEL_RATIO"] = "0"
        environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        environ["QT_SCREEN_SCALE_FACTORS"] = "1"
        environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())