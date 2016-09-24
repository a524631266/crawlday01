#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Zhangll
@software: PyCharm Community Edition
@time: 2016/9/25 1:37
"""
# the third package url:
# 1) request:this package  aims to request the http,and the help demo url:docs.python-requests.org/zh_CN/latest/user/quickstart.html pip install requests
import requests
# 2) Beautifulsoup:this package aims to parse the element of HTML，the help demo url:beautifulsoup.readthedocs.io/zh_CN/latest/#id12   pip install BeautifulSoup4 and  pip install lxml
# but the lxml parse function must in the C++ environment so you had to download C++ from :http://aka.ms/vcpython27
# alse need to install libxml2,Cython package
# libxml2 :http://xmlsoft.org/sources/win32/python/libxml2-python-2.7.7.win32-py2.7.exe
from bs4 import BeautifulSoup
# 3）next step is going to download picture from specific url
import urllib

#create a function to download picture/html documents
def download_jpg(url):
    response=requests.get(url)
    print response.status_code
    #using beuatifulsoup parse the response text
    soup =BeautifulSoup(response.text,'lxml')
    # print soup
    # to use soup parse the html:find_all
    urls=soup.find_all("img","BDE_Image")
    print urls
    for url in urls:
            url=url.get("src")
            print url
            urllib.urlretrieve(url,"img/%s"% url.split('/')[-1])

def get_all_jpg(url,pages):
    for page in range(1,pages+1):
        new_url=url+"?pn"+str(page)
        download_jpg(new_url)

if __name__=='__main__':
    # download_jpg("http://tieba.baidu.com/p/3797994694?pn=1")
    get_all_jpg("http://tieba.baidu.com/p/3797994694",5)