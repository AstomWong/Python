# -*- coding: utf-8 -*-
import requests
import csv
import os
import sys
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from bs4 import BeautifulSoup

Data_05 = []
Data_10 = []
Data_15 = []
Data_20 = []
Content_05 = []
Content_10 = []
Content_15 = []
Content_20 = []


Date = []
Data = []
Date_05 = []
Date_10 = []
Date_15 = []
Date_20 = []
rawData = []
Content = []

#This part is open the CSV File
pathProg = 'E:\\Airport_Project\\20170519\\textFile'
os.chdir(pathProg)

if os.getcwd() != pathProg:
    print "EEROR: the file path incorrect."
    sys.exit()

file = open(pathProg + '\\0002_Data.csv', 'r')
csvCursor = csv.reader(file)

for row in csvCursor:
    # push the data into list
    rawData.append(row)
    #print Data
file.close()

for d in range(len(rawData)):
    day, month, year = rawData[d][0].split("/")
    print (int(year))
    #Date.append([year,month, day, Data[d][1], Data[d][2], Data[d][3], Data[d][4], Data[d][5], Data[d][6]])
    if int(year) >= 2000 and int(year) < 2005:
        Data_05.append([mdates.date2num(dt.date(int(year), int(month), int(day))), rawData[d][1], rawData[d][2], rawData[d][3], rawData[d][4], rawData[d][5], rawData[d][6]])
        Date_05.append([mdates.date2num(dt.date(int(year), int(month), int(day)))])
        Content_05.append(float(rawData[d][1]))
    if int(year) >= 2005 and int(year) < 2010:
        Data_10.append([mdates.date2num(dt.date(int(year), int(month), int(day))), rawData[d][1], rawData[d][2], rawData[d][3], rawData[d][4], rawData[d][5], rawData[d][6]])
        Date_10.append([mdates.date2num(dt.date(int(year), int(month), int(day)))])
        Content_10.append(float(rawData[d][1]))
    if int(year) >= 2010 and int(year) < 2015:
        Data_15.append([mdates.date2num(dt.date(int(year), int(month), int(day))), rawData[d][1], rawData[d][2], rawData[d][3], rawData[d][4], rawData[d][5], rawData[d][6]])
        Date_15.append([mdates.date2num(dt.date(int(year), int(month), int(day)))])
        Content_15.append(float(rawData[d][1]))
    if int(year) >= 2015 and int(year) < 2020:
        Data_20.append([mdates.date2num(dt.date(int(year), int(month), int(day))), rawData[d][1], rawData[d][2], rawData[d][3], rawData[d][4], rawData[d][5], rawData[d][6]])
        Date_20.append([mdates.date2num(dt.date(int(year), int(month), int(day)))])
        Content_20.append(float(rawData[d][1]))

    Data.append([mdates.date2num(dt.date(int(year), int(month), int(day))), rawData[d][1], rawData[d][2], rawData[d][3], rawData[d][4], rawData[d][5], rawData[d][6]])
    Date.append([mdates.date2num(dt.date(int(year), int(month), int(day)))])
    Content.append(float(rawData[d][1]))

#Basic Graphic
#print (mdates.num2date(Date_05))

#plt.subplot(221)
#xRay = Date
#yRay = Content
#plt.xticks(rotation=45)
#plt.format_xdata = mdates.DateFormatter('%y-%m-%d')
#plt.plot_date(xRay, yRay, 'b.-')
#plt.grid(True)

plt.subplot(221)
plt.xticks(rotation=45)
plt.format_xdata = mdates.DateFormatter('%y-%m-%d')
plt.plot_date(Date_05, Content_05, 'r.-')
plt.grid(True)

plt.subplot(222)
plt.xticks(rotation=45)
plt.format_xdata = mdates.DateFormatter('%y-%m-%d')
plt.plot_date(Date_10, Content_10, 'g.-')
plt.grid(True)

plt.subplot(223)
plt.xticks(rotation=45)
plt.format_xdata = mdates.DateFormatter('%y-%m-%d')
plt.plot_date(Date_15, Content_15, 'b.-')
plt.grid(True)

plt.subplot(224)
plt.xticks(rotation=45)
plt.format_xdata = mdates.DateFormatter('%y-%m-%d')
plt.plot_date(Date_20, Content_20, 'b.-')
plt.grid(True)

plt.show()


