# -*- coding: utf-8 -*-
import platform
import unittest
import utils
import mock_device
import test_tuchuan
import test_argparse
from threading import Thread
#import HtmlTestRunner


if __name__ == '__main__':
    cpu_arch = platform.machine()
    parser = test_argparse.get_app_argparser()
    args = parser.parse_args()

    rtmp_server = args.rtmp_server
    janus_server = args.janus_server
    image_tag = "registry.cn-shenzhen.aliyuncs.com/dyi/matrix-tuchuan-linux:0.2.82-648b591"

    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    # runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个报告文件，将句柄传给stream
    #                     tester="miki",                    # 报告中显示的测试人员
    #                     description="注册接口测试报告",        # 报告中显示的描述信息
    #                     title="自动化测试报告")                 # 报告的标题

    carrier_id = utils.guid()
    aircraft_id = utils.guid()
    httpd_port = utils.get_idle_port()
    httpd = mock_device.get_info_server('0.0.0.0', httpd_port, carrier_id, aircraft_id)
    httpd_thread = Thread(target=httpd.serve_forever)
    httpd_thread.start()

    if cpu_arch in ('x86', 'x86_64'):
        suite.addTest(test_tuchuan.TestTuchuanCase.parametrize(test_tuchuan.TestTuchuanCase, image_tag, rtmp_server, janus_server, f"http://172.17.0.1:{httpd_port}", carrier_id, aircraft_id))
        result = runner.run(suite)
        if len(result.failures) > 0:
            exit(1)
    elif cpu_arch in ('aarch64', ):
        ...
    else:
        print(f'Unkonwn cpu arch: {cpu_arch}')

    httpd.server_close()
    httpd.shutdown()
