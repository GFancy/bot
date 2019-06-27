# -*- coding:utf-8 -*-
'''
百度搜索到的url爬取保存
'''
from bs4 import BeautifulSoup    #处理抓到的页面
import requests
from urllib import request
import urllib

 
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
} #定义头文件，伪装成浏览器


def getfromBaidu(word,num):
    url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(word) + '&pn='  # word为关键词，pn是百度用来分页的..
    path = url + str((num - 1) * 10)
    response = request.urlopen(path)
    page = response.read()
    soup = BeautifulSoup(page, 'lxml')
    tagh3 = soup.find_all('h3')
    href2 = ""
    for h3 in tagh3:
        href = h3.find('a').get('href')
        # print(href)
        baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
        real_url = baidu_url.headers['Location']  #得到网页原始地址
        if real_url.startswith('http'):
            href2 = href2 + real_url + '\n'
            #print(real_url + '\n')
        # all.write(real_url + '\n')
    return href2

    
def browse(href):
    respose=requests.get(href)
    respose.encoding='utf-8'
    # print(respose.status_code)# 响应的状态码
    # print(respose.content)  #返回字节信息
    # print(respose.text)  #返回文本内容
    return respose.text


if __name__ == '__main__':
    print(getfromBaidu('Google',2))
