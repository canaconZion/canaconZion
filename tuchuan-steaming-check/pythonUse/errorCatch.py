# from ftplib import error_perm
# import os
# from typing import Any
# from concurrent.futures import ThreadPoolExecutor
# import asyncio
import subprocess

# async def test(comm):
#             p=subprocess.Popen(comm.split(" "),stdout=PIPE, stderr=PIPE,)
#             output, error = p.communicate()
#             if p.returncode != 0:
#                 print("bitcoin failed %d %s %s" % (p.returncode, output, error))
#             await asyncio.sleep(30)
#             # if len(p.stderr.readlines())!=0:
#             # 	print(p.stderr.readlines())
#             p.kill()

# #comm='gst-launch-1.0 rtspsrc location=rtsp://wowzaec2demo.streamlock.net/vod/mp4 ! fakesink dump=true'
# comm='gst-launch-1.0 rtspsrc location=rtsp://192.168.200.2 ! fakesink dump=true'
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(comm))

try:
    scheduler_order = "gst-launch-1.0 rtspsrc location=rtsp://192.168.200.2 ! fakesink dump=true"
    return_info = subprocess.Popen(scheduler_order, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        next_line = return_info.stdout.readline()
        return_line = next_line.decode("utf-8", "ignore")
        if return_line == '' and return_info.poll() != None:
            break
        print(return_line)
        ft=open("errorCatch.txt",'a')
        ft.write(return_line)
        ft.write('\n')

    returncode = return_info.wait()
    if returncode:
        raise subprocess.CalledProcessError(returncode, return_info)
except Exception as e:
    print(e)