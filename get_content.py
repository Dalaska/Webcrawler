# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:02:04 2020

@author: DFTC_ZHANGDR
"""
from bs4 import BeautifulSoup

#如果是网址，可以用这个办法来读取网页

import urllib.request
with urllib.request.urlopen('https://dalaska.github.io/') as response:
   html = response.read()
   

bs = BeautifulSoup(html, "html.parser")
    

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link)
    
for link in links:
    fulllink = link.get ('href')
    print(fulllink)
    
pass