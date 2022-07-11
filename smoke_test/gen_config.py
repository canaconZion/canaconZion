# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import json

CONFIG_TEMPLATE = {
	"device": {
		"type": "post",
		"version": "3.0"
	},
	"product": {
		"type": "tuchuan",
		"version": "arm64-v0.2.2-chenl"
	},
	"logLevel": "DY:info*,DY:warn*,DY:error*,DY:debug*",
	"logRotateSize": "10M",
	"jsonEditor": {
		"serverPort": 12001,
		"matrixConfigJson": "/kd_install/config/matrix-config.json"
	},
	"livesrc": {
		"serviceInfoUrl": "http://docker0:9001/drone",
		"srcUrlRule": "rtsp://admin:workhard0106@192.168.10.4",
		"latency": 10,
		"camera": [
			{
				"type": "ipc",
				"name": "TEST01",
				"srcUrl": "rtsp://admin:workhard0106@192.168.10.4"
			}
		]
	},
	"livecamAgora": {
		"adapter": "tencent",
		"option": {
			"agora": {
				"appId": "6250de74233a4d56a58b2419e839e54b",
				"channel": "001",
				"license": "eyJzaWduIjoib0pOd1ZSWUU0d2NydkhlTitWSmR2K0xpWmRMMzdka3E3Y21oVDU5ZVJpcm9CMVp1blJzRTBZZXdralc2RlJKaWR4eWlmWk1WZkZ0bXBQWWx3MjBrOWdxWnZtdUc5TXdVT3lWbHZtR2VSYTVOMTVUTHFxekovN3p0TmVhYnRib1FLWGhyZGFvL0VTMm9jZStLakhDV0w0VlloY3VhQ3o0Slpid2VKaGQxeHV3SmFLVlpCNXp6dDZCTGR1N2N2NS9najZDWEhGR1B2V2xLcGxTTysvQUNyRGJYU1FDbWxibmdMZ1FaTDhTeTNkSUV5QUd4Mmt4YXRMRXZObStGamhJN2Zta0N3cnlpdzJZeW41MDU4KzFISDNFZXZoUTlBeWk2cTBUOWVMRWNDQlRSMkZ6MnFWZ0s0dUZLbmRxKzY4YjIzbDdMdnlEU2VPNVBMaXRBZ2g0dkx3PT0iLCJjdXN0b20iOiIxOTA2MDYiLCJjcmVkZW50aWFsIjoiNGE1ZmEyZWVkZGQyYjJjOWM3YzQxOTlhYWQ0ODIwNWI5YjBjOWJiMTllYWVmZGVhNDk5NmFhOTlmNmRkOTI1MiIsImR1ZSI6IjIwMjIwNzIxIn0="
			},
			"tencent": {
				"appId": "",
				"channel": "",
				"license": "JwPiUkC6Rwql7B06Ic5K72amXqpTs14Y5SPd6zvzCSZp8HYpRdIJ5z/v0K1vIlGEwPGUGFUmRnU+chcu4ZVqQPc7WA1DVPd7svKxny8h9i+RtXgOZCbb+W3LBPphKNOknzM+iuc9uU3vLFIrJ+vP3g/4T/XH0fr/HQQk41pFLXmGF0dnZ/1MAcNMAiOpNnLbyRS9O8Evh/PMHlX+47l9PWM5UsBLLUsFwDN5ndYQ/KxfqkYxXCxYxWS/GL8PjLulRECu3H14chL+hwvFaXDjye9ol9+6EiBRMVD93CKvYUt2/QBPy2M8XqpAePB5UQBdFY3L4/ndTA0U2bODepbiOA==",
				"sdk_config": {
					"device_id": "tencent_duoyi_test04",
					"device_name": "duoyi_test111",
					"device_streams": 1,
					"server_ip": "101.67.8.158",
					"server_port": 2883,
					"rtc_server_ip": "101.67.8.158",
					"rtc_server_port": 3000,
					"log_enable": 1,
					"sdk_mode": "server",
					"streams_config": [
						{
							"fps": 30,
							"bps": 4000,
							"width": 1920,
							"height": 1080,
							"protocol": "outenc",
							"min_bps": 1,
							"codec": 0
						}
					]
				}
			}
		}
	},
	"livecamWebrtc": {
		"adapter": "default",
		"option": {
			"default": {
				"rtmpServer": "rtmp://dev.smt.dyinnovations.com:1935",
				"resolution": "default"
			},
			"ct": {
				"centerServer": "dycenter",
				"serverPort": 9009
			},
			"dy": {
				"clientVersion": 1,
				"VIDEO_MSG_SERVER_HOST": "http://dycenter:1612"
			},
			"autoSwitch": {
				"resolution": "default",
				"rtmpServer": "rtmp://dev.smt.dyinnovations.com:1935"
			}
		},
		"liveStack": "webrtc",
		"webrtcSignal": "ws://dev.smt.dyinnovations.com:8188",
		"srcMode": "shm",
		"h264decPlugin": "vaapi",
		"recodeForM300": False,
		"lowLatency": False,
		"disableOsdClock": True,
		"disableRecode": False,
		"frameTypeReporting": True,
		"idrinterval": 30,
		"resetUrlDel": "http://docker0:9001/api/v1/debug/refreshIframe",
		"resolution": {
			"default": {
				"bitrate": 4000,
				"gop": 60
			},
			"fluency": {
				"bitrate": 500,
				"gop": 60
			},
			"topspeed": {
				"bitrate": 200,
				"gop": 60
			}
		}
	},
	"livecamGb": {
		"SIP_SERVICE_ID": "44010200492000000001",
		"SIP_SERVICE_DOMAIN": "4401020049",
		"SIP_SERVICE_HOST": "121.4.107.199",
		"SIP_SERVICE_PORT": 5060,
		"SIP_CLIENT_NAME": "44030000991327000201",
		"SIP_CLIENT_ID": "44030000991327000201",
		"SIP_CLIENT_PASSWD": "admin123",
		"SIP_CLIENT_HOST": "192.168.6.204",
		"SIP_CLIENT_PORT": 12506,
		"SIP_CLIENT_CHANNEL": "44030000991327000201",
		"SIP_REGISTER_REMAIN": 3600,
		"HEARTBEAT_REMAIN": 5,
		"netProtocol": "tcp",
		"MAX_BAD_HEARTBEAT_NUMBER": 3,
		"GST_CMD_TO_H264PARSE": "--gst-plugin-load=/workdir/dy-livegbd/dist/libgstrtp.so --gst-plugin-load=/workdir/dy-livegbd/dist/libgstmpegpsmux.so rtspsrc location=rtsp://admin:workhard0106@192.168.10.4 protocols=udp-mcast+udp latency=50 ! rtph264depay ! h264parse ! vaapih264dec ! vaapih264enc bitrate=4096 quality-level=7 rate-control=cbr ! video/x-h264,profile=constrained-baseline"
	},
	"livecamGb_2nd": {
		"SIP_SERVICE_ID": "44010200492000000001",
		"SIP_SERVICE_DOMAIN": "4401020049",
		"SIP_SERVICE_HOST": "121.4.107.199",
		"SIP_SERVICE_PORT": 5060,
		"SIP_CLIENT_NAME": "44030000991327000202",
		"SIP_CLIENT_ID": "44030000991327000202",
		"SIP_CLIENT_PASSWD": "admin123",
		"SIP_CLIENT_HOST": "192.168.6.204",
		"SIP_CLIENT_PORT": 12506,
		"SIP_CLIENT_CHANNEL": "44030000991327000202",
		"SIP_REGISTER_REMAIN": 3600,
		"HEARTBEAT_REMAIN": 5,
		"netProtocol": "tcp",
		"MAX_BAD_HEARTBEAT_NUMBER": 3,
		"GST_CMD_TO_H264PARSE": "--gst-plugin-load=/workdir/dy-livegbd/dist/libgstrtp.so --gst-plugin-load=/workdir/dy-livegbd/dist/libgstmpegpsmux.so rtspsrc location=rtsp://admin:workhard0106@192.168.10.4 protocols=udp-mcast+udp latency=50 ! rtph264depay ! h264parse ! vaapih264dec ! vaapih264enc bitrate=4096 quality-level=7 rate-control=cbr ! video/x-h264,profile=constrained-baseline"
	},
	"livecamRtmp": {
		"adapter": "default",
		"option": {
			"default": {
				"rtmpServer": "rtmp://dev.smt.dyinnovations.com:1935",
				"resolution": "default"
			},
			"autoSwitch": {
				"rtmpServer": "rtmp://dev.smt.dyinnovations.com:1935",
				"resolution": "default",
				"rtmpApiUrl": "rtmp://dev.smt.dyinnovations.com:1985"
			},
			"ct": {
				"centerServer": "dycenter",
				"serverPort": 9009,
				"rtmpServer": "rtmp://dycenter:1935",
				"resolution": "default",
				"rule": "[app]/[stream]",
				"config": [
					{
						"stream": "jitou",
						"url": "rtmp://dycenter:1935/live/inside"
					},
					{
						"stream": "weigan",
						"url": "rtmp://dycenter:1935/live/outside"
					}
				]
			},
			"ft": {
				"kafkaHost": "www.pdio.kafka.com:9094",
				"topicCenter": "com.ft.fss.cms",
				"topicNode": "com.ft.fss.cap"
			},
			"defined": {
				"rtmpServer": "rtmp://dycenter:1935",
				"resolution": "default",
				"rule": "live/[app]_[stream]"
			}
		},
		"liveStack": "rtmp",
		"srcMode": "shm",
		"h264decPlugin": "vaapi",
		"recodeForM300": False,
		"lowLatency": False,
		"disableOsdClock": True,
		"disableRecode": False,
		"resolution": {
			"default": {
				"bitrate": 4000,
				"gop": 60
			},
			"topspeed": {
				"bitrate": 200,
				"gop": 60
			},
			"fluency": {
				"bitrate": 500,
				"gop": 60
			},
			"standard": {
				"bitrate": 10000,
				"gop": 60
			},
			"high": {
				"bitrate": 15000,
				"gop": 60
			}
		},
		"cameraResolution": [
			{
				"name": "XIASHI_LEFT",
				"resolution": "default"
			}
		]
	},
	"liverec": {
		"RECORD_MSG_SERVER": "http://docker0:9001",
		"gop": 60,
		"recodeForM300": False,
		"srcMode": "shm",
		"bitrate": 15000,
		"h264decPlugin": "vaapi",
		"maxCapacityMB": "10"
	},
	"livestatus": {
		"ip": [
			"www.baidu.com",
			"192.168.200.3"
		]
	},
	"livenx": {
		"protocols": "tcp"
	}
}

class TuchuanConfigGenerator:
    def __init__(self):
        self._config = CONFIG_TEMPLATE

    def set_any(self, *args):
        value = args[-1]
        paths = args[: -1]
        try:
            target  = self._config
            final_key = paths[-1]
            for k in paths[:-1]:
                target = target[k]
            target[final_key] = value
        except KeyError:
            print("config{} not found".format("".join(map(lambda s: "["+s+"]", paths))))

    def dumps(self):
        return json.dumps(self._config)
