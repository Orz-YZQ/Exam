# coding=utf-8
import json
import requests

#POST请求为application/json类型，利用请求类型来POST
headers = {'Content-Type':'application/json'}

#POST爬取数据
for i in range(14):
    values = {'ID':i,'Type':'xx','lang':'jp'}
    # json.dump将python对象编码成json字符串
    values_json = json.dumps(values)
    # requests库提交数据进行post请求
    req = requests.post(url='http://dxyq.hbnu.edu.cn/aqzr/wxInterface/index.asmx/selfStudy',headers=headers ,data=values_json)
    reqq = req.text
    # 打印Unicode编码格式的json数据
    print(reqq)
    #新建txt文件
    fileName = 'Json'+str(i)+'.txt'
    f = open(fileName, 'w+')
    #将获取的数据存入txt文件中
    f.write(reqq)








