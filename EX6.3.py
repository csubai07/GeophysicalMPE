#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : EX6.3.py
# @Author: 白冬鑫
# @Date  : 2020/1/13
# @Desc  : EX6.3.py 用途：
# @license : Copyright(C), 中南大学 and 致力科技
# @Contact : baidongxin07@csu.edu.cn; baidongxin07@gmail.com
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve
import copy


def direct_solution():
    a = 20
    b = 10
    N = 40
    M = 20
    dx = a / N
    dy = b / M
    L = np.zeros(((N + 1) * (M + 1), (N + 1) * (M + 1)))
    R = np.zeros(((N + 1) * (M + 1), 1))

    for i in range(M + 1):
        for j in range(N + 1):
            k = (j - 1) * (M + 1) + i
            if i == 0 or i == M or j == 0 or j == N:
                L[k, k] = 1
                R[k, 0] = 0
            else:
                L[k, k - (M + 1)] = 1 / (dy * dy)
                L[k, k - 1] = 1 / (dx * dx)
                L[k, k] = -2 / (dx * dx) - 2 / (dy * dy)
                L[k, k + 1] = 1 / (dx * dx)
                L[k, k + (M + 1)] = 1 / (dy * dy)
                R[k, 0] = 1

    u = solve(L, R)
    u1 = np.reshape(u, (N + 1, M + 1))
    # plt.imshow(u1, cmap='jet', interpolation='gaussian')
    # plt.colorbar()
    # plt.show()

    return u1


def gauss_seidel_solution():
    a = 20
    b = 10
    N = 40
    M = 20
    dx = a / N
    dy = b / M

    A = 1 / (dx * dx)
    B = 1 / (dy * dy)
    K = 2 * A + 2 * B

    u = np.zeros((N + 1, M + 1))
    u1 = copy.deepcopy(u)

    err = np.zeros((N + 1, M + 1))
    err[1:err.shape[0]-1,1:err.shape[1]-1] = 1
    while np.mean(err) > 1e-6:
        for i in range(1, N ):
            for j in range(1, M):

                u1[i, j] = (A * u[i + 1, j] + B * u[i, j + 1] + A * u1[i - 1, j] + B * u1[i, j - 1]-1) / K
                err[i, j] =np.abs(u1[i, j] - u[i, j])
        u =copy.deepcopy(u1)
        print("err=%.8f"% np.mean(err))

    # plt.imshow(u1, cmap='jet', interpolation='gaussian')
    # plt.colorbar()
    # plt.show()

    return u1


def method_comparison():
    u1 = direct_solution()
    u2 = gauss_seidel_solution()
    ax1 =plt.subplot(121)

    plt.imshow(u1, cmap='jet', interpolation='gaussian')
    plt.colorbar(ax=ax1)

    ax2 = plt.subplot(122)
    plt.imshow(u2, cmap='jet', interpolation='gaussian')
    plt.colorbar(ax=ax2)

    plt.show()

if __name__ == '__main__':
    # gauss_seidel_solution()
    # direct_solution()
    method_comparison()

