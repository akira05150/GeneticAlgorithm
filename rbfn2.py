# !/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import Kmeans

# 讀入資料集
def read_data(path):
    arrays = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            arr = line.split(' ')
            arr = list(map(float, arr))
            arrays.append(arr)
    dataset = np.array(arrays)
    return dataset

def distance(x, center):
    dis = np.sqrt(np.sum((x - center)**2, axis=1)).tolist()
    dis = np.array(dis)
    return dis

# 高斯基底函數
def gauss(x, m, sigma):
    return np.exp(-((distance(x, m)**2)/(2*(sigma**2))))

# 正規化
def regularized(d):
    d_max = max(d)
    d_min = min(d)
    return ((d-d_min)/(d_max-d_min))


def reverse_regularized(d, y):
    d_max = max(d)
    d_min = min(d)
    return y*(d_max-d_min)+d_min


def loss(d, y):
    # 期望輸出-真實輸出
    difference = (d - y)**2
    # print("diff:",difference)
    return np.sum(difference)/len(y)


def train(dataset, k, epoch, lr):
    dataset[:, -1] = regularized(dataset[:, -1])
    data_x = np.delete(dataset, -1, 1)
    data_y = dataset[:, -1]
    matrix_y = np.array(data_y, copy=True)

    init_m, init_sigma, init_weight = Kmeans.kmeans(k, dataset)
 
    init_weight = np.insert(init_weight, 0, 1)

    for ep in range(epoch):
        # 第一筆
        matrix_Fy = gauss(data_x[0], init_m, init_sigma)
        matrix_Fy = np.insert(matrix_Fy, 0, 1)
        y = matrix_Fy.dot(init_weight)
        matrix_y[0] = y

        for i in range(1, len(data_y)):
            # 更新權重
            delta_y = data_y[i-1] - y
            new_w = init_weight + lr*delta_y*matrix_Fy
            

            new_m = init_m + \
                lr*delta_y*np.array([init_weight[1:]*matrix_Fy[1:]]).T * \
                (data_x[i]-init_m)/((init_sigma**2).T)

            new_s = init_sigma + lr*delta_y * \
                np.array([init_weight[1:]*matrix_Fy[1:]]) * \
                (distance(data_x[i], init_m)**2/(init_sigma**3))

            # 準備下次迭代
            init_weight = np.array(new_w, copy=True)
            init_m = np.array(new_m, copy=True)
            init_sigma = np.array(new_s, copy=True)

            matrix_Fy = gauss(data_x[i], init_m, init_sigma)
            matrix_Fy = np.insert(matrix_Fy, 0, 1)
            y = matrix_Fy.dot(new_w)
            matrix_y[i] = y

        print("epoch:" + str(ep+1) + "  loss:" + str(loss(data_y, matrix_y)))
    return init_weight, init_m, init_sigma


def rbf(w, m, sigma, x, d):
    matrix_Fy = gauss(x, m, sigma)
    matrix_Fy = np.insert(matrix_Fy, 0, 1)
    y = matrix_Fy.dot(w)
    # 逆正規化
    output = reverse_regularized(d, y)
    return output
