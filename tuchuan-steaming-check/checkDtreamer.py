
# import os
# import commands
# print('=============================ls')
# os.system('gst-launch-1.0 rtspsrc location=rtsp://192.168.10.189:8554/test ! fakesink dump=true')

import json
import os
from typing import Any

def judgeProtocol(str):
	command:Any
	s=str[0:4]
	if(s=="rtsp"):
		command='gst-launch-1.0 rtspsrc location= '+str+'! fakesink dump=true'
	elif(s=="rtmp"):
		command='gst-launch-1.0 rtmpsrc location= '+str+'! fakesink dump=true'
	return command

path='./automated-testing-config.json'
f = open(path,'r',encoding='utf-8')
m = json.load(f) # json.load() 这种方法是解析一个文件中的数据
				 # json.loads() 需要先将文件，读到一个变量作为字符串, 解析一个字符串中的数
a=m['srcurl']
#os.system('gst-launch-1.0 rtspsrc location=rtsp://192.168.10.189:8554/test ! fakesink dump=true')
i=0
for str in a:
	#print(str)
	command=judgeProtocol(str)
	#print(command)
	for b in os.popen(command).readlines():
		i+=1
		if(i>1000):
			break

	if(i>1000):
		print("push stream successful")
	else:
		print("filed to push streamin")

