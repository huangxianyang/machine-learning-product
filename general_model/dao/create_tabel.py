# -*- coding: utf-8 -*-
# @Time    : 2020-02-22 22:36
# @Author  : HuangSir
# @FileName: create_tabel.py
# @Software: PyCharm
# @Description: 建表语句

# 原始入参表
createParam = """
    CREATE TABLE IF NOT EXISTS lgbReqData(
        id INT AUTO_INCREMENT PRIMARY KEY,
        order_id VARCHAR(255) NOT NULL,
        old_customer INT NOT NULL,
        debt_amount DECIMAL(20,2) NOT NULL,
        debt_number INT NOT NULL,
        recent24hours_apply INT NOT NULL,
        recent7days_apply INT NOT NULL,
        recent30days_apply INT NOT NULL,
        debt_level VARCHAR(255) NOT NULL,
        education VARCHAR(255) NOT NULL,
        iswhatsapp VARCHAR(20) NOT NULL,
        whatsapp_avatar VARCHAR(20) NOT NULL,
        whatsapp_company_account VARCHAR(20) NOT NULL,
        idinquiriesuname_21d INT NOT NULL,
        idinquiriesuname_30d INT NOT NULL,
        topup_360_720_max FLOAT(6,1) NOT NULL,
        topup_360_720_avg FLOAT(6,1) NOT NULL,
        topup_0_360_min FLOAT(6,1) NOT NULL,
        topup_180_360_avg FLOAT(6,1) NOT NULL,
        preference_bank_60d FLOAT(6,1) NOT NULL,
        A_II_360d INT NOT NULL,
        A_PI_360d INT NOT NULL,
        created_time DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
        created_by VARCHAR(255) NULL DEFAULT 'huangSir',
        INDEX index_order_id (order_id ASC) 
    ) CHARSET=UTF8MB4
"""

# 模型表
createMl = """
    CREATE TABLE IF NOT EXISTS lgbModel(
      id INT AUTO_INCREMENT PRIMARY KEY,
      order_id VARCHAR(255) NOT NULL,
      recent7days_refuse_num INT NOT NULL,
      avg_debt_amount INT NOT NULL ,
      education INT NOT NULL ,
      preference_bank_60d INT NOT NULL ,
      recent7days_apply INT NOT NULL ,
      idinquiriesuname_21d INT NOT NULL,
      idinquiriesuname_30d INT NOT NULL,
      recent7days_debt__weight INT NOT NULL,
      debt_number INT NOT NULL,
      topup_0_360_min INT NOT NULL,
      debt_level INT NOT NULL,
      old_customer INT NOT NULL,
      A_II_360d INT NOT NULL,
      recent30days_apply INT NOT NULL,
      recent24hours_apply  INT NOT NULL,
      iswhatsapp  INT NOT NULL,
      whatsapp_avatar  INT NOT NULL,
      recent30days_refuse_num  INT NOT NULL,
      topup_360_720_max  INT NOT NULL,
      A_PI_360d  INT NOT NULL,
      topup_360_720_avg INT NOT NULL,
      topup_180_360_avg INT NOT NULL,
      recent24hours_debt_weight INT NOT NULL,
      debt_amount INT NOT NULL,
      whatsapp_company_account INT NOT NULL,
      lgb_prob FLOAT(5,3) NOT NULL,
      lr_prob FLOAT(5,3) NOT NULL,
      ml_score INT NOT NULL,
      status INT NOT NULL,
      reason VARCHAR(255) NOT NULL,
      create_time DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
      created_by VARCHAR(255) NULL DEFAULT 'huangSir',
      INDEX index_lgbScore (order_id ASC)
    ) CHARSET=UTF8MB4
"""

# 请求参数
param = """
    INSERT INTO lgbReqData(order_id,old_customer,debt_amount,debt_number,recent24hours_apply,recent7days_apply,recent30days_apply,
                           debt_level,education,iswhatsapp,whatsapp_avatar,whatsapp_company_account,idinquiriesuname_21d,
                           idinquiriesuname_30d,topup_360_720_max,topup_360_720_avg,topup_0_360_min,topup_180_360_avg,
                           preference_bank_60d,A_II_360d,A_PI_360d)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

# 模型结果
ml = """
    INSERT INTO lgbModel(order_id,recent7days_refuse_num,avg_debt_amount,education,preference_bank_60d,recent7days_apply,
                       idinquiriesuname_21d,idinquiriesuname_30d,recent7days_debt__weight,debt_number,topup_0_360_min,
                       debt_level,old_customer,A_II_360d,recent30days_apply,recent24hours_apply,iswhatsapp,whatsapp_avatar,
                       recent30days_refuse_num,topup_360_720_max,A_PI_360d,topup_360_720_avg,topup_180_360_avg,recent24hours_debt_weight,
                       debt_amount,whatsapp_company_account,lgb_prob,lr_prob,ml_score,status,reason)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

# 创建映射表
varMap ="""
        CREATE TABLE IF NOT EXISTS mapStatus(
        id INT AUTO_INCREMENT PRIMARY KEY,
        varName VARCHAR(255) NOT NULL,
        origin VARCHAR(255) NOT NULL,
        label INT NOT NULL,
        created_time DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
        created_by VARCHAR(255) NULL DEFAULT 'huangSir'
        ) CHARSET=UTF8MB4
"""

mapw = """
    INSERT INTO mapStatus(varName,origin,label) VALUES(%s,%s,%s)
"""
