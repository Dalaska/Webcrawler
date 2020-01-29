import requests
from lxml import html
url='https://movie.douban.com/' #��Ҫ�����ݵ���ַ
url = 'https://www.zhipin.com/job_detail/f220858e85d8094403N53tq7ElA~.html?ka=search_list_1'
page=requests.Session().get(url) 
tree=html.fromstring(page.text) 
result=tree.xpath('//td[@class="job-sec"]//a/text()') #��ȡ��Ҫ������
