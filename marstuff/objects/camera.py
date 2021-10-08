from enum import Enum

from marstuff.bases import Object
from marstuff.utils import convert, Extras


class Camera(Object):
    def __init__(self, id=None, name=None, rover_id=None, full_name=None, **extras):
        self.id = convert(id, int)
        self.name = convert(name, str)
        self.rover_id = convert(rover_id, int)
        self.full_name = convert(full_name, str)
        self.extras: dict = convert(extras, Extras)


class CAMERAS(Enum):
    EDL_RUCAM = "Rover Up-Look Camera"
    EDL_RDCAM = "Rover Down-Look Camera"
    EDL_DDCAM = "Descent Stage Down-Look Camera"
    EDL_PUCAM1 = "Parachute Up-Look Camera A"
    EDL_PUCAM2 = "Parachute Up-Look Camera B"
    NAVCAM_LEFT = "Navigation Camera - Left"
    NAVCAM_RIGHT = "Navigation Camera - Right"
    MCZ_RIGHT = "Mast Camera Zoom - Right"
    MCZ_LEFT = "Mast Camera Zoom - Left"
    FRONT_HAZCAM_LEFT_A = "Front Hazard Avoidance Camera - Left"
    FRONT_HAZCAM_RIGHT_A = "Front Hazard Avoidance Camera - Right"
    REAR_HAZCAM_LEFT = "Rear Hazard Avoidance Camera - Left"
    REAR_HAZCAM_RIGHT = "Rear Hazard Avoidance Camera - Right"
    SKYCAM = "MEDA Skycam"
    SHERLOC_WATSON = "SHERLOC WATSON Camera"
    FHAZ = "Front Hazard Avoidance Camera"
    RHAZ = "Rear Hazard Avoidance Camera"
    MAST = "Mast Camera"
    CHEMCAM = "Chemistry and Camera Complex"
    MAHLI = "Mars Hand Lens Imager"
    MARDI = "Mars Descent Imager"
    NAVCAM = "Navigation Camera"
    PANCAM = "Panoramic Camera"
    MINITES = "Miniature Thermal Emission Spectrometer (Mini-TES)"
