> 调用本机摄像头录制视频并保存

```
sudo gst-launch-1.0 -v v4l2src ! video/x-raw,format=YUY2,framerate=30/1 ! clockoverlay halignment=right valignment=top shaded-background=true font-desc="Sans,36" time-format="%Y-%m-%d %H:%m:%s" ! videoconvert ! x264enc bitrate=1000 ! h264parse ! flvmux ! filesink location=myVideo.flv
``` 