from datetime import date

from marstuff.utils import convert


class Rover:
    def __init__(self, id, name, landing_date, launch_date, status):
        self.id = convert(id, int)
        self.name = convert(name, str)
        self.landing_date = convert(landing_date, date)
        self.launch_date = convert(launch_date, date)
        self.status = convert(status, str)
