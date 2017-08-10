__author__ = 'Hannah Cat'

# ===========================================================
# Example:
# catch dara directly from http://news.baidu.com
# get hot news and links
# using urllib operate web page
# using BeautifulSoup for scrapping
# 2017.08.09
# ===========================================================

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
# import urllib
# import sys
# import imp
# imp.reload(sys)

url = 'http://news.baidu.com/' #待抓取的网页地址
content = urllib.request.urlopen(url).read() #获取网页的html文本
soup = BeautifulSoup(content, "lxml")

#识别热点新闻
hotNews = soup.find_all('div', {'class', 'hotnews'})[0].find_all('li')
for i in hotNews:
    print(i.a.text) #打印新闻标题
    print(i.a['href']) #打印新闻链接
