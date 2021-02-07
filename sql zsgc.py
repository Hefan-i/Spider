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
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='python')  # 参数db为指定数据库
tt = db.cursor()

# addsql = "insert into yiqing (province, city, area, street, level, creat_time) " \
#           "values (%s, %s, %s, %s, %s, %s)"
# changesql="update yiqing set level='无风险' where area='滨江区';"
# # print("执行sql")
# # change=tt.execute(changesql)
# # print(change)
# fingsql="select* from yiqing where street='长河街道';"
# find=tt.execute(fingsql)
# result=tt.fetchall()
# print(find)
# print(result)
deletesql=" delete from yiqing where area='诸暨';"
tt.execute(deletesql)

# res = tt.execute(addsql, ("浙江省", "绍兴", '诸暨', '安华','风险','111' ))
db.commit()