from gettext import npgettext
from tokenize import String
import numpy as np
import re
import time
import datetime
import json

def wFile(time:String,error,count):
    f=open("AnalyzeDoc.txt",'a') #新建文件，不改变文件原有内容，在后面写入
    line='错误发生时间：'+time+'   |   错误名称：'+error+'   |   出现次数：'+str(count)
    f.write(line) #写入数据
    f.write('\n')

def wErrorInFile(line):
    fts=open("AnalyzeDoc.txt",'a')
    fts.write(line)
    fts.write('\n')

def fileFormat():
    # now = time.asctime( time.localtime(time.time()))
    now=datetime.datetime.now() #.strftime('%Y-%m-%d') 获取当前时间
    ft=open("AnalyzeDoc.txt",'a')
    ft.write('\n')
    ft.write('检测时间： ')
    ft.write(str(now))
    ft.write('\n')

file="./tuchuan.log"
conPath='./errorCode.json'
errorName = json.load(open(conPath,'r',encoding='utf-8'))['errorCode']['error']
print(errorName)
a=0
#errorName='shmsrc error'
for line in open("./testLog/1657510357813-livegbd.log","r",encoding='UTF-8'):
    strs=line
    patt='error:' #设置需要匹配的字符串
    pattern=re.compile(patt) #使用compile方法进行匹配
    if pattern.findall(strs): #与str进行匹配
        a+=1 #如果匹配到了相同的字符串，记录
        Errtime=strs[0:24]
        # patta='2022-07-11T03:32'
        # #time=re.compile(patta).findall(line)
        # print(time)
        # wErrorInFile(line)
        # #result = pattern.findall(line)
        errReason=''
        for e in errorName:
            pattern=re.compile(str(e['errorName']))
            if pattern.findall(strs):
                errReason=e['reason']
        if(errReason!=''):
            errMess=str(Errtime)+": "+str(errReason)
            wErrorInFile(errMess)
        else:
            errMess=str(Errtime)+": 未知错误"
            wErrorInFile(errMess)

result=str(a)+' errors'
fts=open("AnalyzeDoc.txt",'a')
fts.write(result)
fts.write('\n')
fts.write('----------------------------------------------------------------')
fts.write('\n')
#wFile(str(time[0]),errorName,a)
fileFormat()
print("日志检测完成，数据记录在AnalyzeDoc.txt文件中")



