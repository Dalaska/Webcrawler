"""
get car sales from website
"""
import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve  
import pandas as pd
#url = 'https://xl.16888.com/brand-0-201911-201911-1.html'
#error:https://www.cnblogs.com/mengyu/p/6638975.html
#r = requests.get(url) #get webpage 
# 网站防爬虫机制只回复浏览器，将网页下载后读取
#soup = BeautifulSoup(r.content, "html.parser") #解析网页，比如加上.content的内容。

soup = BeautifulSoup(open("car_sales.html",'rb'))
print(soup.prettify())

hyperlink = soup.find_all('td')

list1 = []
list2 = []
list3 = []
# 
for link in hyperlink:
    title = link.get('class')
    if title == ['xl-td-t1']:
        list1.append(link)
    elif title == ['xl-td-t2']:
        list2.append(link)
    elif title == ['xl-td-t3']:
        list3.append(link)

rank = []
brand = []
country = []
sales = []
share = []
for n in range(len(list1)):
    # get rank
    rank.append(list1[n].contents[0])
    # get brand
    brand.append(list2[n].contents[0].contents[0]) 
    # get country
    country.append(list3[3*n].contents[0])
    # get sales 
    sales.append(list3[3*n+1].contents[0])
    # get percentage
    share.append(list3[3*n+2].contents[0])

#entry = [rank, brank, country, sales, share ]

entry = {'rank':rank,'brand':brand,'country':country,\
'sales':sales, 'share':share}
data_df = pd.DataFrame(entry)
data_df.to_csv('car_sales.csv',index=None,encoding="gb2312")

pass

