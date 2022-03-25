# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import bs4
import requests
import time

def QHDaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/shijiancezhan/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    return value

def SHGaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/diyiguan/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    return value

def CLXaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/changlihuanbaoju/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    return value

def FNaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/funingdangxiao/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    return value

def BDHaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/beidaihe/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    return value

def LLXaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/lulongxianqixiangju/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    return value
    
while(True):
    print("the current AQI in 秦皇岛 is " + str(QHDaqiValue()))
    print("the current AQI in 山海关 is " + str(SHGaqiValue()))
    print("the current AQI in 昌黎县环保局 is " + str(CLXaqiValue()))
    print("the current AQI in 抚宁党校 is " + str(FNaqiValue()))
    print("the current AQI in 北戴河 is " + str(BDHaqiValue()))
    print("the current AQI in 卢龙县 is " + str(LLXaqiValue()))
    print("----------sleeping for one hour----------")
    t = 3600
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(" "+ timer, end="\r")
        time.sleep(1)
        t-=1
    time.sleep(t)




    



