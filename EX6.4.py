#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : EX6.4.py
# @Author: 白冬鑫
# @Date  : 2020/1/13
# @Desc  : EX6.4.py 用途：
# @license : Copyright(C), 中南大学 and 致力科技
# @Contact : baidongxin07@csu.edu.cn; baidongxin07@gmail.com

import numpy as np
import matplotlib.pyplot as plt


def func(M=44, dt=0.25):
    a = 0.2
    dx = 0.2
    # dt = 0.25
    # M = 44
    alpha = a * a * dt / (dx * dx)

    u = np.ones((M + 1, 6))
    for k in range(1, M + 1):
        u[k, 0] = 1 + dt * k
        u[k, -1] = 1 + dt * k

        for j in range(1, 5):
            u[k, j] = alpha * u[k - 1, j - 1] + (1 - 2 * alpha) * u[k - 1, j] + alpha * u[k - 1, j + 1]

    return u


if __name__ == '__main__':
    u1 = func(M=11, dt=1)
    print(u1)

    u2 = func()
    print("-------------------------------------")
    print(u2)
