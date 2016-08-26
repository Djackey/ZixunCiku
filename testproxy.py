# coding: utf-8
from random import choice
import requests

params = {'by': '0',
          'kw': '红酒',
          'page': '1'
          }

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
    'Content-Type': 'text/html'
}
proxies = {
    "http:": "http:124.166.251.59:3128"
}

res = requests.post(
    "http://s.tool.chinaz.com/baidu/words.aspx#form", headers=headers, params=params, proxies=proxies, timeout=7)

print len(res.text)
print res.text
