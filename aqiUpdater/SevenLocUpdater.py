# -*- coding: utf-8 -*-
"""
AQI Range Name Samples
0-50 
print("AQI in QinHuangDao is GREEN(0-50)") 
arduino.write(b'QHD1')
50-100 
print("AQI in QinHuangDao is YELLOW(50-100)") 
arduino.write(b'QHD2')
100-150 
print("AQI in QinHuangDao is ORANGE(100-150)") 
arduino.write(b'QHD3')
150-200 
print("AQI in QinHuangDao is RED(150-200)") 
arduino.write(b'QHD4')
above 200 
print("AQI in QinHuangDao is PURPLE(above200)") 
arduino.write(b'QHD5')
"""

import bs4
import requests
import time
import serial

arduino = serial.Serial('COM3', 9600, timeout=0.05)
time.sleep(1)
if not arduino.isOpen():
    arduino.open() 

def QHDaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/shijiancezhan/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text  
    data = int(value)
    if data >= 0 and data < 50:
        print("AQI in qinhuangdao is GREEN(0-50)") 
        arduino.write(b'A')
    elif data >= 50 and data < 100:
        print("AQI in qinhuangdao is YELLOW(50-100)") 
        arduino.write(b'B')
    elif data >= 100 and data < 150:
        print("AQI in qinhuangdao is ORANGE(100-150)") 
        arduino.write(b'C')
    elif data >= 150 and data < 200:
        print("AQI in qinhuangdao is RED(150-200)") 
        arduino.write(b'D')
    elif data >= 200:
        print("AQI in qinhuangdao is PURPLE(above200)") 
        arduino.write(b'E')
    else: print("qinhuangdao's data not in range")
    return value

def SHGaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/diyiguan/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    data = int(value)
    if data >= 0 and data < 50:
        print("AQI in shanhaiguan is GREEN(0-50)") 
        arduino.write(b'F')
    elif data >= 50 and data < 100:
        print("AQI in shanhaiguan is YELLOW(50-100)") 
        arduino.write(b'G')
    elif data >= 100 and data < 150:
        print("AQI in shanhaiguan is ORANGE(100-150)") 
        arduino.write(b'H')
    elif data >= 150 and data < 200:
        print("AQI in shanhaiguan is RED(150-200)") 
        arduino.write(b'I')
    elif data >= 200:
        print("AQI in shanhaiguan is PURPLE(above200)") 
        arduino.write(b'J')
    else: print("shanhaiguan's data not in range")
    return value

def CLXaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/changlihuanbaoju/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    data = int(value)
    if data >= 0 and data < 50:
        print("AQI in changlixian is GREEN(0-50)") 
        arduino.write(b'K')
    elif data >= 50 and data < 100:
        print("AQI in changlixian is YELLOW(50-100)") 
        arduino.write(b'L')
    elif data >= 100 and data < 150:
        print("AQI in changlixian is ORANGE(100-150)") 
        arduino.write(b'M')
    elif data >= 150 and data < 200:
        print("AQI in changlixian is RED(150-200)") 
        arduino.write(b'N')
    elif data >= 200:
        print("AQI in changlixian is PURPLE(above200)") 
        arduino.write(b'O')
    else: print("changlixian's data not in range")
    return value

def FNaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/funingdangxiao/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    data = int(value)
    if data >= 0 and data < 50:
        print("AQI in funing is GREEN(0-50)") 
        arduino.write(b'P')
    elif data >= 50 and data < 100:
        print("AQI in funing is YELLOW(50-100)") 
        arduino.write(b'Q')
    elif data >= 100 and data < 150:
        print("AQI in funing is ORANGE(100-150)") 
        arduino.write(b'R')
    elif data >= 150 and data < 200:
        print("AQI in funing is RED(150-200)") 
        arduino.write(b'S')
    elif data >= 200:
        print("AQI in funing is PURPLE(above200)") 
        arduino.write(b'T')
    else: print("funing's data not in range")
    return value

def BDHaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/beidaihe/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    data = int(value)
    if data >= 0 and data < 50:
        print("AQI in beidaihe is GREEN(0-50)") 
        arduino.write(b'U')
    elif data >= 50 and data < 100:
        print("AQI in beidaihe is YELLOW(50-100)") 
        arduino.write(b'V')
    elif data >= 100 and data < 150:
        print("AQI in beidaihe is ORANGE(100-150)") 
        arduino.write(b'W')
    elif data >= 150 and data < 200:
        print("AQI in beidaihe is RED(150-200)") 
        arduino.write(b'X')
    elif data >= 200:
        print("AQI in beidaihe is PURPLE(above200)") 
        arduino.write(b'Y')
    else: print("beidaihe’s data not in range")
    return value

def LLXaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/lulongxianqixiangju/cn/'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    data = int(value)
    if data >= 0 and data < 50:
        print("AQI in lulongxian is GREEN(0-50)") 
        arduino.write(b'Z')
    elif data >= 50 and data < 100:
        print("AQI in lulongxian is YELLOW(50-100)") 
        arduino.write(b'0')
    elif data >= 100 and data < 150:
        print("AQI in lulongxian is ORANGE(100-150)") 
        arduino.write(b'1')
    elif data >= 150 and data < 200:
        print("AQI in lulongxian is RED(150-200)") 
        arduino.write(b'2')
    elif data >= 200:
        print("AQI in lulongxian is PURPLE(above200)") 
        arduino.write(b'3')
    else: print("lulongxian's data not in range")
    return value

def SHGQZFaqiValue():
    url = 'https://aqicn.org/city/hebei/qinhuangdaoshi/shanhaiguanquzhengfu'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    data = int(value)
    if data >= 0 and data < 50:
        print("AQI in shanhaiguanquzhengfu is GREEN(0-50)") 
        arduino.write(b'4')
    elif data >= 50 and data < 100:
        print("AQI in shanhaiguanquzhengfu is YELLOW(50-100)") 
        arduino.write(b'5')
    elif data >= 100 and data < 150:
        print("AQI in shanhaiguanquzhengfu is ORANGE(100-150)") 
        arduino.write(b'6')
    elif data >= 150 and data < 200:
        print("AQI in shanhaiguanquzhengfu is RED(150-200)") 
        arduino.write(b'7')
    elif data >= 200:
        print("AQI in shanhaiguanquzhengfu is PURPLE(above200)") 
        arduino.write(b'8')
    else: print("shanhaiguanquzhengfu's data not in range")
    return value

    
while(True):
    print("the current AQI in 秦皇岛 is " + str(QHDaqiValue()))
    print("the current AQI in 山海关 is " + str(SHGaqiValue()))
    print("the current AQI in 昌黎县环保局 is " + str(CLXaqiValue()))
    print("the current AQI in 抚宁党校 is " + str(FNaqiValue()))
    print("the current AQI in 北戴河 is " + str(BDHaqiValue()))
    print("the current AQI in 卢龙县 is " + str(LLXaqiValue()))
    print("the current AQI in 山海关区政府 is " + str(SHGQZFaqiValue()))
    print("----------sleeping for 60 seconds----------")

    t = 60
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(" "+ timer, end="\r")
        time.sleep(30)
        t-=30
    time.sleep(t)
    
    
    
    
    
    
    
    
    
