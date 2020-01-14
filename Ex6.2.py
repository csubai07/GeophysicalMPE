#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Ex6.2.py
# @Author: 白冬鑫
# @Date  : 2020/1/13
# @Desc  : Ex6.2.py 用途：
# @license : Copyright(C), 中南大学 and 致力科技
# @Contact : baidongxin07@csu.edu.cn; baidongxin07@gmail.com

import numpy as np
import copy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    u = np.zeros((5, 4))
    u[2, 0] = 1
    u[1, 0] = 0.707
    u[3, 0] = 0.707
    u[0, 1] = 2
    u[0, 2] = 2

    u1 = copy.deepcopy(u)
    err = 10
    while err > 1e-5:
        for i in range(1, 4):
            for j in range(1, 3):
                u1[i, j] = (u[i + 1, j] + u[i, j + 1] + u1[i - 1, j] + u1[i, j - 1]) / 4
                # print(i, j, u[i, j])
        err = u1[1, 1] - u[1, 1]
        u = copy.deepcopy(u1)

    print(u)
    plt.imshow(u1, cmap='jet', interpolation='gaussian')
    plt.show()
