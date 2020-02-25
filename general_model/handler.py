"""
基于Python3 Flask API
event, context 属性参考:

class Event:
    def __init__(self):
        self.body = request.get_data()
        self.headers = request.headers
        self.method = request.method
        self.query = request.args
        self.path = request.path

class Context:
    def __init__(self):
        self.hostname = os.environ['HOSTNAME']

函数返回的字典中, 支持三个数据, 分别是:
statusCode: 返回的HTTP状态码.
body: 返回的数据, 可以是字典(json)或者字符串.
"""
import sys
sys.path.append('..')

import json
from datetime import datetime
from general_model.data.featurelist import *
from general_model.dao.Dao import insertParam,insertMl
from general_model.model.lgbpredict import Model

def handle(event, context):
    """
    主函数
    """
    data = json.loads(event.body.decode()) # 入参
    version = context.version # 版本号
    result = {}
    result['order_id'] = data.get('order_id')
    result['version'] = version
    createdTime = str(datetime.now())[:19]  # 请求时间
    result['created_time'] = createdTime

    try:
        # 判断字段是否缺失或错误
        if set(data.get('data').keys()) != set(origin_feature):
            result['status'] = 202
            result['reason'] = '请求失败, 字段缺失或错误'
            return {'body':result}
    except AttributeError:
            result['status'] = 202
            result['reason'] = '请求失败, 无data参数'
            return {'body': result}
    try:
        # 入参落库
        insertParam(data)
        # 判断所有入参字段是否为-99
        if set(data.get('data').values()) == {'-99'}:
            result['ml_score'] = -99
            result['status'] = 201
            result['reason'] = '请求成功, 所有字段值均为-99'
            # 模型入库
            mlData = {**result, **{k:v for k,v in zip(model_feature, [-99]*len(model_feature))}}
            insertMl(mlData)
            return {'body':result}
        else:
            # 模型预测
            mData = Model(data=data['data']).predict()
            result['ml_score'] = mData['ml_score']
            result['status'] = 200
            result['reason'] = '请求成功'
            # 结果落库
            mlData = {**result,**mData}
            insertMl(mlData)
            return {'body':result}

    except (ValueError,KeyError):
        result['status'] = 203
        result['reason'] = '请求失败,参数值类型错误'
        return {'body': result}