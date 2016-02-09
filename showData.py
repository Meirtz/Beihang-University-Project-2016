from pandas import DataFrame, Series
#from matplotlib.pyplot import *

def getAQISeries(dataList, index):#dataList = readDataAndSaveToDataBase(), index = pd.date_range('20151101',periods=60)
    date_set = [data['date'] for data in dataList if data['date'] in index]
    AQI_set = [data['AQI'] for data in dataList if data['date'] in index]
    return Series(AQI_set, index=date_set)

def getAQIFrame(dataList, index):#dataList = readDataAndSaveToDataBase(), index = pd.date_range('20151101',periods=60)
    date_set = [data['date'] for data in dataList if data['date'] in index]
    AQI_set = [data['AQI'] for data in dataList if data['date'] in index]
    return DataFrame(AQI_set, index=date_set)

def degreeEveryday(dataList, index):
    date_set = [(data['date'],data['degree']) for data in dataList if data['date'] in index]
    for data in date_set:
        print(data[0], data[1])
    return date_set

def showDegreeTopPollutant(dataList, index):
    #柱状图显示污染物天数
    cframe = frame.dropna(how='any')
    cframe = DataFrame(dataList)
    pollutant_counts = cframe['pollutant'].value_counts()
    print(pollutant_counts)
    pollutant_counts.plot(kind='bar', rot=0)
    show()

def showDegreePieMonthly(dataList, index):
    #污染程度扇形图
    cframe = frame.dropna(how='any')
    cframe = DataFrame(dataList)
    pollutant_counts = cframe['degree'].value_counts()
    print(pollutant_counts)
    pollutant_counts.plot(kind='pie', rot=0)
    show()

def showAQIMonthly(dataList, index):
    series = getAQISeries(dataList, index)
    series.dropna(how='any')
    print(series)
    a = series.resample('M', how='mean')
    a.plot(kind='bar', rot=0, x=index)
    show()

def showAQISta(AQI_series):
    AQI_series.plot()
    show()
