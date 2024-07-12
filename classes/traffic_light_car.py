import enum


class TrafficLightCarColor(int, enum.Enum):
    red = 0
    yellow = 1
    green = 2


class TrafficLightCar:
    def __init__(
            self,
            id: str,
            color: enum = TrafficLightCarColor.red,
            timer: int = 0
    ):
        self._id = id
        self._color = color
        self._count = 0
        self._timer = timer
        self._queue = []

    @property
    def id(self):
        return self._id

    @property
    def color(self):
        return self._color

    @property
    def count(self):
        return self._count

    @property
    def timer(self):
        return self._timer

    @property
    def queue(self):
        return self._queue

    @id.setter
    def id(self, id: str):
        self._id = id

    @color.setter
    def color(self, color: enum):
        self._color = color

    @count.setter
    def count(self, count: int):
        self._count = count

    @timer.setter
    def timer(self, timer: int):
        self._timer = timer

    @queue.setter
    def queue(self, event: dict):
        self._queue.append(event)

    def send_event(self):
        pass