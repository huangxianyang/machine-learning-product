# -*- coding: utf-8 -*-
# @Time    : 2020-02-23 00:03
# @Author  : HuangSir
# @FileName: Dao.py
# @Software: PyCharm
# @Description: 数据库操作
import sys
sys.path.append('..')
import re
from general_model.dao.create_tabel import *
import pymysql
from util.PropertiesUtil import Properties
from general_model.data.featurelist import model_feature

config = Properties(fileName='../resources/database.properties').getProperties()

try:
    config['port'] = int(float(config.get('port')))
except TypeError:
    print('数据库端口配置错误')


def table_exists(con,table_name):
    sql = 'show tables;'
    con.execute(sql)
    tables = [con.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if table_name in table_list:
        return True
    else:
        return False

def insertParam(data):
    """插入入参"""
    insert_feature = param.replace('\n','').replace(' ','')
    insert_feature = re.split('\(|\)',insert_feature)[1].split(',')
    insert_feature.remove('order_id') # 移除
    insert_data = []
    insert_data.append(data['order_id'])
    for i in insert_feature:
        insert_data.append(data['data'][i])
    # 数据库连接
    try:
        cnn = pymysql.connect(**config)
        try:
            with cnn.cursor() as cursor:
                if not table_exists(cursor,'lgbreqdata'):
                    cursor.execute(createParam)
                cursor.execute(param,insert_data)
                cnn.commit()
        finally:
            cnn.close()
    except pymysql.err.OperationalError:
        print('数据库连接失败')

def insertMl(data):
    """插入模型结果"""
    insert_data = []
    insert_feature = ml.replace('\n', '').replace(' ', '')
    insert_feature = re.split('\(|\)', insert_feature)[1].split(',')
    for i in insert_feature:
        # print(i,type(data[i]))
        if i in model_feature:
            insert_data.append(float(data[i]))
        else:
            insert_data.append(data[i])
    # 数据库连接
    try:
        cnn = pymysql.connect(**config)
        try:
            with cnn.cursor() as  cursor:
                if not table_exists(cursor, 'lgbmodel'):
                    cursor.execute(createMl)
                cursor.execute(ml,insert_data)
                cnn.commit()
        finally:
            cnn.close()
    except pymysql.err.OperationalError:
        print('数据库连接失败')