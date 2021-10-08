import typing
from datetime import date, datetime

import httpx

from marstuff.objects.photo import Photo
from marstuff.objects.rover import Rover, ROVERS

from marstuff.utils import convert, get_rover_name, List, Union


class Client:
    def __init__(self, api_key: str, base_url: str = "https://api.nasa.gov/mars-photos/api/v1/"):
        self.api_key = api_key
        self.base_url = base_url

    def get(self, endpoint, **params):
        params['api_key'] = self.api_key
        return httpx.get(self.base_url + endpoint, params=params).json()

    def get_rover_photos_on_sol(self, rover: typing.Union[Rover, ROVERS, str], sol: int):
        rover_name = get_rover_name(rover)
        sol = convert(sol, int)
        photos = self.get(f"rovers/{rover_name}/photos", sol=sol)
        return convert(photos['photos'], List[Photo])
