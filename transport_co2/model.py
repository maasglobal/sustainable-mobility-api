from enum import Enum


class Mode(Enum):
    """
    Data structure containing grams of CO2/vehicle KM for several modes of transport
    along with average occupancy for each mode.

    Source data:
    CO2 emissions from passenger transport
    from European Environment Agency
    https://www.eea.europa.eu/media/infographics/co2-emissions-from-passenger-transport/view
    """

    def __init__(self, co2_per_vehicle_km: float, average_occupancy: float):
        self.co2_per_vehicle_km = co2_per_vehicle_km
        self.average_occupancy = average_occupancy

    LIGHT_RAIL = (2184, 156)
    SMALL_CAR = (168, 1.5)
    LARGE_CAR = (220, 1.5)
    SCOOTER = (86.4, 1.2)
    BUS = (863, 12.7)
