# coding=utf-8
import re
import requests
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request
from urllib.request import urlopen
import pandas as movieDataList

baseUrl='https://movie.douban.com/top250?start='
headers = {
     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56'

}
movieDataList = []
for j in range(0,2):
    star=j*25
    url=baseUrl+str(star)
    req = Request(url=url, headers=headers, method="GET")
    response = urlopen(req).read().decode("utf-8")

    soup = BeautifulSoup(response, 'html.parser')
    movielist = soup.find_all("div", class_="item")
    for i in range(0, 25):
        moviename = re.search(r'<span class="title">(.*?)</span>', str(movielist[i]))
        movevedio = movielist[i].select(".info > .hd > a")[0]
        vedioname = re.search(r'<a class="" href="(.*?)">', str(movevedio))
        movieimg = movielist[i].select(".pic>a>img")
        img = re.search('src="(.*?)"', str(movieimg))
        movedaoyan = movielist[i].select(".info>.bd>p")[0]
        daoyan = re.search('<p class="">([\s\S]*?)</p>', str(movedaoyan))
        jianjie = daoyan.group(1).strip().replace(" ", '').replace("\n", '').replace("<br/>", '').replace('/', '')
        moviecomment = movielist[i].select(".star>.rating_num")[0].get_text()
        jieshao = movielist[i].select('.quote>.inq')[0].get_text()
        movedata = (moviename.group(1), vedioname.group(1), img.group(1), jianjie, moviecomment, jieshao)
        # print(movedata)
        movieDataList.append(movedata)

print(movieDataList)
print(len(movieDataList))