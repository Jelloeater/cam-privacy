import json
import os

import amcrest

# Should just use .env file for inputs


def get_cameras() -> list[amcrest.ApiWrapper]:
    import amcrest

    cameras = json.loads(os.getenv("CAMERAS"))
    cam_out = []
    for i in cameras:
        cam = amcrest.AmcrestCamera(host=i, port=80, user=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
        cam_out.append(cam.camera)
    return cam_out


def privacy_toggle(privacy_mode: bool):
    for i in get_cameras():
        i.set_privacy(privacy_mode)
    return
