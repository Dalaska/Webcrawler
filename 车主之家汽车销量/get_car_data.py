"""
get car sales from website

"""
import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve  

#url = 'https://xl.16888.com/brand-0-201911-201911-1.html'
#r = requests.get(url) #get webpage 
#soup = BeautifulSoup(r.content, "html.parser") #解析网页，比如加上.content的内容。

soup = BeautifulSoup(open("car_sales.html",'rb'))
#error:https://www.cnblogs.com/mengyu/p/6638975.html
print(soup.prettify())

hyperlink = soup.find_all('td')

file_list = []

for h in hyperlink:
    hh = h.get('class')
    if hh == ['xl-td-t1']:
        file_list.append(h)

pass