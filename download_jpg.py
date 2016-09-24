#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Zhangll
@software: PyCharm Community Edition
@time: 2016/9/24 23:50
"""
import urllib
import urllib2
import  re

def download_jpg(url):
    request=urllib2.Request(url)
    response=urllib2.urlopen(request)

    print response.getcode()

    html=response.read().decode('utf-8')#用网页的chatset来解码
    #用（）来获取我们想要的内容
    string = r'src="(http://imgsrc\.baidu\.com/forum/w%3D580/sign=.+?\.jpg)" pic_ext="jpeg"'
    urls=re.findall(string,html)
    # print urls
    x=0
    for url in urls:
        urllib.urlretrieve(url,"%s.jpg"% x)
        x+=1
        print url
if __name__=='__main__':
    download_jpg('http://tieba.baidu.com/p/3797994694')
