#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Ex6.1.py
# @Author: 白冬鑫
# @Date  : 2020/1/11
# @Desc  : Ex6.1.py 用途：
# @license : Copyright(C), 中南大学 and 致力科技
# @Contact : baidongxin07@csu.edu.cn; baidongxin07@gmail.com


import numpy as np
from numpy.linalg import solve
from matplotlib import pyplot as plt


if __name__ == '__main__':
    a = 1
    N = 20
    dx = a / N
    np.zeros()

    K = np.zeros((N + 1, N + 1))
    K[0, 0] = 1
    K[-1, -1] = 1
    for ii in range(1, N):
        K[ii, ii - 1] = 1 / dx ** 2
        K[ii, ii] = -2 / dx ** 2
        K[ii, ii + 1] = 1 / dx ** 2

    P = np.ones((N + 1, 1))
    P[0] = 0
    P[-1] = 0

    u = solve(K, P)

    x = np.linspace(0, a, N + 1)
    u_a = 0.5 * x ** 2 - 0.5 * x

    plt.plot(x, u, 'o-', label='numerical solution')
    plt.plot(x, u_a, 'p-.', label='analytical solution')
    plt.grid()
    plt.legend()
    plt.show()
