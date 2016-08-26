#!/usr/local/bin/python
#-*-coding:utf-8-*-
# 2015-6-26 DaoXin
import pycurl
import StringIO
import urllib
import urllib2
from random import choice
import re
import sys
import string
from bs4 import BeautifulSoup
import requests
import sys
import csv
import xlrd
import xlwt
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

# useragent 列表，大家可以自行去收集。不过在本例中似乎不需要这个
AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-CN) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; zh-CN) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; zh-CN) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.5 (KHTML, like Gecko) Safari/312.3",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Camino/2.2.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre Camino/2.2a1pre",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.79 Safari/537.4",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; zh-CN) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; zh-CN) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0",
]




class CrawlZzword:

    def __init__(self):
        self.UserAgent = choice(AGENTS)

# 这个curl方法是从zero那里扒过来的。http://www.seoqx.com/post/341
    def curl(self, guanjianci,proxy):
        url = "http://s.tool.chinaz.com/baidu/words.aspx"
        post_data_dic = {	"by": "0",
                          "kw": guanjianci,
                          "page": "1"
                          }
        crl = pycurl.Curl()
        crl.setopt(pycurl.VERBOSE, 1)
        crl.setopt(pycurl.FOLLOWLOCATION, 1)
        crl.setopt(pycurl.MAXREDIRS, 5)
        # crl.setopt(pycurl.AUTOREFERER,1)

        crl.setopt(pycurl.CONNECTTIMEOUT, 60)
        crl.setopt(pycurl.TIMEOUT, 300)
        crl.setopt(pycurl.PROXY, proxy)
        crl.setopt(pycurl.HTTPPROXYTUNNEL, 1)
        #crl.setopt(pycurl.NOSIGNAL, 1)
        crlfp = StringIO.StringIO()
        crl.setopt(pycurl.USERAGENT, choice(AGENTS))

        # Option -d/--data <data>   HTTP POST data
        crl.setopt(crl.POSTFIELDS,
                   urllib.urlencode(post_data_dic))

        crl.setopt(pycurl.URL, url)
        crl.setopt(crl.WRITEFUNCTION, crlfp.write)
        crl.perform()
        return crlfp.getvalue(),crl.getinfo(crl.HTTP_CODE)


# s="红酒"
# print urllib.quote(s.encode('gbk')).lower()
