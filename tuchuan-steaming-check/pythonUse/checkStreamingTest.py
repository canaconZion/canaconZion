
import json
import os
from typing import Any
from concurrent.futures import ThreadPoolExecutor
import asyncio
import subprocess
import time

async def test(comm):
    p=subprocess.Popen(comm.split(" "),stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #await asyncio.sleep(30)
    #p.kill()

    time_start=time.time()
    time_end=time.time()
    haveStreaming=True
    # next_line = p.stdout.readline()
    # return_line = next_line.decode("utf-8", "ignore")
    while time_end-time_start<30:
        next_line = p.stdout.readline()
        return_line = next_line.decode("utf-8", "ignore")
        if return_line == '' and p.poll() != None:
            print("Failed to push streaming")
            haveStreaming=False
            break
        print(return_line)
        ft=open("errorCatch1.txt",'a')
        ft.write(return_line)
        ft.write('\n')
        time_end=time.time()
    #     print(return_line)
    #     ft=open("errorCatch1.txt",'a')
    #     ft.write(return_line)
    #     ft.write('\n')
    #     time_end=time.time()
    if haveStreaming==True:
        print("Successfully pushing streaming from :")
        print(comm)
    else:
        print("Failed to push video streaming from :")
        print(comm)
    p.kill()
		
comm='gst-launch-1.0 rtspsrc location=rtsp://wowzaec2demo.streamlock.net/vod/mp4 ! fakesink dump=true'
#comm='gst-launch-1.0 rtspsrc location=rtsp://192.168.200.2 ! fakesink dump=true'
print(comm)
loop = asyncio.get_event_loop()
loop.run_until_complete(test(comm))