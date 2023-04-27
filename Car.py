import numpy as np
import math
from sympy import Point, Segment, Ray, Circle, intersection


class Car:
    def __init__(self):
        self.radius = 3.0
        self.diameter = 6.0
        self.position = np.array([0., 0.])

        self.angle = 90.0
        self.angle_min = -90.0
        self.angle_max = 270.0

        self.wheel_angle = 0.0
        self.wheel_angle_min = -40.0
        self.wheel_angle_max = 40.0

    def get_position(self):
        return self.position

    def get_r(self):
        return self.radius

    # 感測器在圓心
    def get_sensor_position(self):
        sensor_front = self.position + np.array([self.radius*math.cos(math.radians(self.angle)),
                                                 self.radius*math.sin(math.radians(self.angle))])
        sensor_left = self.position + np.array([self.radius*math.cos(math.radians(self.angle+45)),
                                                self.radius*math.sin(math.radians(self.angle+45))])
        sensor_right = self.position + np.array([self.radius*math.cos(math.radians(self.angle-45)),
                                                 self.radius*math.sin(math.radians(self.angle-45))])
        # print("sensor:", sensor_front, sensor_left, sensor_right)
        return sensor_front, sensor_left, sensor_right
    
    def get_sensor_distance(self):
        # 圓心和感測器的連線 相交於 邊界上的第一個交點 與感測器的距離 ||p交點-p圓心||
        # 圓心與sensor
        front, left, right = self.get_sensor_position()
        center = self.get_position()
        pc, pf, pl, pr = Point(center[0], center[1]), Point(
            front[0], front[1]), Point(left[0], left[1]), Point(right[0], right[1])

        # 圓心與感測器連線
        line_front = Ray(pc, pf)
        line_left = Ray(pc, pl)
        line_right = Ray(pc, pr)

        # 邊界
        blines = BorderLine().getLines()
        dis_f, dis_l, dis_r = [], [], []
        # 計算交點與距離 ||p交點-p圓心||
        for line in blines:
            cross_pf = line_front.intersection(line)
            cross_pl = line_left.intersection(line)
            cross_pr = line_right.intersection(line)

            if(cross_pf != []):
                df = pc.distance(cross_pf[0])
                dis_f.append(df.evalf())

            if(cross_pl != []):
                dl = pc.distance(cross_pl[0])
                dis_l.append(dl.evalf())

            if(cross_pr != []):
                dr = pc.distance(cross_pr[0])
                dis_r.append(dr.evalf())

        # 取最小距離(第一個碰撞到的邊界)
        dis_front = float(min(dis_f))
        dis_left = float(min(dis_l))
        dis_right = float(min(dis_r))
        sensor_dis = np.array([dis_front, dis_right, dis_left])
        return sensor_dis

    # x座標移動
    def move_x(self, theta):
        # 這裡theta是 wheel angle
        self.position[0] = self.position[0] + math.cos(math.radians(
            self.angle+theta)) + math.sin(math.radians(theta))*math.sin(math.radians(self.angle))
        return self.position[0]

    # y座標移動
    def move_y(self, theta):
        self.position[1] = self.position[1] + math.sin(math.radians(
            self.angle+theta)) - math.sin(math.radians(theta))*math.cos(math.radians(self.angle))
        return self.position[1]

    # 車子與水平軸夾角
    def change_angle(self, theta):
        self.angle = self.angle - \
            math.degrees(
                math.asin((2*math.sin(math.radians(theta))/self.diameter)))
        # angle限制
        if self.angle > self.angle_max:
            self.angle = self.angle - 360
        elif self.angle < self.angle_min:
            self.angle = self.angle + 360
        return self.angle

    # 方向盤角度
    def get_wheel_angle(self, theta):
        if theta > self.wheel_angle_max:
            self.wheel_angle = self.wheel_angle_max
        elif theta < self.wheel_angle_min:
            self.wheel_angle = self.wheel_angle_min
        else:
            self.wheel_angle = theta
        return self.wheel_angle

    # 移動車子 x, y , 水平夾角
    def move_car(self, theta):
        w_angle = self.get_wheel_angle(theta)
        self.move_x(w_angle)
        self.move_y(w_angle)
        self.change_angle(w_angle)

    def get_angle(self):
        return self.angle
    
    def isCollision(self):
      endLine = Segment((18, 40), (30, 37))
      center = self.get_position()
      pc = Point(center[0], center[1])

      # 所有邊界
      blines = BorderLine().getLines()
      blines.append(endLine)

      # 車
      c = Circle(pc, self.radius)
      for line in blines:
          cross_p = intersection(line, c)
          if cross_p != []:
            print("collide")
            return True
      return False

# 場地邊界線
class BorderLine():
    def __init__(self):
        self.l1 = Segment((-6, 0), (-6, 22))
        self.l2 = Segment((6, 0), (6, 10))
        self.l3 = Segment((18, 22), (18, 50))
        self.l4 = Segment((30, 10), (30, 50))
        self.l5 = Segment((6, 10), (30, 10))
        self.l6 = Segment((-6, 22), (18, 22))
        self.l7 = Segment((18, 50), (30, 50))

    def getLines(self):
        l_collection = [self.l1, self.l2, self.l3,
                        self.l4, self.l5, self.l6, self.l7]
        return l_collection
