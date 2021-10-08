from datetime import date

from marstuff.objects.camera import Camera
from marstuff.objects.rover import Rover
from marstuff.bases import Object
from marstuff.utils import convert, Extras


class Photo(Object):
    def __init__(self, id=None, sol=None, camera=None, img_src=None, earth_date=None, rover=None, **extras):
        self.id = convert(id, int)
        self.sol = convert(sol, int)
        self.camera = convert(camera, Camera)
        self.img_src = convert(img_src, str)
        self.earth_date = convert(earth_date, date)
        self.rover = convert(rover, Rover)
        self.extras: dict = convert(extras, Extras)
