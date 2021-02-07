# coding=utf-8
import re
from bs4 import BeautifulSoup

import urllib.request,urllib.error
baseUrl = 'https://movie.douban.com/top250?start=0'
headers = {
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"
}

# 1.图片地址
# 2、影片中文、英文名字
# 3、影片的介绍
# 4、影片的评分
# 5、影片的评价人数
# 6、影片的简介

def getdata():
    req = urllib.request.Request(url=baseUrl, headers=headers, method="GET")
    try:
        response = urllib.request.urlopen(req).read().decode("utf-8")
    except Exception as e:
        print(e)
    soup=BeautifulSoup(response,'html.parser')
    liList=soup.find_all("div",class_="item")
    # print(liList[0])
    # movieList=str(soup.find('span',class_="title"))
    # moviename=re.search(r'<span class="title">(.*?)</span>',movieList)
    # print(moviename.group(1))
    # print(movieList)
    a=liList[0].select(".pic>a")[0]
    print(a)
    movieAdress=re.search(r'<a href="(.*)">',str(a))
    print(movieAdress.group(1))
    img= liList[0].select(".pic>a>img")[0]
    print(img)
    movieImg=re.search(r'src="(.*?)"', str(img))
    print(movieImg.group(1))
getdata()