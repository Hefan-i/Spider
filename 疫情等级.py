#coding=utf-8
import pymysql
import re
import requests
import time
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request
from urllib.request import urlopen
import pandas as movieDataList
import datetime
from selenium import webdriver
Listgao=[]
url='http://bmfw.www.gov.cn/yqfxdjcx/risk.html'''
driver=webdriver.Chrome() #声明调用chrome
driver.get(url) #获取百度页面
# str1=driver.find_elements_by_class_name("h-header") # class
# print("okok")
# for i in range(0,len(str1)):
#     difang = str(str1[i].text)
#     difang=difang.replace('高风险','')
#     lst = difang.split()
#     province = lst[0]
#     city = lst[1]
#     area = lst[2]
#     if len(lst)>=3:
#         for j in range(3,len(lst)):
#             t = (province, city,area,lst[j],'高风险')
#             Listgao.append(t)
#     else :
#         t = (province, city,area,'高风险')
#         Listgao.append(t)
# print(Listgao)

# print(str[0].find_elements_by_class_name("h-span"))
time.sleep(3)
# fengxian=driver.find_element_by_class_name('r-middle')
# # input.send_keys("python")#输入搜索关键词
# # searchButton=driver.find_element_by_id('su')#获取搜索按钮
# fengxian.click()
# Listzhong=[]
# str2=driver.find_elements_by_class_name("m-header") # class
# print("okok")
# for i in range(0,len(str2)):
#     difang = str(str2[i].text)
#     difang=difang.replace('中风险','')
#     lst = difang.split()
#     province = lst[0]
#     city = lst[1]
#     area = lst[2]
#     if len(lst)>=3:
#         for j in range(3,len(lst)):
#             t = (province, city,area,lst[j],'中风险')
#             Listzhong.append(t)
#     else :
#         t = (province, city,area,'中风险')
#         Listzhong.append(t)
# print(Listzhong)

# response=urlopen().read().decode("UTF-8")
# time.sleep(5)
# print(response)
now = datetime.datetime.now()
def getMessage(A,B,C):

    fengxian = driver.find_element_by_class_name(A)
    # input.send_keys("python")#输入搜索关键词
    # searchButton=driver.find_element_by_id('su')#获取搜索按钮
    fengxian.click()
    str1 = driver.find_elements_by_class_name(B)  # class
    print("okok")
    for i in range(0, len(str1)):
        difang = str(str1[i].text)
        difang = difang.replace(C, '')
        lst = difang.split()
        province = lst[0]
        city = lst[1]
        area = lst[2]
        if len(lst) > 3:
            for j in range(3, len(lst)):
                t = (province, city, area, lst[j], C, now)
                Listgao.append(t)
        else:
            t = (province, city, area,'所有地区', C, now)
            Listgao.append(t)

getMessage('r-high','h-header','高风险')
time.sleep(3)
hbutton=driver.find_elements_by_id("nextPage")[0]
while hbutton.is_enabled():
    print('我点了')
    hbutton.click()
    hbutton = driver.find_elements_by_id("nextPage")[0]#重新获取一下按钮
    getMessage('r-high','h-header','高风险')
time.sleep(2)
getMessage('r-middle','m-header','中风险')
time.sleep(3)
mbutton=driver.find_elements_by_id("nextPage")[1]
while mbutton.is_enabled():
    print('我点了')
    mbutton.click()
    mbutton = driver.find_elements_by_id("nextPage")[1]#重新获取一下按钮
    getMessage('r-middle', 'm-header', '中风险')


print(Listgao)
driver.quit()


db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='python')  # 参数db为指定数据库
tt = db.cursor()
clearsql='truncate table yiqing;'
tt.execute(clearsql)
addsql = "insert into yiqing (province, city, area, street, level, creat_time) " \
          "values (%s, %s, %s, %s, %s, %s)"

print("执行sql")
try:
    res=tt.executemany(addsql,Listgao)#执行sql语句
    db.commit() # 提交到数据库执行
except:
    # 如果发生错误则回滚
    db.rollback()
print(res)
db.close()

