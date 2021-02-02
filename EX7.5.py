#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : EX7.5.py
# @Author: 白冬鑫
# @Date  : 2020/3/1
# @Desc  : EX7.5.py 用途：
# @license : Copyright(C), 中南大学 and 致力科技
# @Contact : baidongxin07@csu.edu.cn; baidongxin07@gmail.com

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import solve

NP = 101
NE = NP - 1
L = 1
x = np.linspace(0, L, NP)
dx = x[1] - x[0]
dt = 0.01
r = 0.25
Q = 0
K = np.zeros((NP, NP))
M = np.zeros((NP, NP))
P = np.zeros((NP, 1))

u = np.zeros((NP, 1))

ke = r * np.array([[1 / dx, -1 / dx], [-1 / dx, 1 / dx]])
Pe = Q * np.array([dx / 2, dx / 2])
M_loc = np.array([[dx / 3, dx / 6], [dx / 6, dx / 3]])

ME = np.zeros((NE,2))
for i in range(NE):
    ME[i,0] = i
    ME[i,1] = i+1

