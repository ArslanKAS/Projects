from PIL import Image
import os
import glob
import cv2
import sys
import numpy as np
from PyQt5.QtCore import pyqtSlot
from pip._vendor.distlib.compat import raw_input
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog


class Ui_MainWindow(object):

    def createFolder(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error: Creating directory. ' + directory)

    createFolder(self=True, directory='./R/')
    createFolder(self=True, directory='./G/')
    createFolder(self=True, directory='./B/')

    def on_click(self):
        global path
        path = filedialog.askdirectory()
        print(path)
        global user_input
        user_input = path #(path + '\*.jpg') | (path + '\*.tif') | (path + '\*.png')
        global image_list
        #image_list = []
        image_list = [Image.open(item) for i in
                      [glob.glob(path + '/*.%s' % ext) for ext in ["jpg", "png", "tif"]] for item in i]
        # for filename in glob.glob('D:\MyResearch\Band-splitter\*.jpg'):
        # for filename in glob.glob(user_input):
        #     im = Image.open(filename)
        #     image_list.append(im)

        outpath1 = './R/'
        outpath2 = './G/'
        outpath3 = './B/'

        d = 0
        for imgs in image_list:
            split = Image.Image.split(imgs)
            band_R = split[0]
            band_G = split[1]
            band_B = split[2]
            cv2.imwrite(os.path.join(outpath1, str(d) + 'R.jpg'), np.array(band_R))
            cv2.imwrite(os.path.join(outpath2, str(d) + 'G.jpg'), np.array(band_G))
            cv2.imwrite(os.path.join(outpath3, str(d) + 'B.jpg'), np.array(band_B))
            d = d + 1

        return user_input, image_list

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 461, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RGB Band Splitter"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton.clicked.connect(self.on_click)
        # button = self.pushButton('PyQt5 button', self)
        # button.setToolTip('This is an example button')
        # button.move(100, 70)
        # button.clicked.connect(self.on_click)

        # glob.

        # src_fname, ext = os.path.splitext(filename)
        # save_fnameR = os.path.join(outpath1, os.path.basename(src_fname)+'.jpg')
        # save_fnameG = os.path.join(outpath2, os.path.basename(src_fname)+'.jpg')
        # save_fnameB = os.path.join(outpath3, os.path.basename(src_fname)+'.jpg')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    # for band in split:
    #     d = d + 1
    #     cv2.imwrite(os.path.join(outpath1, str(d) + 'R.jpg'), band)
    #     #band.save(str(d) + save_fnameR)
    #     print(d)
    # [bands].save("./R/file.jpg")
    # bands.save("./R/file.jpg")
    # band.show()
    # split[0].show()
    # split[0].save("./R/file{1}.jpg".format(1,d))
    # d+1
    # split[0].show()
    # split[1].show()
    # split[2].show()
    # split[1].save(save_fnameG)
    # split[2].save(save_fnameB)

#

# im1[0].save('./R/r{:>05}.jpg')
# im1[1].save('./G/g{:>05}.jpg')
# im1[2].save('./B/b{:>05}.jpg')
#
# im1[0].show()
# im1[1].show()
# im1[2].show()
