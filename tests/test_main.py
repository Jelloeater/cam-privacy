import os
from multiprocessing import Process
from time import sleep

import requests
from dotenv import load_dotenv

import cam_privacy.webserver as web
import cam_privacy.main

load_dotenv()
os.environ.setdefault("TEST_MODE", str(True))  # To break out of color cycle loop


class Test_API_full:
    background_server = Process(target=web.Server.start_server, daemon=True)

    @classmethod
    def setup_class(cls):
        cls.background_server.start()
        sleep(0.5)  # Wait for server to start

    @classmethod
    def teardown_class(cls):
        cls.background_server.terminate()

    def test_base_url(self):
        r = requests.get(url="http://" + web.Server.local_nic() + ":" + str(web.Server.port))
        assert r.status_code == 200


class TestMain:
    def test_privacy_on(self):
        cam_privacy.main.privacy_toggle(True)
