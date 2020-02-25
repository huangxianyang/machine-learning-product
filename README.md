## 项目说明
- 一个完整的二分类机器学习项目生产环境部署,包括接收请求原始变量入参,<br> 
    参数检测, 数据预处理, 模型变量构造, 模型预测, 数据库操作, 返回结果. <br>
    
 - API入参
 ```python
 {
	"order_id":"123456789",
	"data":{
		"old_customer":"0",
    "debt_amount":"7000000",
    "debt_number":"6",
    "recent24hours_apply":"1",
    "recent7days_apply":"13",
    "recent30days_apply":"31",
    "debt_level":"GENERAL",
    "education":"S1",
    "iswhatsapp":"yes",
    "whatsapp_avatar":"yes",
    "whatsapp_company_account":"no",
    "idinquiriesuname_21d":"9",
    "idinquiriesuname_30d":"11",
    "topup_360_720_max":"100",
    "topup_360_720_avg":"32",
    "topup_0_360_min":"1",
    "topup_180_360_avg":"51",
    "preference_bank_60d":"0",
    "A_II_360d":"20",
    "A_PI_360d":"11"
	}
}
 ```
- API出参
```python
{
    "created_time": "2020-02-24 23:27:49",
    "ml_score": 768,
    "order_id": "测试订单",
    "reason": "请求成功",
    "status": 200,
    "version": "0.0.1"
}
```
***
### 文件
- __web__ &nbsp;&nbsp;web层
- __util__ &nbsp;&nbsp;通用工具
- __resources__ &nbsp;&nbsp;资源配置
- __general_model__ &nbsp;&nbsp;逻辑层
- __general_model.model__ &nbsp;&nbsp;数据预处理和模型预测
- __general_model.dao__ &nbsp;&nbsp;数据库操作
- __general_model.data__ &nbsp;&nbsp;模型文件
- __start.sh__ &nbsp;&nbsp;启动服务
- __stop.sh__ &nbsp;&nbsp;关闭服务


### 服务部署
#### step1: 环境配置
1. 系统环境: centOS7.0+或ubuntu16.0+, 4G+内存
2. 安装anaconda3
<br> 安装包: Anaconda3-2019.03-Linux-x86_64.sh
<br> 安装: bash Anaconda3-2019.03-Linux-x86_64.sh 
3. 安装依赖
<br> 依赖文件: requirements.txt
<br> 安装: pip install -r requirements.txt
#### step2: 启动/关闭服务
1. 启动服务命令: bash start.sh
2. 关闭服务命令: bash stop.sh
