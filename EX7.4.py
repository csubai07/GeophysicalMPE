#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : {NAME}.py
# @Author: 白冬鑫
# @Date  : {DATE}
# @Desc  : {NAME}.py 用途：
# @license : Copyright(C), 中南大学 and 致力科技
# @Contact : baidongxin07@csu.edu.cn; baidongxin07@gmail.com

from os import environ
from abaqus import *
from abaqusConstants import *
from  caeModules import mesh
from driverUtils import executeOnCaeStartup

environ['ABAQUS_BAT_PATH'] = 'D:\InstallPosition\ABAQUS\SIMULIA\Commands'
environ['ABAQUS_BAT_SETTING'] = 'noGUI'
if __name__ == '__main__':
    mymodel = mdb.Model(name="beam")
    mymodel.s

    pass