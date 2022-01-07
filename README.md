# demo
import requests
import json
import pandas as pd
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
url="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList" #一共380页数据
epsName = []  # 企业名称
productSn = []  # 许可证编号
epsProductAddress = []  # 企业地址
legalPerson = []  # 法人姓名
qfManagerName = []  # 发证机关

for n in range(1,3):
    n=str(n)
    data_dict={
    'on': 'true',
    'page': n,
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': ''
    }
    response=requests.post(url=url,data=data_dict,headers=headers).json()
    id_list=response['list']


    for id in id_list: #获取每个公司的ID号，进行第二层网页爬取
        id_no=id['ID']
        url_info="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
        data_dict_info={"id":id_no}
        response_info=requests.post(url=url_info,data=data_dict_info,headers=headers).json()
        epsName.append(response_info['epsName'])
        productSn.append(response_info['productSn'])
        epsProductAddress.append(response_info['epsProductAddress'])
        legalPerson.append(response_info['legalPerson'])
        qfManagerName.append(response_info['qfManagerName'])

dict_info={"企业名称":epsName,"许可证编号":productSn,"企业地址":epsProductAddress,"法人代表":legalPerson,"发证机关":qfManagerName}
df=pd.DataFrame(dict_info)
df.to_excel('huazhuangp.xlsx',index=False)
