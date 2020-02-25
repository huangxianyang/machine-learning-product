# -*- coding: utf-8 -*-
# @Time    : 2020-02-22 18:21
# @Author  : HuangSir
# @FileName: preUtils.py
# @Software: PyCharm
# @Description: 数据预处理函数

from  datetime import datetime
import warnings
import numpy as np

class CrossMethod(object):
    def __init__(self):
        """"""
        self.method = {
            '-add-': self.add,
            '-sub-': self.substract,
            '-mul-': self.times,
            '-div-': self.divide,
            '-equal-': self.equal,
            '-max-': self.max,
            '-min-': self.min,
            '-mean-': self.mean,
            '-cv-': self.cv,
            '-std-': self.std
             }

    def add(self,x, y):
        return x + y

    def substract(self,x, y):
        return x - y

    def times(self,x, y):
        return x * y

    def divide(self,x, y):
        return (x + 0.001) / (y + 0.001)

    def equal(self,x, y):
        return np.equal(x, y)

    def max(self,x, y):
        return np.maximum(x, y)

    def min(self,x, y):
        return np.minimum(x, y)

    def mean(self,x, y):
        return (x + y) / 2

    def cv(self,x, y):
        std = (0.5 * (x - y) ** 2) ** 0.5
        u = (x + y)
        return std / (u + 0.001)

    def std(self,x, y):
        t = (0.5 * (x - y) ** 2) ** 0.5
        return t
    
def caculateAge(x):
    """
    计算年龄
    :param x:
    :return: age int
    """
    if x == '-99':
        return -99
    try:
        t = (datetime.today()-datetime.strptime(x,'%Y-%m-%d')).days
        t = int(t/365)
    except ValueError:
        t = -99
        warnings.warn('传值错误,默认缺失, 将年龄赋值 -99')
    return t

def featureSub(a,b):
    """特征相减"""
    if str(a) == '-99' or str(b) == '-99':
        return -99
    else:
        try:
            t = float(a) - float(b)
            if t < 0:
                return 0
            else:
                return int(t)
        except ValueError:
            warnings.warn('传入非法字符,空值处理, 默认 -99')
            return -99

def featureDiv(a,b):
    """特征相除"""
    try:
        if str(a) == '-99' or str(b) == '-99':
            return -99
        elif float(b) == 0:
            return 0
        else:
            t = float(a)*100/float(b)
            return int(t)
    except ValueError:
        warnings.warn('传入非法字符,空值处理,默认 -99')
        return -99

def zeroDebt(x):
    try:
        if float(x) == 0:
            return 1
        else:
            return 0
    except ValueError:
        warnings.warn('传入非法字符,空值处理,默认 -99')
        return -99

def str2mat(x):
    """去除空格和转大写"""
    return str(x).replace(' ','').upper()