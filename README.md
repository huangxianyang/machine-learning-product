## 项目说明
- 一个完整的二分类机器学习项目生产环境部署,包括接收请求原始变量入参,<br> 
    参数检测, 数据预处理, 模型变量构造, 模型预测, 数据库操作, 返回结果.
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
<br> 安装包: /root/Anaconda3-2019.03-Linux-x86_64.sh
<br> 安装: bash Anaconda3-2019.03-Linux-x86_64.sh 
3. 安装依赖
<br> 依赖文件: /root/mlModel/requirements.txt
<br> 安装: pip install -r requirements.txt
#### step2: 启动/关闭服务
1. 启动服务命令: bash start.sh
2. 关闭服务命令: bash stop.sh