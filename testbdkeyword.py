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
from Crawlzzindex import CrawlZzword
from random import choice
import urllib
import requests


zixungjc = open('zixungjc.txt', 'a')
zixunzs = open('zixunzs.txt', 'a')
crawlzzword = CrawlZzword()
baidussrelate_date = []
comboboxci_date = []
baidusswurl = open('baidusswurl.txt', 'a')
crawlbaidukeyword = CrawlBaidukeyword()
for firstmuci in open(r'firstmuci.txt', 'r'):
    firstmuci = firstmuci.strip('\n')
    baidussurl = "https://www.baidu.com/s?ie=utf-8&wd=" + \
        urllib.quote(firstmuci)
    baidusshtml = crawlbaidukeyword.curl(baidussurl)
    if 'http://verify.baidu.com/' in baidusshtml:
        print '出现验证码，等待5分钟后自动开始'
        time.sleep(500)
    else:
        baidussrelatelist = crawlbaidukeyword.baidurightrelatedsearch(
            baidusshtml)
        for baidussrelate in baidussrelatelist:
            baidussrelatestr = str(baidussrelate)
            baidussrelate_date.append(baidussrelatestr)

for baidussrelateindex in baidussrelate_date:
    comboboxcilist = crawlbaidukeyword.baiduindexcombobox(baidussrelateindex)
    for comboboxci in comboboxcilist:
        comboboxci_date.append(comboboxci)


for j in range(0, len(comboboxci_date)):
    zixungjc.write('%s\n' % comboboxci_date[j].decode("GBK").encode("utf-8"))
    print comboboxci_date[j].decode("GBK").encode("utf-8")

# proxy_data = []
# for proxylist in open(r'proxy.txt', 'r'):
#     httpproxylist = "http://" + proxylist
#     proxy_data.append(httpproxylist)
# zzproxy = choice(proxy_data)

# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
#     'Content-Type': 'text/html'
# }
# proxies = {
#     "http:": zzproxy
# }


# # for comboboxciindexutf in comboboxci_date:
# for comboboxciindexutf in open(r'testfirstmuci.txt', 'r'):
#     comboboxciindexutf = comboboxciindexutf.strip('\n')
#     params = {'by': '0',
#               'kw': comboboxciindexutf,
#               'page': '1'
#               }
#     comboboxciindex = comboboxciindexutf.decode("GBK").encode("utf-8")
#     baiduindexurl = "http://index.baidu.com/main/word.php\?word=" + \
#         urllib.quote(comboboxciindex.encode('gbk')).lower()
#     while 1:
#         res = requests.post(
#             "http://s.tool.chinaz.com/baidu/words.aspx#form", headers=headers, params=params, proxies=proxies, timeout=7)
#         pagehtml = res.text
#         if res.status_code == "200":
#             if "404 -" in pagehtml:
#                 print '出现验证码，等待5分钟后自动开始'
#                 zzproxy = choice(proxy_data)
#                 continue
#             else:
#                 soup = BeautifulSoup(pagehtml, 'lxml')
#                 keywordindexlist = soup.find_all(
#                     href=re.compile(baiduindexurl))
#                 if keywordindexlist:
#                     print keywordindexlist[0].string
#                     zixunzs.write('%s\n' % keywordindexlist[0].string)
#                     break
#                 else:
#                     print '0'
#                     zixunzs.write('0\n')
#                     break
#         else:
#             zzproxy = choice(proxy_data)
#             continue


# file = xlwt.Workbook()
# table = file.add_sheet('sheet name')
# # 写入数据table.write(行,列,value)
# for j in range(0, 20):
#     table.write(j, 1, comboboxci_date[j])

# file.save('chanpin.xls')
# for comboboxciindex in comboboxci_date:
#     comboboxciindex = comboboxciindex.strip('\n')
#     urlindex5118 = "http://www.5118.com/seo/words/" + \
#         urllib.quote(comboboxciindex)
#     urlindex5118html = crawlbaidukeyword.curl(urlindex5118)
#     if "您的操作过于频繁,请提交验证码" in urlindex5118html:
#         print "您的操作过于频繁,请提交验证码"
#         time.sleep(500)
#         continue
#     else:
#         keywordindexlist = crawlbaidukeyword.index5118(urlindex5118html)
#         for keywordindexzs in keywordindexlist:
#             keywordindexzs = keywordindexzs.strip('\n')
#             print keywordindexzs
#             zixunzs.write('%s\n' % keywordindexzs)
