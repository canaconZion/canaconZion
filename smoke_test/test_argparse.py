# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(description="test launch binary args")

parser.add_argument('--rtmp_server', help='rtmp server to connect to. eg "rtmp://localhost:1935"', default='rtmp://dev.smt.dyinnovations.com:1935')
parser.add_argument('--janus_server', help='janus webrtc signaling server. eg "ws://localhost:8188"', default='ws://dev.smt.dyinnovations.com:8188')
parser.add_argument('--image_tag', help='docker image to test')


def get_app_argparser():
    return parser
