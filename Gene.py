class Gene:
    def __init__(self, init_m, init_sigma, init_weight):
        # weight 每群資料各點的期望輸出平均 K群 K個 10*1 +w0 = 11*1
        # m(center) 中心點 10*3
        # sigma 每群資料離群中心的平均距離 10*1
        self.weight = init_weight
        self.m = init_m
        self.sigma = init_sigma