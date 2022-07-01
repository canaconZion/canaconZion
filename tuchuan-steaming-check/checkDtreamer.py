
# import os
# import commands
# print('=============================ls')
# os.system('gst-launch-1.0 rtspsrc location=rtsp://192.168.10.189:8554/test ! fakesink dump=true')

import json
import os
from typing import Any
from concurrent.futures import ThreadPoolExecutor
import asyncio
import subprocess

async def test(comm):
		p=subprocess.Popen(comm.split(" "),stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
		await asyncio.sleep(10)
		if len(p.stderr.readlines())!=0:
			print(p.stderr.readlines())
		p.kill()
		

def judgeProtocol(str):
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
a=m['srcurl']
#os.system('gst-launch-1.0 rtspsrc location=rtsp://192.168.10.189:8554/test ! fakesink dump=true')
i=0
for str in a:
	#print(str)
	comm=judgeProtocol(str)
	print(comm)
	loop = asyncio.get_event_loop()
	loop.run_until_complete(test(comm))
	# for b in os.popen(command).readline():
	# 	print(b)
	# 	i+=1
	# 	if(i>100):
	# 		break

	# if(i>100):
	# 	print("push stream successful")
	# else:
	# 	print("filed to push streamin")


