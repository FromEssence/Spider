#实例：
#中国大学排名爬虫
#定向爬虫
#输入URL排名，输出大学排名信息

import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30);
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag): #过滤掉非标签类型的信息
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUniveList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}" #输出模板，其中的0，1，2，3表示使用第0，1，2，3个参数    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
          u = ulist[i]
          print(tplt.format(u[0], u[1], u[2], chr(12288)))
          
    print('Suc'+str(num));

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUniveList(uinfo, 20) #20 univs

main()
