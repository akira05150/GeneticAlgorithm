import playground
import rbfn2
import Car
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import sys
import demo_ui
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")


class myMainWindow(QMainWindow, demo_ui.Ui_MainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
         self.setWindowTitle("111522083 徐嘉彤")
         self.setup_control()

         self.canvas = Figure_Canvas()
         self.canvas.ground()
         c = Car.Car()
         circle = plt.Circle( (0, 0), c.radius, color='orange', fill=False)
         self.canvas.axes.add_patch(circle)

         self.timer = QTimer(self)
         self.timer.timeout.connect(self.showTime)

         self.x = []
         self.sensor = []

         graphicscene = QtWidgets.QGraphicsScene()
         graphicscene.addWidget(self.canvas)
         self.gv_ground.setScene(graphicscene)
         self.gv_ground.show()
    
    # 每個時刻的sensor與車子位置
    def showTime(self):
        for i in range(len(self.x)):
            self.lb_dis_front.setText(str(np.round(self.sensor[i][0], 7)))
            self.lb_dis_right.setText(str(np.round(self.sensor[i][1], 7)))
            self.lb_dis_left.setText(str(np.round(self.sensor[i][2], 7)))

            self.canvas.axes.add_patch(self.x[i])
            self.canvas.draw()
            self.canvas.flush_events()
        self.endTimer()
            
    # 取得車子位置與sensor資料
    def getdata(self):
        path = self.lb_filename.text()
        k = int(self.edt_k.text())
        epoch = int(self.edt_epoch.text())
        lr = float(self.edt_lr.text())

        datasets = rbfn2.read_data(path)
        d = np.array(datasets[:, -1], copy=True)

        if path == r'train4dAll.txt':

            w, m, sigma = rbfn2.train(datasets, k, epoch, lr)

            # 存成紀錄檔
            car = Car.Car()
            with open('train4D.txt', 'w') as f:
                for i in range(len(d)):
                    if car.isCollision():
                        break
                    sensor_dis = car.get_sensor_distance()
                    output = rbfn2.rbf(w, m, sigma, sensor_dis, d)
                    print(output)
                    car.move_car(output)
                    circle = plt.Circle(
                        (car.position[0], car.position[1]), car.radius, color='orange', fill=False)
                    self.x.append(circle)
                    self.sensor.append(sensor_dis)
                    f.write("{:.7f}".format(sensor_dis[0])+' ')
                    f.write("{:.7f}".format(sensor_dis[1])+' ')
                    f.write("{:.7f}".format(sensor_dis[2])+' ')
                    f.write("{:.7f}".format(output) + '\n')



        elif path == r'train6dAll.txt':
            w, m, sigma = rbfn2.train(datasets, k, epoch, lr)

            # 存成紀錄檔
            car = Car.Car()
            with open('train6D.txt', 'w') as f:
                for i in range(len(d)):
                    if car.isCollision():
                        break
                    sensor_dis = car.get_sensor_distance()
                    x, y = car.get_position()
                    sensor_dis = np.insert(sensor_dis, 0, x)
                    sensor_dis = np.insert(sensor_dis, 1, y)
                    output = rbfn2.rbf(w, m, sigma, sensor_dis, d)
                    car.move_car(output)
                    circle = plt.Circle(
                        (car.position[0], car.position[1]), car.radius, color='orange', fill=False)
                    self.x.append(circle)
                    self.sensor.append(sensor_dis)

                    f.write("{:.7f}".format(sensor_dis[0])+' ')
                    f.write("{:.7f}".format(sensor_dis[1])+' ')
                    f.write("{:.7f}".format(sensor_dis[2])+' ')
                    f.write("{:.7f}".format(sensor_dis[3])+' ')
                    f.write("{:.7f}".format(sensor_dis[4])+' ')
                    f.write("{:.7f}".format(output) + '\n')

        elif path == r'track4D.txt':
            # 讀取記錄檔顯示圖表
            car = Car.Car()
            # car.draw_car(self.canvas.axes)  # 初始車
            track = rbfn2.read_data('track4D.txt')
            output_angle = np.array(track[:, -1], copy=True)
            for i in range(len(track)):
                if car.isCollision():
                    break
                car.move_car(output_angle[i])
                circle = plt.Circle(
                    (car.position[0], car.position[1]), car.radius, color='orange', fill=False)
                self.x.append(circle)
                self.sensor.append(track[i][0:-1])


        elif path == r'track6D.txt':
            # 讀取記錄檔顯示圖表
            car = Car.Car()
            # car.draw_car(self.axes)  # 初始車
            track = rbfn2.read_data('track6D.txt')
            output_angle = np.array(track[:, -1], copy=True)
            for i in range(len(track)):
                if car.isCollision():
                    break
                car.move_car(output_angle[i])
                circle = plt.Circle(
                    (car.position[0], car.position[1]), car.radius, color='orange', fill=False)
                self.x.append(circle)
                self.sensor.append(track[i][0:-1])

    def startTimer(self):
        self.initial_fig()
        self.getdata()
        self.timer.start(1000)

    def endTimer(self):
        self.timer.stop()
        self.x = []
        self.sensor = []
    
    def initial_fig(self):
        self.canvas.axes.cla()
        self.canvas.ground()
        c = Car.Car()
        circle = plt.Circle((0, 0), c.radius, color='orange', fill=False)
        self.canvas.axes.add_patch(circle)

    # 加上函式連結元件
    def setup_control(self):
        self.btn_file.clicked.connect(self.open_file)
        self.btn_start.clicked.connect(self.startTimer)

    # 開啟資料夾選擇檔案路徑
    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Open file",
                                                         "./",filter='TXT (*.txt)')
                                                         
        if filename:
            print(filename, filetype)
            f = filename.rfind('/')
            self.lb_filename.setText(filename[f+1:])
        else:
            pass
    
# matplotlib在pyqt上畫圖
class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=7, height=7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.axes = self.fig.add_subplot()
        self.axes.axis('equal')

    def ground(self):
        playground.draw_ground(self.axes)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = myMainWindow()
    window.show()
    sys.exit(app.exec_())
