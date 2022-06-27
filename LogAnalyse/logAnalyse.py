from gettext import npgettext
import os
from tokenize import String
import numpy as np
import re
import time
import datetime

def wFile(time:String,error,count):
    f=open("AnalyzeDoc.txt",'a') #新建文件，不改变文件原有内容，在后面写入
    line='错误发生时间：'+time+'   |   错误名称：'+error+'   |   出现次数：'+str(count)
    f.write(line) #写入数据
    f.write('\n')

def fileFormat():
    # now = time.asctime( time.localtime(time.time()))
    now=datetime.datetime.now() #.strftime('%Y-%m-%d') 获取当前时间
    ft=open("AnalyzeDoc.txt",'a')
    ft.write('\n')
    ft.write('检测时间： ')
    ft.write(str(now))
    ft.write('\n')
    ft.write('----------------------------------------------------------------')
    ft.write('\n')

file="./tuchuan.log"
a=0
name:any
errorName='shmsrc error'
for line in open("tuchuan.log","r",encoding='UTF-8'):
    strs=line
    patt='error' #设置需要匹配的字符串
    pattern=re.compile(patt) #使用compile方法进行匹配
    if pattern.findall(strs): #与str进行匹配
        a+=1 #如果匹配到了相同的字符串，记录
        patta='2022-06-22T08:00:57.705Z'
        time=re.compile(patta).findall(line)
        #print(time)
        #result = pattern.findall(line)
#print(a)
fts=open("AnalyzeDoc.txt",'a')
fts.write('----------------------------------------------------------------')
fts.write('\n')
wFile(str(time[0]),errorName,a)
fileFormat()
print("日志检测完成，数据记录在AnalyzeDoc.txt文件中")



