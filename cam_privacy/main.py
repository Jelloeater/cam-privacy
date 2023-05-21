import json
import os

import amcrest


# Should just use .env file for inputs
def get_camera_single(hostname: str) -> amcrest.ApiWrapper:
    return amcrest.AmcrestCamera(
        host=hostname, port=80, user=os.getenv("USERNAME"), password=os.getenv("PASSWORD")
    ).camera


def privacy_toggle_single(hostname: str, privacy_mode: bool):
    c = get_camera_single(hostname)
    return c.set_privacy(privacy_mode)
