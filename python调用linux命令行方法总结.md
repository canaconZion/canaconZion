最近需要写一个播放地址拉流检测的脚本，中间调用linux的命令行。经过学习和研究，这里对python调用linux命令行的几种方法进行总结。
## 1. os.system()
> 代码示例
``` python
import os

comm='gst-launch-1.0 rtspsrc location=rtsp://wowzaec2demo.streamlock.net/vod/mp4 ! fakesink dump=true'
os.system(comm)
```
## 2. os.popen()
> 代码实例
```python
import os

comm='gst-launch-1.0 rtspsrc location=rtsp://wowzaec2demo.streamlock.net/vod/mp4 ! fakesink dump=true'
os.popen(comm)
```
## 3. subprocess
> 代码实例
```python
import subprocess

comm='gst-launch-1.0 rtspsrc location=rtsp://wowzaec2demo.streamlock.net/vod/mp4 ! fakesink dump=true'
p=subprocess.Popen(comm.split(" "))
p.kill()
```