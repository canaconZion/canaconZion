import os
import subprocess

comm='gst-launch-1.0 rtspsrc location=rtsp://wowzaec2demo.streamlock.net/vod/mp4 ! fakesink dump=true'
p=subprocess.Popen(comm.split(" "))
#p.kill()