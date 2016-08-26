#!/usr/local/bin/python
#-*-coding:utf-8-*-
# 2015-6-26 DaoXin
import re
from CrawlBaiduKeyword import CrawlBaidukeyword
import xlwt
from bs4 import BeautifulSoup
import urllib
import xlwt
import time
from CrawlHc360 import CrawlHc360xx
from random import choice
import urllib
import requests


zixungjc = open('zixungjc.txt', 'a')
zixunzs = open('zixunzs.txt', 'a')

hc360lm_date = []
baidusswurl = open('baidusswurl.txt', 'a')
crawlhc360xx = CrawlHc360xx()


pagehtml = crawlhc360xx.curl("http://www.hc360.com/")
# print pagehtml

hc360lm_date = crawlhc360xx.hc360leimu(pagehtml)

for hc360lm in hc360lm_date:
	print hc360lm
