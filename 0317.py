#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0317.py
# @Author: 白冬鑫
# @Date  : 2020/3/17
# @Desc  : 0317.py 用途：郑洲顺老师3月17日上课提出的问题最后的解方程程序
# @license : Copyright(C), 中南大学 and 致力科技
# @Contact : baidongxin07@csu.edu.cn; baidongxin07@gmail.com

import numpy as np
from numpy.linalg import solve
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # 初始参数
    a = 0
    b = 1
    dx = 0.002
    N = int((b - a) / dx + 1)

    # 准备矩阵
    K = np.zeros((N, N))
    K[0, 0] = 1
    K[1, 0] = -1
    K[1, 1] = 1

    for ii in range(2, N):
        K[ii, ii - 2] = 1 / dx ** 2 - 15 / dx
        K[ii, ii - 1] = 1 - 2 / dx ** 2
        K[ii, ii] = 1 / dx ** 2 + 15 / dx

    # 准备右侧向量
    B = np.zeros((N, 1))
    B[0, 0] = 0
    B[1, 0] = dx

    for ii in range(2, N):
        B[ii, 0] = (ii - 1) * dx + 1

    # 解方程组
    Y = solve(K, B)

    # 绘图
    x = [i * dx for i in range(N)]
    plt.plot(x, Y)
    plt.show()

    print(Y)
