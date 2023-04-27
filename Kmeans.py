# !/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import random

# 歐幾里得距離
def distance(x, center):
    return np.sqrt(np.sum((x - center)**2))

# 分群
def clustering(w, data):
    # 初始化cluster
    cluster = []
    for i in range(len(w)):
        cluster.append(np.zeros(len(data[0])))

    for point in data:
        dis = distance(point[0:-1], w[0][0:-1]) # 跟第一個中心的距離
        center = 0                              # 分到第一群
        for k in range(len(w)):                 # w[k]
            new_distance = distance(point[0:-1], w[k][0:-1])
            if (new_distance < dis):
                dis = new_distance
                center = k                      # 比較近的更新為群聚中心
        # print("center:")
        # print(center)
        cluster[center] = np.insert(cluster[center], 0, point, 0)

    # reshape cluster
    for k in range(len(w)): # k群
        r = int(len(cluster[k])/len(data[0]))
        cluster[k] = np.reshape(cluster[k], (r,len(data[0])))
        cluster[k] = np.delete(cluster[k], -1, 0)
    return cluster

# 更新群心
def find_new_center(w, cluster):
    new_center = np.array(w, copy=True)
    # 計算新的中心點
    for group in range(len(cluster)):
        sum = np.zeros(len(w[0]))   # sum維度 = w[k]維度
        for point in cluster[group]:
            sum += point
        new_center[group] = sum/len(cluster[group])
    
    # 計算相差值
    e = 0.0000001
    isConvergence = False
    for i in range(len(w)):
        if distance(new_center[i], w[i]) >= e:
            # print(distance(new_center[i], w[i]))
            break
        isConvergence = True
    return new_center, isConvergence

def init_sigma(cluster, new_center):
    # 每群資料離群中心的平均距離
    sigma = np.zeros(len(new_center), dtype=float)
    for group in range(len(cluster)):
        average_dis = 0
        for point in cluster[group]:
            average_dis += distance(new_center[group], point[0:-1])
        if (len(cluster[group])==0):
            sigma[group] = average_dis/1
        else:
            sigma[group] = average_dis/len(cluster[group])
    # print(sigma)
    return sigma

def init_weight(cluster, K):
    # 每群資料各點的期望輸出平均 K群 K個
    init_w = np.zeros(K, dtype=float)
    for group in range(len(cluster)):
        expected = 0
        for point in cluster[group]:
            expected += point[-1]
        init_w[group] = expected/len(cluster[group])
    # print(init_w)
    return init_w

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

# Kmeans找初始化中心點
def kmeans(K, data):
    # 挑出初始中心點
    w = np.array(data[0:K], copy=True)
    r = random.sample(range(0,len(data)-1), K)
    for i in range(K):
        w[i] = data[r[i]]
    print("w")
    print(w)
    
    new_center = np.array(w, copy=True)

    iternums = 0
    while True:
        iternums += 1

        cluster = clustering(new_center, data)
        new_center, isConvergent = find_new_center(new_center, cluster)

        if isConvergent or iternums>200:
            print("iters:")
            print(iternums)

            new_center = np.delete(new_center, -1, 1)
            sigma = np.array([init_sigma(cluster, new_center)])
            weight = np.array([init_weight(cluster, K)])

            return new_center, sigma, weight
