# -*- coding: utf-8 -*-
# @Time    : 2020-02-23 16:08
# @Author  : HuangSir
# @FileName: lgbpredict.py
# @Software: PyCharm
# @Description: 模型预测
import sys
sys.path.append('..')

import joblib
catMap = joblib.load('../general_model/data/category_map.pkl')
lgb = joblib.load('../general_model/data/lgbModel.pkl')
lr = joblib.load('../general_model/data/lrModel.pkl')
import numpy as np

from general_model.model.preprocess import Prepro
from general_model.data.featurelist import *
from util.modelUtil import Prob2Score

class Model(object):
    """模型预测"""
    def __init__(self,data:dict):
        self.__data = data

    def cat_map(self):
        data = Prepro(data=self.__data).derivative()
        # print('衍生变量结果:',data)
        for col in cat_feature:
            # 数值化分类特征
            if col != 'old_customer': # 首复借无缺失
                data[col] = catMap[col].get(data[col],-99)
            else:
                data[col] = catMap[col][float(data[col])]
        # 获取模型特征集
        mData = {}
        for k in lgb.feature_name():
            mData[k] = data[k]
        return mData

    def lgb_lr(self):
        data = self.cat_map()
        X = np.array(list(data.values())).reshape(1, -1)
        data['lgb_prob'] = float(lgb.predict(data=X, num_iteration=lgb.best_iteration)[0])
        data['lr_prob'] = float(lr.predict_proba(X=np.array(data['lgb_prob']).reshape(1,-1))[:,1][0])
        return data

    def predict(self):
        data = self.lgb_lr()
        data['ml_score'] =  Prob2Score(prob=data['lr_prob'])
        return data
