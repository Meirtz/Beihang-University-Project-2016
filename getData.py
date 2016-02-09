#coding=utf-8
import urllib
import os

def getHtml(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
    return html

def writeHtml(filename, html):
    fp = open(filename,"w")
    fp.write(html)

def getData():
    for i in range(1,14):
        request = "http://datacenter.mep.gov.cn/report/air_daily/air_dairy.jsp?city=%E5%8C%97%E4%BA%AC%E5%B8%82&page="+repr(i)+"&startdate=2015-01-01&enddate=2015-12-31"
        #print request
        html = getHtml(request)
        filename = "./html/"+repr(i)+".txt"
        writeHtml(filename, html)