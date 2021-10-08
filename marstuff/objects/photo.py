from datetime import date

from marstuff.objects.camera import Camera
from marstuff.objects.rover import Rover
from marstuff.utils import convert


class Photo:
    def __init__(self, id, sol, camera, img_src, earth_date, rover):
        self.id = convert(id, int)
        self.sol = convert(sol, int)
        self.camera = convert(camera, Camera)
        self.img_src = convert(img_src, ImageLink)
        self.earth_date = convert(earth_date, date)
        self.rover = convert(rover, Rover)
