from __future__ import annotations

from datetime import date
from typing import Optional, Union

import httpx

from marstuff.utils import convert, get_name, List

CLIENTS = {}


class Client:
    def __init__(self, api_key: str, base_url: str = "https://api.nasa.gov/mars-photos/api/v1/"):
        self.api_key = api_key
        self.base_url = base_url
        CLIENTS[api_key] = self

        self.ROVERS = make_rovers(self)

        self.perseverance: Rover = self.ROVERS.PERSEVERANCE.value
        self.curiosity: Rover = self.ROVERS.CURIOSITY.value
        self.opportunity: Rover = self.ROVERS.OPPORTUNITY.value
        self.spirit: Rover = self.ROVERS.SPIRIT.value

    def get(self, endpoint, **params):
        params['api_key'] = self.api_key
        return httpx.get(self.base_url + endpoint, params = params).json()

    def get_photos(self, rover: Union[Rover, ROVERS, str], sol: int = None, earth_date: str = None,
                   page_number: Optional[int] = 1, camera: Union[BaseCamera, CAMERAS, str] = None):
        rover_name = get_name(rover, Rover, ROVERS)
        params = {}
        if sol is not None:
            sol = convert(sol, int)
            params['sol'] = sol
        elif earth_date is not None:
            earth_date = convert(earth_date, date)
            params['earth_date'] = earth_date.isoformat()
        if page_number is not None:
            page_number = convert(page_number, int)
            params['page'] = page_number
        if camera is not None:
            camera = get_name(camera, BaseCamera, CAMERAS)
            params['camera'] = camera
        photos = self.get(f"rovers/{rover_name}/photos", **params)
        return convert(photos['photos'], List[Photo])


from marstuff.objects.camera import BaseCamera, Camera, CAMERAS
from marstuff.objects.photo import Photo
from marstuff.objects.rover import make_rovers, Rover, ROVERS
