from selenium import webdriver
import time

url = 'https://www.baidu.com/'
driver=webdriver.Chrome() #声明调用chrome
driver.get(url) #获取百度页面
input=driver.find_element_by_id('kw')
input.send_keys("python")#输入搜索关键词
searchButton=driver.find_element_by_id('su')#获取搜索按钮
searchButton.click()
time.sleep(3)
driver.quit()
