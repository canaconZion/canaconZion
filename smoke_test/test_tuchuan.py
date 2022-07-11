import unittest
import asyncio
import os
import tempfile

import scout_janus
import gen_config
import utils
import subprocess
import time

class TestTuchuanCase(unittest.TestCase):
    
    def __init__(self, methodName: str, image_tag: str, rtmp_server: str, webrtc_server: str, src_info_url:str, carrier_id, aircraft_id) -> None:
        super().__init__(methodName)
        self.image_tag = image_tag
        self.rtmp_server = rtmp_server
        self.webrtc_server = webrtc_server
        self.src_info_url = src_info_url
        self.carrier_id = carrier_id
        self.aircraft_id = aircraft_id
        self.config_generator = gen_config.TuchuanConfigGenerator()
        self.async_event_loop = asyncio.new_event_loop()
        # --- --- ---
        self.config_generator.set_any('livesrc', 'serviceInfoUrl', self.src_info_url)

    @staticmethod
    def parametrize(cls, *args, **kwargs):
        loader = unittest.TestLoader()
        testnames = loader.getTestCaseNames(cls)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(cls(name, *args, **kwargs))
        return suite

    def setUp(self) -> None:
        print('setup')
        _, self.temp_config_file = tempfile.mkstemp(dir='/tmp', prefix="tuchuan_config_")
        print("tmp conf file: ", self.temp_config_file)
        _, self.temp_service_file = tempfile.mkstemp(dir='/tmp')
        with open(self.temp_config_file, 'w') as f:
            f.write(self.config_generator.dumps())
        self.container_name = utils.guid()
        utils.run_tuchuan_container(self.image_tag, self.temp_config_file, name=self.container_name)
        return super().setUp()

    def tearDown(self) -> None:
        print('teardown')
        os.system(f"docker rm -f {self.container_name}")
        if os.path.exists(self.temp_config_file):
            os.remove(self.temp_config_file)
        if os.path.exists(self.temp_service_file):
            os.remove(self.temp_service_file)
        return super().tearDown()

    def test_livesrc(self) -> None:
        time.sleep(10)
        self.assertTrue(os.path.exists('/tmp/livesrc_TEST01'))

    def test_rtmp(self) -> None:
        time.sleep(15)
        p = subprocess.Popen(f"gst-launch-1.0 rtmpsrc location={self.rtmp_server}:/{self.carrier_id}/TEST01 ! watchdog ! fakesink".split(' '))
        time.sleep(10)
        self.assertIsNone(p.poll(), "pull rtmp stream failed!")
        p.terminate()
        

    def test_webrtc(self) -> None:
        scout = scout_janus.ScoutJanus(self.webrtc_server, self.carrier_id, "{}_{}".format(self.carrier_id, "TEST01"))
        time.sleep(20)
        scout.scout()
        self.assertTrue(scout.result, "target stream not published!")


if __name__ == '__main__':
    unittest.main()
