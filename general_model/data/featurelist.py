# -*- coding: utf-8 -*-
# @Time    : 2020-02-22 21:53
# @Author  : HuangSir
# @FileName: featurelist.py
# @Software: PyCharm
# @Description:入模变量

# 请求参数
origin_feature = [
    'old_customer',
    'debt_amount',
    'debt_number',
    'recent24hours_apply',
    'recent7days_apply',
    'recent30days_apply',
    'debt_level',
    'education',
    'iswhatsapp',
    'whatsapp_avatar',
    'whatsapp_company_account',
    'idinquiriesuname_21d',
    'idinquiriesuname_30d',
    'topup_360_720_max',
    'topup_360_720_avg',
    'topup_0_360_min',
    'topup_180_360_avg',
    'preference_bank_60d',
    'A_II_360d',
    'A_PI_360d'
]

cat_feature = ['old_customer','education','iswhatsapp','whatsapp_avatar','whatsapp_company_account']

# 模型参数
model_feature = [
    'recent7days_refuse_num', # recent7days_apply - debt_number
    'avg_debt_amount', # debt_amount / debt_number
    'education',
    'preference_bank_60d',
    'recent7days_apply',
    'idinquiriesuname_21d',
    'idinquiriesuname_30d',
    'recent7days_debt__weight', # recent7days_apply / debt_number
    'debt_number',
    'topup_0_360_min',
    'debt_level',
    'old_customer',
    'A_II_360d',
    'recent30days_apply',
    'recent24hours_apply',
    'iswhatsapp',
    'whatsapp_avatar',
    'recent30days_refuse_num', # recent30days_apply - debt_number
    'topup_360_720_max',
    'A_PI_360d',
    'topup_360_720_avg',
    'topup_180_360_avg',
    'recent24hours_debt_weight', # recent24hours_apply / debt_number
    'debt_amount',
    'whatsapp_company_account'
]