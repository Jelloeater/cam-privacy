import logging
import os

import fastapi

import cam_privacy.main

import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

if os.getenv("LOG_LEVEL") is None:
    logging.basicConfig(level=logging.WARNING)
else:
    logging.basicConfig(level=int(os.getenv("LOG_LEVEL")))


class web_app:
    def __init__(self):
        self.app = FastAPI()

        @self.app.get("/", include_in_schema=False)
        async def root():
            return RedirectResponse(self.app.docs_url)

        @self.app.get("/{hostname}/on")
        async def privacy_on(hostname: str):
            s = cam_privacy.main.privacy_toggle_single(hostname, True)
            r = fastapi.Response()
            r.body(s)
            return r

        @self.app.get("/{hostname}/off")
        async def privacy_off(hostname: str):
            s = cam_privacy.main.privacy_toggle_single(hostname, False)
            r = fastapi.Response()
            r.body(s)
            return r


class Server:
    port = 8080

    @classmethod
    def local_nic(cls):
        import socket

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        nic = s.getsockname()[0]
        s.close()
        return nic

    @classmethod
    def start_server(cls):  # pragma: no cover # TODO Remove when test fixed
        u = uvicorn
        c = u.config.Config(app=web_app().app, host=cls.local_nic(), port=cls.port, proxy_headers=True)
        w = u.Server(c)
        w.run()


if __name__ == "__main__":
    Server().start_server()
