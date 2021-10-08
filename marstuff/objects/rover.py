import random
from enum import Enum
from typing import Optional, Union

from marstuff.client import Client, CLIENTS
from marstuff.objects.camera import BaseCamera, CAMERAS

CLIENT_ROVERS = []


class Rover:
    def __init__(self, name: str, client: Client = None):
        self.name: str = name
        self._client = client
        if self._client:
            CLIENT_ROVERS.append(self)

    def add_client(self, client):
        if not isinstance(client, Client):
            raise TypeError(f"Expected Client, got {client}")
        if self._client and self in CLIENT_ROVERS:
            CLIENT_ROVERS.remove(self)
        return self.__class__(self.name, client)

    @property
    def client(self) -> Client:
        if CLIENTS:
            return random.choice(CLIENTS.values())
        raise ValueError('No Clients Available!!')

    def get_photos(self, sol: int = None, earth_date: str = None, page_number: Optional[int] = 1,
                   camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.client.get_photos(self, sol, earth_date, page_number, camera)


class ROVERS(Enum):
    PERSEVERANCE = Rover("Perseverance")
    CURIOSITY = Rover("Curiosity")
    OPPORTUNITY = Rover("Opportunity")
    SPIRIT = Rover("Spirit")
