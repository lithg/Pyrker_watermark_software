# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lithg\Desktop\Development\Python\pyrker.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PIL import Image
import time
import os
import threading



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 405)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.btn_logo = QtWidgets.QPushButton(Dialog)
        self.btn_logo.setGeometry(QtCore.QRect(110, 30, 180, 60))
        self.btn_logo.setStyleSheet("font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 8px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        self.btn_logo.setObjectName("btn_logo")
        self.btn_dir = QtWidgets.QPushButton(Dialog)
        self.btn_dir.setGeometry(QtCore.QRect(110, 130, 180, 60))
        self.btn_dir.setStyleSheet("font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 8px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        self.btn_dir.setObjectName("btn_dir")
        self.btn_start = QtWidgets.QPushButton(Dialog)
        self.btn_start.setGeometry(QtCore.QRect(110, 250, 180, 60))
        self.btn_start.setStyleSheet("font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 1px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        self.btn_start.setObjectName("btn_start")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(115, 330, 180, 30))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)

        self.lbl_data = QtWidgets.QLabel(Dialog)
        self.lbl_data.setGeometry(QtCore.QRect(80, 5, 400, 20))
        self.lbl_data.setObjectName("lbl_data")
        self.lbl_data.setStyleSheet('font-size: 10pt; font-family: Courier;')

        self.lbl_hora = QtWidgets.QLabel(Dialog)
        self.lbl_hora.setGeometry(QtCore.QRect(280, 5, 400, 20))
        self.lbl_hora.setObjectName("lbl_hora")
        self.lbl_hora.setStyleSheet('font-size: 10pt; font-family: Courier;')



        self.lbl_logo = QtWidgets.QLabel(Dialog)
        self.lbl_logo.setGeometry(QtCore.QRect(170, 90, 131, 16))
        self.lbl_logo.setObjectName("lbl_logo")
        self.lbl_dir = QtWidgets.QLabel(Dialog)
        self.lbl_dir.setGeometry(QtCore.QRect(150, 190, 400, 16))
        self.lbl_dir.setObjectName("lbl_dir")
        self.lbl_done = QtWidgets.QLabel(Dialog)
        self.lbl_done.setGeometry(QtCore.QRect(160, 340, 150, 80))
        self.lbl_done.setObjectName("lbl_done")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_logo.clicked.connect(self.openLogo)
        self.btn_dir.clicked.connect(self.openPath)
        self.btn_start.clicked.connect(self.start2)


        t1 = threading.Thread(target=self.showTime)
        #t1.start()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pyrker Watermark Helper"))
        self.btn_logo.setText(_translate("Dialog", "Load Logo"))
        self.btn_dir.setText(_translate("Dialog", "Choose Directory"))
        self.btn_start.setText(_translate("Dialog", "START"))
        self.lbl_logo.setText(_translate("Dialog", "example.png"))
        self.lbl_dir.setText(_translate("Dialog", "C:\Example\Images\Path"))
        self.lbl_done.setText(_translate("Dialog", ""))


    def showTime(self):
        while True:
            data = time.strftime("[%A] %d/%m/%Y")
            hora = time.strftime("%H:%M:%S")
            self.lbl_data.setText(data)
            self.lbl_hora.setText(hora)



    def openLogo(self):

        global fileName
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"Select the logo file", "","JPEG/PNG (*.jpg *.jpeg *.png)" , options=options)
        if fileName:
            print(fileName)
            self.lbl_logo.setText(os.path.basename(fileName))


    def openPath(self):

        global input_dir
        input_dir = QFileDialog.getExistingDirectory(None, 'Select the images path')
        if input_dir:
            print(input_dir)
            self.lbl_dir.setText(input_dir)


    def start2(self):

        try:

            self.completed = 0
            path = input_dir
            for images in os.listdir(path):
                progress_length = 100 / len(images)

                if images.endswith('.png') or images.endswith('.jpg'):


                    bg = Image.open(os.path.join(path, images))

                    logo = Image.open(fileName)

                    transp = logo.convert('L').point(lambda x: min(x, 500))
                    logo.putalpha(transp)

                    bg.paste(logo, (0, 0), logo)
                    #bg.save(os.path.join(path, images), 'PNG', quality=100) # overwrite original images
                    bg.save(os.path.join(path, 'new_' + images), 'PNG', quality=100)

                self.completed += progress_length
                self.progressBar.setValue(self.completed)

            self.lbl_done.setStyleSheet('font-size: 18pt; font-family: Courier; color: green')
            self.lbl_done.setText('Done!')
            self.progressBar.setValue(100)


        except:
            self.lbl_done.setStyleSheet('color: red')
            self.lbl_done.setText('Error! No image found!')




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())







