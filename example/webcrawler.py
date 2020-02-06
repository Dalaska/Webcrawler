import requests
from lxml import html
url='https://movie.douban.com/' #��Ҫ�����ݵ���ַ
page=requests.Session().get(url) 
tree=html.fromstring(page.text) 
result=tree.xpath('//td[@class="job-sec"]//a/text()') #��ȡ��Ҫ������
