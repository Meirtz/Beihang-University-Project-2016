import os
from tkinter import *
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from showData import *
from dateutil.parser import parse

def readDataAndSaveToDataBase():
    files = os.listdir("./data/")
    del files[:1]

    dataList = []
    for file in files:
        with open("./data/" + file,'r') as fp:
            for line in fp:
                (ID, city, date, AQI, degree, pollutant) = line.split()
                if AQI == 'Na':
                    AQI = np.nan
                if pollutant == "Na":
                    dict_tmp = {'ID':int(ID), 'city':city, 'date':parse(date), 'AQI':float(AQI), 'degree':degree}
                else:
                    dict_tmp = {'ID':int(ID), 'city':city, 'date':parse(date), 'AQI':float(AQI), 'degree':degree, 'pollutant':pollutant}
                dataList.append(dict_tmp)
    return dataList


dataList = readDataAndSaveToDataBase()
index = pd.date_range('20150101',periods=300)
def gui(master):
    #设计GUI界面
    label1=Label(master,text="输入起始日期(如:20150101)")
    label1.pack()

    label2=Label(master,text="时间长度(天数,合理的整数)")
    label2.pack()

    text = Text(master,height=2,width=25)
    text.pack()

    button1 = Button(master,text="污染程度扇形图:",command=showDegreePieMonthly(dataList, index))
    button1.pack()

    button2 = Button(master,text="污染物排行：",command=showDegreeTopPollutant(dataList, index))
    button2.pack()

    button3 = Button(master,text="AQI数据：",command=showAQISta(dataList))
    button3.pack()

    button4 = Button(master,text="月度AQI数据：",command=showAQIMonthly(dataList, index))
    button4.pack()

#airdata_set = sqlite3.connect("airdata.db")
#airdata_set.execute("CREATE TABLE airdata (id INT PRIMARY KEY, city TEXT, date VARCHAR(10), AQI INT, degree INT, pollutant TEXT)")
#airdata_set.commit()


master=Tk()
master.title("空气质量分析")
gui(master)
master.mainloop()






