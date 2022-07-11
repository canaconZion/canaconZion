# -*- utf-8 -*-
from audioop import add
from concurrent.futures import ThreadPoolExecutor
import asyncio
import http.server
import socketserver
import json
from typing import Tuple
import uuid
import requests
import sys

def get_device_info(carrider_id, aircraft_id):
    return {
        "carrierId": carrider_id,
        "drones": [ { "ip": '172.17.0.1', "aircraftId": aircraft_id }]
    }


class MockDeviceHttpRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self, *args, **kwargs):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps(get_device_info(self.carrier_id, self.aircraft_id)).encode())


def get_info_server(addr, port, carrier_id, aircraft_id):
    handler_cls = MockDeviceHttpRequestHandler
    handler_cls.carrier_id = carrier_id
    handler_cls.aircraft_id = aircraft_id
    httpd = socketserver.TCPServer((addr, port), handler_cls)
    print("will serve at {}:{}".format(addr, port))
    return httpd
 

async def connect_stdin_stdout():
    loop = asyncio.get_event_loop()
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    w_transport, w_protocol = await loop.connect_write_pipe(asyncio.streams.FlowControlMixin, sys.stdout)
    writer = asyncio.StreamWriter(w_transport, w_protocol, reader, loop)
    return reader, writer


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('--host')
    parser.add_argument('--port')
    args = parser.parse_args()

    
    host = args.host
    port = args.port
    httpd = get_info_server(host, port, "001", "001")
    loop = asyncio.get_event_loop()
    loop.run_in_executor(ThreadPoolExecutor(), httpd.serve_forever)
    resp = requests.get(f'http://{host}:{port}')
    info = json.loads(resp.text)
    async def read_stdin():
        reader, _ = await connect_stdin_stdout()
        while True:
            input: str = (await reader.readline()).decode()
            print(input)
            if input.strip() == 'quit':
                print("quit!")
                break
        httpd.server_close()
        httpd.shutdown()

    loop.create_task(read_stdin())
    loop.run_forever()
