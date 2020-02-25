# -*- coding: utf-8 -*-
# @Time    : 2020-02-22 18:12
# @Author  : HuangSir
# @FileName: preprocess.py
# @Software: PyCharm
# @Description: # 数据预处理
import sys
sys.path.append('..')

from general_model.data.featurelist import *
import util.preUtils as  preU

mapDict = {
    'month_income': {
        'BELOW_2M': 0,
        'BETWEEN_2M_4M': 1,
        'BETWEEN_4M_8M': 2,
        'OVER_8M': 3
    },
    'debt_level': {
        'NO_HIT': 0,  # 无
        'SLIGHT': 1,  # 轻微
        'GENERAL': 2,  # 一般
        'SERIOUS': 3,  # 严重
        'DANGER': 4  # 危险
    },
    'identity_gender': {
        'PEREMPUAN': '男',
        'LAKI-LAKI': '女'
    },
    'target': {
        '逾期': 1,
        '已还清': 0,
        '还款成功': 0
    }
}

class Prepro(object):
    def __init__(self,data:dict):
        self.__data = data

    def getvalue(self):
        """获取变量值并转化类型"""
        data = {}
        for col in self.__data.keys():
            if col in cat_feature:
                data[col] = preU.str2mat(self.__data[col])
            elif col == 'debt_level':
                data[col] = mapDict['debt_level'].get(self.__data[col], -99) # 负债程度映射
            else:
                data[col] = float(self.__data[col])
        return data

    def derivative(self):
        """衍生变量构造"""
        d = self.getvalue()
        d['recent7days_refuse_num'] = preU.featureSub(a=d['recent7days_apply'],b=d['debt_number'])
        d['avg_debt_amount'] = preU.featureDiv(a=d['debt_amount'],b=d['debt_number'])/100
        d['recent7days_debt__weight'] = preU.featureDiv(a=d['recent7days_apply'],b=d['debt_number'])
        d['recent30days_refuse_num'] = preU.featureSub(a=d['recent30days_apply'],b=d['debt_number'])
        d['recent24hours_debt_weight'] = preU.featureDiv(a=d['recent24hours_apply'],b=d['debt_number'])
        return d
