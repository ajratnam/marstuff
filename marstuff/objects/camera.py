from marstuff.utils import convert


class Camera:
    def __init__(self, id, name, rover_id, full_name):
        self.id = convert(id, int)
        self.name = convert(name, str)
        self.rover_id = convert(rover_id, int)
        self.full_name = convert(full_name, str)
