# -*- coding: utf-8 -*-
# @Time    : 2020-02-23 17:05
# @Author  : HuangSir
# @FileName: modelUtil.py
# @Software: PyCharm
# @Description:
import sys
sys.path.append('..')
from util.PropertiesUtil import Properties
import numpy as np
bp = Properties('../resources/model.properties').getProperties()
basePoint = float(bp.get('basePoint'))
PDO = float(bp.get('PDO'))

def Prob2Score(prob, basePoint=basePoint,PDO=PDO):
    # 将概率转化成分数且为正整数
    y = np.log(prob/(1-prob))
    y2 = basePoint+PDO/np.log(2)*(-y)
    score = int(y2)
    return score