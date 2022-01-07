import requests
import json
import pandas as pd
from lxml import etree
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
url="https://movie.douban.com/top250"
names=[]
engnames=[]
othernames=[]
quotes=[]
scores=[]
score_nos=[]
directors=[]
styles=[]
for i in range(3):
    n=str(i*25)
    param={'start': n,
    'filter': ''}
    response=requests.get(url=url,params=param,headers=headers).text
    tree=etree.HTML(response)
    name=tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')#电影名
    for na in name:
        names.append(na.strip())
    englishname=tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[2]/text()')#英文名
    for eng in englishname:
        engnames.append(eng.strip())
    # othername=tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[3]/text()')#别名,有的没有
    # for oth in othername:
    #     othernames.append(oth.strip())
    # quote=tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()')#简介
    # for quo in quote:
    #     quotes.append(quo.strip())
    score=tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')#评分
    for sc in score:
        scores.append(sc.strip())
    score_no=tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[4]/text()')#打分人数
    for scn in score_no:
        score_nos.append(scn.strip())
    # director=tree.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[1]/text()[1]')#演职人员
    # for direc in director:
    #     directors.append(direc.strip())
    style=tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[2]')#年份类型
    for sty in style:
        styles.append(sty.strip())
    print("第{}页已经完成了！！！".format(i+1))
info_dict={'电影名':names,'英文名':engnames,'评分':scores,'打分人数':score_nos,'年份类型':styles}
df=pd.DataFrame(info_dict)
#df.to_excel('douban3.xlsx')
df.to_excel(r'C:\Users\Administrator\Desktop\douban3.xlsx')
