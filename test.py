import numpy as np
import Kmeans, rbfn2
import Gene


# a = [1, 2 , 3]
# b = a[:]
# b.append(10)
# print(a, b)
# w = np.array([1, 2, 3])
# m = np.array([1, 2, 10])
# s = np.array([1, 2, 15, 6])
# a = Gene.Gene(m, s, w)

# print(a.weight)
# print(a.m)
# print(a.sigma)

# path = r'train4dAll.txt'
# datasets = rbfn2.read_data(path)

# datasets[:, -1] = rbfn2.regularized(datasets[:, -1])

# init_m, init_sigma, init_weight = Kmeans.kmeans(10, datasets)
# init_weight = np.insert(init_weight, 0, 1)
# print(f"init_m: {init_m}\n init_sigma: {init_sigma}\n init_w: {init_weight}")
# print()

# init_m, init_sigma, init_weight = Kmeans.kmeans(10, datasets)
# init_weight = np.insert(init_weight, 0, 1)
# print(f"init_m: {init_m}\n init_sigma: {init_sigma}\n init_w: {init_weight}")
# print()

# init_m, init_sigma, init_weight = Kmeans.kmeans(10, datasets)
# init_weight = np.insert(init_weight, 0, 1)
# print(f"init_m: {init_m}\n init_sigma: {init_sigma}\n init_w: {init_weight}")
# print()


# 不同記憶體位置 不會影響
# a = np.array([1, 2, 3])
# b = np.array(a, copy=True)
# print(a, b)

# a[2] = 10
# print(a,b)