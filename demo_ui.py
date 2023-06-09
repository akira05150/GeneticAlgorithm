# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 853)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gv_ground = QtWidgets.QGraphicsView(self.centralwidget)
        self.gv_ground.setGeometry(QtCore.QRect(10, 20, 730, 780))
        self.gv_ground.setObjectName("gv_ground")
        self.btn_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_file.setGeometry(QtCore.QRect(770, 50, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.btn_file.setFont(font)
        self.btn_file.setObjectName("btn_file")
        self.lb_filename = QtWidgets.QLabel(self.centralwidget)
        self.lb_filename.setGeometry(QtCore.QRect(890, 50, 201, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lb_filename.setFont(font)
        self.lb_filename.setObjectName("lb_filename")
        self.lb_lr = QtWidgets.QLabel(self.centralwidget)
        self.lb_lr.setGeometry(QtCore.QRect(770, 140, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lb_lr.setFont(font)
        self.lb_lr.setObjectName("lb_lr")
        self.lb_epoch = QtWidgets.QLabel(self.centralwidget)
        self.lb_epoch.setGeometry(QtCore.QRect(770, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lb_epoch.setFont(font)
        self.lb_epoch.setObjectName("lb_epoch")
        self.edt_lr = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_lr.setGeometry(QtCore.QRect(950, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.edt_lr.setFont(font)
        self.edt_lr.setObjectName("edt_lr")
        self.edt_epoch = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_epoch.setGeometry(QtCore.QRect(950, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.edt_epoch.setFont(font)
        self.edt_epoch.setObjectName("edt_epoch")
        self.lb_sensor_f = QtWidgets.QLabel(self.centralwidget)
        self.lb_sensor_f.setGeometry(QtCore.QRect(770, 360, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lb_sensor_f.setFont(font)
        self.lb_sensor_f.setObjectName("lb_sensor_f")
        self.lb_sensor_r = QtWidgets.QLabel(self.centralwidget)
        self.lb_sensor_r.setGeometry(QtCore.QRect(770, 410, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lb_sensor_r.setFont(font)
        self.lb_sensor_r.setObjectName("lb_sensor_r")
        self.lb_sensor_l = QtWidgets.QLabel(self.centralwidget)
        self.lb_sensor_l.setGeometry(QtCore.QRect(770, 460, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lb_sensor_l.setFont(font)
        self.lb_sensor_l.setObjectName("lb_sensor_l")
        self.lb_dis_front = QtWidgets.QLabel(self.centralwidget)
        self.lb_dis_front.setGeometry(QtCore.QRect(940, 360, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lb_dis_front.setFont(font)
        self.lb_dis_front.setObjectName("lb_dis_front")
        self.lb_dis_right = QtWidgets.QLabel(self.centralwidget)
        self.lb_dis_right.setGeometry(QtCore.QRect(940, 410, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lb_dis_right.setFont(font)
        self.lb_dis_right.setObjectName("lb_dis_right")
        self.lb_dis_left = QtWidgets.QLabel(self.centralwidget)
        self.lb_dis_left.setGeometry(QtCore.QRect(940, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lb_dis_left.setFont(font)
        self.lb_dis_left.setObjectName("lb_dis_left")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(770, 540, 321, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.lb_epoch_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_epoch_2.setGeometry(QtCore.QRect(770, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lb_epoch_2.setFont(font)
        self.lb_epoch_2.setObjectName("lb_epoch_2")
        self.edt_k = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_k.setGeometry(QtCore.QRect(950, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.edt_k.setFont(font)
        self.edt_k.setObjectName("edt_k")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_file.setText(_translate("MainWindow", "File"))
        self.lb_filename.setText(_translate("MainWindow", "..."))
        self.lb_lr.setText(_translate("MainWindow", "Learning rate"))
        self.lb_epoch.setText(_translate("MainWindow", "epoch"))
        self.edt_lr.setText(_translate("MainWindow", "0.01"))
        self.edt_epoch.setText(_translate("MainWindow", "100"))
        self.lb_sensor_f.setText(_translate("MainWindow", "Front Sensor:"))
        self.lb_sensor_r.setText(_translate("MainWindow", "Right Sensor:"))
        self.lb_sensor_l.setText(_translate("MainWindow", "Left Sensor:"))
        self.lb_dis_front.setText(_translate("MainWindow", "..."))
        self.lb_dis_right.setText(_translate("MainWindow", "..."))
        self.lb_dis_left.setText(_translate("MainWindow", "..."))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.lb_epoch_2.setText(_translate("MainWindow", "k groups"))
        self.edt_k.setText(_translate("MainWindow", "10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
