#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Ex6.5.py
# @Author: 白冬鑫
# @Date  : 2020/1/13
# @Desc  : Ex6.5.py 用途：
# @license : Copyright(C), 中南大学 and 致力科技
# @Contact : baidongxin07@csu.edu.cn; baidongxin07@gmail.com

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import solve


def explicit_solution():
    L = 1
    T = 1
    M = 2500
    dt = T / M
    N = 50
    dx = L / N
    alpha = 0.25 * dt / (dx * dx)

    u = np.zeros((M + 1, N + 1))
    time = [0]
    x = []
    for xi in range(N + 1):
        x.append(xi * dx)
        u[0, xi] = np.sin(np.pi * xi * dx)
    for k in range(1, M + 1):
        u[k, 0] = 0
        u[k, -1] = 0
        time.append(k * dt)

        for i in range(1, N):
            u[k, i] = u[k - 1, i] + alpha * (u[k - 1, i + 1] - 2 * u[k - 1, i] + u[k - 1, i - 1])

    print(u)

    X, Y = np.meshgrid(x, time)



    return X,Y,u


def implicit_method():
    L = 1
    T = 1
    M = 2500
    dt = T / M
    N = 50
    dx = L / N
    alpha = 0.25 * dt / (dx * dx)

    MM = (1 + 2 * alpha) * np.eye(N - 1, k=0) - alpha * np.eye(N - 1, k=-1) - alpha * np.eye(N - 1, k=1)

    x = []
    u = np.zeros((N + 1, 1))
    for xi in range(N + 1):
        u[xi, 0] = np.sin(xi * dx * np.pi)
        x.append(xi * dx)

    r = np.zeros((N + 1, M + 1))
    r[:, 0] = u[:, 0]
    time = [0]
    for k in range(1, M + 1):
        uu = u[1:N, 0]
        uu[0] = uu[0] + alpha * 0
        uu[-1] = uu[-1] + alpha * 0
        u1 = solve(MM, uu.T)
        u[1:N, 0] = u1.T
        r[:, k] = u[:, 0]
        time.append(k*dt)

    X,Y = np.meshgrid(x,time)

    return X,Y,r.T

def method_comparison():
    X1,Y1,u1 = explicit_solution()
    X2,Y2,u2 = implicit_method()
    # 定义figure
    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection='3d')

    ax1.plot_surface(X1, Y1, u1,  cmap=plt.get_cmap('rainbow'))
    ax1.set_xlabel("x")
    ax1.set_ylabel("time")
    ax1.set_zlabel("u")
    # plt.imshow(u,cmap='jet',interpolation='gaussian')

    ax2 = fig.add_subplot(122, projection='3d')
    ax2.plot_surface(X2,Y2,u2,  cmap=plt.get_cmap('rainbow'))
    ax2.set_xlabel("x")
    ax2.set_ylabel("time")
    ax2.set_zlabel("u")
    plt.show()

if __name__ == '__main__':
    # print(np.eye(5,k=-1))
    # implicit_method()
    method_comparison()