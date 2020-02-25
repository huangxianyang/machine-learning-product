# -*- coding: utf-8 -*-
# @Time    : 2020-02-22 21:53
# @Author  : HuangSir
# @FileName: featurelist.py
# @Software: PyCharm
# @Description:入模变量

# 请求参数
origin_feature = [
    'old_customer', # 是老客: 1, 不是老客: 0
    'debt_amount', # 共债金额
    'debt_number', # 共债平台数
    'recent24hours_apply', # 近24小时申请平台数
    'recent7days_apply', # 近7天申请平台数
    'recent30days_apply', # 近30天申请平台数
    'debt_level', # 负债水平, NO_HIT, SLIGHT, GENERAL, SERIOUS,DANGER
    'education', # 学历
    'iswhatsapp', # 是否开通whatsapp, yes, no
    'whatsapp_avatar', # 是否有whatsapp头像, yes, no
    'whatsapp_company_account', # whatsapp账户是否为企业账户, yes, no
    'idinquiriesuname_21d', # 近21天申请平台数
    'idinquiriesuname_30d', # 近30天申请平台数
    'topup_360_720_max', # 上一年最大一笔话费充值金额
    'topup_360_720_avg', # 上一年平均每笔话费充值金额
    'topup_0_360_min', # 近一年话费最小一笔充值金额
    'topup_180_360_avg', # 上半年话费平均每笔充值金额
    'preference_bank_60d', # 近60天金融类APP访问次数
    'A_II_360d', # 近一年身份证下借款平台数
    'A_PI_360d' # 近1年该电话号码下借款平台数
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
