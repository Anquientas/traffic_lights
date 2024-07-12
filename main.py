from classes.traffic_light_car import (
    TrafficLightCar,
    TrafficLightCarColor
)
from classes.traffic_light_pedestrian import (
    TrafficLightPedestrian,
    TrafficLightPedestrianColor
)
from config import (
    TRAFFIC_LIGHTS_CAR_IDS,
    TRAFFIC_LIGHTS_PEDESTRIAN_IDS,
    INITIAL_GREEN_TRAFFIC_LIGHT_CAR_ID,
    INITIAL_GREEN_TRAFFIC_LIGHTS_PEDESTRIAN_IDS
)


def init_traffic_lights():
    traffic_lights = []
    for identifier in TRAFFIC_LIGHTS_CAR_IDS:
        traffic_lights.append(
            TrafficLightCar(id=identifier)
        )
    traffic_lights.append(
        TrafficLightCar(
            id=INITIAL_GREEN_TRAFFIC_LIGHT_CAR_ID,
            color=TrafficLightCarColor.green,
            timer=10
        )
    )
    for identifier in TRAFFIC_LIGHTS_PEDESTRIAN_IDS:
        traffic_lights.append(
            TrafficLightPedestrian(id=identifier)
        )
    for identifier in INITIAL_GREEN_TRAFFIC_LIGHTS_PEDESTRIAN_IDS:
        traffic_lights.append(
            TrafficLightCar(
                id=identifier,
                color=TrafficLightPedestrianColor.green,
                timer=10
            )
        )
    return traffic_lights


def main():
    traffic_lights = init_traffic_lights()
    print(traffic_lights)


if __name__ == '__main__':
    main()
