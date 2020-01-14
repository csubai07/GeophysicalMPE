#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : EX6.7.py
# @Author: 白冬鑫
# @Date  : 2020/1/14
# @Desc  : EX6.7.py 用途：
# @license : Copyright(C), 中南大学 and 致力科技
# @Contact : baidongxin07@csu.edu.cn; baidongxin07@gmail.com

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import solve

if __name__ == '__main__':
    L = 1
    T = 2
    a = 1
    M = 200

    dt = T / M
    N = 10
    dx = L / N
    alpha = a * a * dt * dt / (dx * dx)

    # 初始条件
    x = []
    u = np.zeros((N + 1, M + 1))
    for xi in range(N + 1):
        x.append(xi * dx)
        u[xi, 0] = np.sin(np.pi * xi * dx)
        u[xi, 1] = u[xi, 0] + dt * 0

    # 向前差分
    time = [0, dt]
    for k in range(2, M + 1):
        u[0, k] = 0
        u[-1, k] = 0
        for i in range(1, N):
            u[i, k] = alpha * u[i - 1, k - 1] + (2 - 2 * alpha) * u[i, k - 1] + alpha * u[i + 1, k - 1] - u[i, k - 2]
        time.append(k * dt)

    X, Y = np.meshgrid(x, time)

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.contourf(X, Y, u.T, cmap=plt.get_cmap('rainbow'))
    ax1.set_xlabel("x")
    ax1.set_ylabel("t")

    ax2 = fig.add_subplot(122, projection='3d')
    ax2.plot_surface(X, Y, u.T, cmap=plt.get_cmap('rainbow'))
    ax2.set_xlabel("x")
    ax2.set_ylabel("t")

    plt.show()
    pass
