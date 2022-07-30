import sys
import os

try:
    frontUrl="http://app.dyinnovations.com/prod-versions/app-tuchuan-wlan-v0.10/index.html#/janus?livecamId={0}&liveServer=http%3A%2F%2F{1}%3A1612&janusApiSrv=ws%3A%2F%2F{2}%3A8188%2Fjanus" \
    .format(sys.argv[1],sys.argv[2],sys.argv[3])
    print("The front Url is:\n"+frontUrl)
    comm="google-chrome --new-window "+frontUrl.replace("&","\&")
    try:
        os.system(comm)
    except:
        print("请检查google浏览器是否正常")
except IndexError:
    print("请检查是否缺少关键值")