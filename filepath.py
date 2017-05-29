import sys, os
import rosbag
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt4 import *
from PyQt5.QtCore import QCoreApplication

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1082, 800)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("Play rosbag")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))


class Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.openFile)

        self.le = QLineEdit(self)
        self.le.move(150,100)
        self.le.resize(350,35)

        btn=QPushButton('Button',self)
        btn.clicked.connect(self.showDialog)
        btn.resize(btn.sizeHint())
        btn.move(1, 100)

        self.ex = QPushButton('Quit',self)
        self.ex.clicked.connect(QCoreApplication.instance().quit)
        self.ex.resize(self.ex.sizeHint())
        self.ex.move(550,100)

    # FUNCTION BELOW NOT WORKING


    """def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.le.setText(str(fileName))
            bag=rosbag.Bag(fileName)
            for topic,msg,t in bag.read_messages(topics=['/kinect2/fusion/numberOfPeople']):
                print msg,t
            bag.close()
    """
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print(fname[0])
        self.le.setText(str(fname[0]))
        self.readbag(fname[0])
        """if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
       """

    def readbag(self,a):
        bag=rosbag.Bag(a)
        msg1=[]
        time=[]
        secondcount=[]
        i=0
        for topic,msg,t in bag.read_messages(topics=['/kinect2/fusion/numberOfPeople']):
            people=str(msg)
            msg1.append(people[-1])
            time.append(t.secs)

            #print msg,t

        for i in range(len(time)):
            secondcount.append(time[i]-time[0])
        #print (msg1,time,len(msg1))
        print(len(secondcount),len(msg1),secondcount,msg1,dict(zip(secondcount,msg1)))
        bag.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Widget()
    Form.show()
    sys.exit(app.exec_())
