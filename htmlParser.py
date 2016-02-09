from bs4 import BeautifulSoup
import sqlite3
import os


def creatDataFile(filename):
    fp = open(filename, 'w')
    #fp.write('')
    fp.close()

def writeData(filename, line, terminator):
    if line == None:
        line = "Na" + terminator
    else:
        line += terminator
    fp = open(filename,"a")
    fp.write(line)
    fp.close()

def parseHtmlAndSave():
    i = 1
    htmlFilename ="./html/" + repr(i)+".txt"
    dataFilename = "./data/data.txt"
    creatDataFile(dataFilename)
    while os.path.exists(htmlFilename):
        print ("***************第%d组***************" % i)
        soup = BeautifulSoup(open(htmlFilename), "lxml")
        stas =  soup.body.table.tr.div.center.find_all('td')
        #删除多余内容
        del stas[0:10]
        del stas[-14:]
        index = 1
        terminator = ''
        for sta in stas:
           print (sta.string)
           if index % 6 != 0:
               terminator = ' '
           else:
               terminator = '\n'
           writeData(dataFilename, sta.string, terminator)
           index += 1
        i += 1
        htmlFilename = "./html/"+repr(i)+".txt"
        dataFilename = "./data/data.txt"

parseHtmlAndSave()