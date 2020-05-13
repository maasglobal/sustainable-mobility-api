# -*- coding: utf-8 -*-

"""Modes along with their data and estimator."""

from enum import Enum
from statistics import mean
from typing import Optional


class Fuel(Enum):
    """
    Data structure for estimating grams of CO2 per litre of various fuel types.

    Source data:
    Learn the facts: Fuel consumption and CO2
    from Natural Resources Canada
    https://www.nrcan.gc.ca/sites/www.nrcan.gc.ca/files/oee/pdf/transportation/fuel-efficient-technologies/autosmart_factsheet_6_e.pdf
    """

    PETROL = 2_290
    ETHANOL_10 = 2_210
    ETHANOL_85 = 1_610
    DIESEL = 2_660
    BIODIESEL_5 = 2_650
    BIODIESEL_20 = 2_620

    def estimate_co2_g(
        self, litres: float, *, co2_g_per_litre: Optional[float] = None
    ) -> float:
        """
        Estimate CO2 grams produced for fuel type.

        Keyword arguments:
            litres -- total litres of fule combusted (required)
            co2_g_per_litre -- CO2 emission in grams per litre of fuel
                (optional, uses fuel type average if falsey)
        """

        co2_g_per_litre = co2_g_per_litre or self.value
        return co2_g_per_litre * litres


class Mode(Enum):
    """
    Data structure containing grams of CO2/vehicle KM for several modes of transport
    along with average occupancy for each mode.

    See the library README for sources and a description of how we arrive at these CO2 values.
    """

    def __init__(self, avg_co2_per_vehicle_km: float, avg_occupancy: float):
        self.avg_co2_per_vehicle_km = avg_co2_per_vehicle_km
        self.avg_occupancy = avg_occupancy

    LIGHT_RAIL = (2184, 156)
    SMALL_CAR = (168, 1.5)
    LARGE_CAR = (220, 1.5)
    SCOOTER = (86.4, 1.2)
    BUS = (863, 12.7)

    # Additional OTP modes
    WALK = (0, 1)
    BICYCLE = (0, 1)
    CAR = (mean([SMALL_CAR[0], LARGE_CAR[0]]), 1.5)
    TRAM = LIGHT_RAIL
    SUBWAY = LIGHT_RAIL
    RAIL = LIGHT_RAIL
    FERRY = (15014.4, 184)
    CABLE_CAR = LIGHT_RAIL
    GONDOLA = LIGHT_RAIL
    FUNICULAR = LIGHT_RAIL
    TRANSIT = BUS
    LEG_SWITCH = (0, 1)
    AIRPLANE = (25080, 88)

    def estimate_co2(
        self,
        distance_in_km: float,
        *,
        co2_per_vehicle_km: Optional[float] = None,
        occupancy: Optional[float] = None,
    ) -> float:
        """
        Estimate CO2 usage for transport mode based on KM and optional vehicle occupancy.

        Keyword arguments:
            distance_in_km -- distance for the trip in kilometers (required)
            co2_per_vehicle_km -- CO2 emission in grams per vehicle km
                (optional, uses mode average if falsey)
            occupancy -- vehicle occupancy (optional, uses mode average if falsey)
        """

        co2_per_vehicle_km = co2_per_vehicle_km or self.avg_co2_per_vehicle_km
        # occupancy should be above zero
        occupancy = occupancy or self.avg_occupancy

        return co2_per_vehicle_km * distance_in_km / occupancy
