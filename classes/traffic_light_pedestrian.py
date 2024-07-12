import enum


class TrafficLightPedestrianColor(int, enum.Enum):
    red = 0
    green = 1


class TrafficLightPedestrian:
    def __init__(
            self,
            id: str,
            color: enum = TrafficLightPedestrianColor.red,
            timer: int = 0
    ):
        self._id = id
        self._color = color
        self._count = 0
        self._timer = timer
        self._queue = []

    def get_id(self):
        return self._id

    def get_color(self):
        return self._color

    def get_count(self):
        return self._count

    def get_timer(self):
        return self._timer

    def get_queue(self):
        return self._queue

    def set_id(self, id: str):
        self._id = id

    def set_color(self, color: enum):
        self._color = color

    def set_count(self, count: int):
        self._count = count

    def set_timer(self, timer: int):
        self._timer = timer

    def set_queue(self, event: dict):
        self._queue.append(event)

    def send_event(self):
        pass
