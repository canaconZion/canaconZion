#
# 检测rtsp和rtmp拉流地址是否有流
#

from base64 import urlsafe_b64decode
import json
from locale import LC_ALL
import os
from typing import Any
from concurrent.futures import ThreadPoolExecutor
import asyncio
import subprocess
import time
import datetime
from unittest import result

def writeToFile(url,result): # 将检测结果写入文件并记录检测时间
	now=datetime.datetime.now()
	ft=open("urlDetectionResult.txt",'a')
	ft.write('\n')
	ft.write(result)
	ft.write('\n')
	ft.write(url)
	ft.write('\n')
	ft.write("Detection time：")
	ft.write(str(now))
	ft.write('\n')

async def judgUrl(comm): # 判断地址是否有流
	p=subprocess.Popen(comm.split(" "),stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	time_start=time.time()
	time_end=time.time()
	haveStreaming=True
	while time_end-time_start<30:
		next_line = p.stdout.readline()
		return_line = next_line.decode("utf-8", "ignore")
		if return_line == '' :#and p.poll() == None:
			print("Failed to push streaming")
			haveStreaming=False
			break
		print(return_line)
		# ft=open("errorCatch1.txt",'a')
		# ft.write(return_line)
		# ft.write('\n')
		time_end=time.time()
	if haveStreaming==True:
		print("Successfully pulled the stream from the url:")
		print(comm)
		
	else:
		print("Failed to pull a video stream from the url :")
		print(comm)
	p.kill()
	return haveStreaming
		
def judgeProtocol(str): # 判断拉流协议
	command:any
	s=str[0:4]
	if(s=="rtsp"):
		command='gst-launch-1.0 rtspsrc location= '+str+' ! fakesink dump=true'
	elif(s=="rtmp"):
		command='gst-launch-1.0 rtmpsrc location= '+str+' ! fakesink dump=true'
	return command

path='./automated-testing-config.json'
f = open(path,'r',encoding='utf-8')
m = json.load(f) 
urls=m['srcurl']
for url in urls:
	#print(str)
	comm=judgeProtocol(url)
	print(comm)
	loop = asyncio.get_event_loop()
	checkResult=loop.run_until_complete(judgUrl(comm))
	checkTime=str(datetime.datetime.now())
	if checkResult==True:
		writeToFile(url,"Successfully pulled the video stream from the url:")
	else:
		writeToFile(url,"Failed to pull a video stream from the url :")