import os
import sqlite3
import getData
import csv
from collections import defaultdict
from collections import Counter # Counter.most_common(int)
from pandas import DataFrame, Series, Panel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dateutil.parser import parse
import datetime




dataset = pd.read_csv('./data/data.txt', names=['ID', 'city', 'date', 'AQI', 'degree', 'pollutant'])
print(dataset)
group_data = dataset.groupby('pollutant').sum()
print(group_data)
group_data.plot()
plt.show()
#po_data = dataset.pivot_table('AQI', rows='date', cols='pollutant',aggfunc=sum)