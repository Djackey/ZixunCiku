import urllib2
from bs4 import BeautifulSoup
from CrawlBaiduKeyword import CrawlBaidukeyword
# get the proxy
crawlbaidukeyword = CrawlBaidukeyword()
# of = open('proxy.txt', 'w')
# for page in range(1, 2):
#     xicidailiurl = "http://www.xicidaili.com/nn/%s" % str(page)
#     xicipagehtml = crawlbaidukeyword.curl(xicidailiurl)
#     soup = BeautifulSoup(xicipagehtml, 'lxml')
#     trs = soup.select("#ip_list")
#     print trs
#     for tr in trs:
#         print tr
#         ip = tds[2].text.strip()
#         port = tds[3].text.strip()
#         protocol = tds[6].text.strip()
#         if protocol == 'HTTP' or protocol == 'HTTPS':
#             # of.write('%s=%s:%s\n' % (protocol, ip, port))
#             print '%s://%s:%s' % (protocol, ip, port)


of = open('proxy.txt', 'w')
for page in range(1, 80):
    xicidailiurl = "http://www.kuaidaili.com/free/inha/%s/" % str(page)
    # xicipagehtml = urllib2.urlopen(xicidailiurl).read()
    xicipagehtml = crawlbaidukeyword.curl(xicidailiurl)
    soup = BeautifulSoup(xicipagehtml, 'lxml')
    trs = soup.select("[class~=table-striped] tbody tr")
    for tr in trs:
      tds=tr.select("td")
      ip= tds[0].text.strip() 
      port =tds[1].text.strip() 
      protocol = tds[3].text.strip() 
      if protocol == 'HTTP' or protocol == 'HTTPS':
            of.write('%s=%s:%s\n' % (protocol, ip, port))
            print '%s://%s:%s' % (protocol, ip, port)