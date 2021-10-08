import random
from enum import Enum
from typing import Optional

from marstuff.bases import Object
from marstuff.objects.rover import CLIENT_ROVERS, Rover
from marstuff.utils import convert, Extras


class BaseCamera:
    pass


class Camera(Object, BaseCamera):
    def __init__(self, id=None, name=None, rover_id=None, full_name=None, **extras):
        self.id = convert(id, int)
        self.name = convert(name, str)
        self.rover_id = convert(rover_id, int)
        self.full_name = convert(full_name, str)
        self.extras: dict = convert(extras, Extras)


class CameraClient(BaseCamera):
    def __init__(self, name: str, full_name: str, rover: Rover = None):
        self.name = name
        self.full_name = full_name
        self._rover = rover

    @property
    def rover(self) -> Rover:
        if CLIENT_ROVERS:
            return random.choice(CLIENT_ROVERS.values())
        raise ValueError('No Rovers Available!!')

    def get_photos(self, sol: int = None, earth_date: str = None, page_number: Optional[int] = 1):
        return self.rover.get_photos(sol, earth_date, page_number, self)

    def get_photos_by_sol(self, sol: int = None, page_number: Optional[int] = 1):
        return self.get_photos(sol, None, page_number)

    def get_photos_by_earth_date(self, earth_date: str = None, page_number: Optional[int] = 1):
        return self.get_photos(None, earth_date, page_number)

    def get_all_photos(self, sol: int = None, earth_date: str = None):
        return self.get_photos(sol, earth_date, None)

    def get_all_photos_by_sol(self, sol: int = None):
        return self.get_all_photos(sol, None)

    def get_all_photos_by_earth_date(self, earth_date: str = None):
        return self.get_all_photos(None, earth_date)


class CAMERAS(Enum):
    EDL_RUCAM = CameraClient("EDL_RUCAM", "Rover Up-Look Camera")
    EDL_RDCAM = CameraClient("EDL_RDCAM", "Rover Down-Look Camera")
    EDL_DDCAM = CameraClient("EDL_DDCAM", "Descent Stage Down-Look Camera")
    EDL_PUCAM1 = CameraClient("EDL_PUCAM1", "Parachute Up-Look Camera A")
    EDL_PUCAM2 = CameraClient("EDL_PUCAM2", "Parachute Up-Look Camera B")
    NAVCAM_LEFT = CameraClient("NAVCAM_LEFT", "Navigation Camera - Left")
    NAVCAM_RIGHT = CameraClient("NAVCAM_RIGHT", "Navigation Camera - Right")
    MCZ_RIGHT = CameraClient("MCZ_RIGHT", "Mast Camera Zoom - Right")
    MCZ_LEFT = CameraClient("MCZ_LEFT", "Mast Camera Zoom - Left")
    FRONT_HAZCAM_LEFT_A = CameraClient("FRONT_HAZCAM_LEFT_A", "Front Hazard Avoidance Camera - Left")
    FRONT_HAZCAM_RIGHT_A = CameraClient("FRONT_HAZCAM_RIGHT_A", "Front Hazard Avoidance Camera - Right")
    REAR_HAZCAM_LEFT = CameraClient("REAR_HAZCAM_LEFT", "Rear Hazard Avoidance Camera - Left")
    REAR_HAZCAM_RIGHT = CameraClient("REAR_HAZCAM_RIGHT", "Rear Hazard Avoidance Camera - Right")
    SKYCAM = CameraClient("SKYCAM", "MEDA Skycam")
    SHERLOC_WATSON = CameraClient("SHERLOC_WATSON", "SHERLOC WATSON Camera")
    FHAZ = CameraClient("FHAZ", "Front Hazard Avoidance Camera")
    RHAZ = CameraClient("RHAZ", "Rear Hazard Avoidance Camera")
    MAST = CameraClient("MAST", "Mast Camera")
    CHEMCAM = CameraClient("CHEMCAM", "Chemistry and Camera Complex")
    MAHLI = CameraClient("MAHLI", "Mars Hand Lens Imager")
    MARDI = CameraClient("MARDI", "Mars Descent Imager")
    NAVCAM = CameraClient("NAVCAM", "Navigation Camera")
    PANCAM = CameraClient("PANCAM", "Panoramic Camera")
    MINITES = CameraClient("MINITES", "Miniature Thermal Emission Spectrometer (Mini-TES)")
