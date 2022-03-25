# -*- coding: utf-8 -*-


import bs4
import requests
import serial
import time

arduino = serial.Serial('COM6', 9600, timeout=0.05)
time.sleep(1)
if not arduino.isOpen():
    arduino.open() 


def aqiValue():
    url = 'https://aqicn.org/city/shanghai'
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text, 'html.parser')
    value = soup.find('div', {'id':'aqiwgtvalue'}).text
    data = int(value)
    threshold = 50
    if(data > threshold):
        print("AQI is above 50") 
        arduino.write(b'H')
    if(data < threshold):
        print("AQI is below 50") 
        arduino.write(b'L') 
    return data

while True:  
    print("the current aqi in QinHuangDao is " + str(aqiValue()))

