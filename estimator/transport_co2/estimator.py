# -*- coding: utf-8 -*-

"""Estimator as a function."""

from typing import Optional, Union
from .model import Fuel, Mode


def estimate_co2(
    mode: Union[str, Mode],
    distance_in_km: float,
    *,
    co2_per_vehicle_km: Optional[float] = None,
    occupancy: Optional[float] = None
) -> float:
    """
    Estimate CO2 usage for transport mode based on KM and optional vehicle occupancy.

    Keyword arguments:
        mode -- vehicle mode (limited to allowed values, required)
        distance_in_km -- distance for the trip in kilometers (required)
        co2_per_vehicle_km -- CO2 emission in grams per vehicle km
            (optional, uses mode average if falsey)
        occupancy -- vehicle occupancy (optional, uses mode average if falsey)
    """

    if isinstance(mode, str):
        mode = Mode[mode.upper()]

    return mode.estimate_co2(
        distance_in_km=distance_in_km,
        co2_per_vehicle_km=co2_per_vehicle_km,
        occupancy=occupancy,
    )


def estimate_fuel_co2_g(
    fuel: Union[str, Fuel],
    litres: float,
    *,
    co2_g_per_litre: Optional[float] = None
) -> float:
    """
    Estimate CO2 emissions based on litre of fuel consumed.

    Keyword arguments:
        fuel -- type of fuel used (limited to allowed values, required)
        litres -- litres of fuel consumed
        co2_g_per_litre -- grams of CO2 released when consuming a litre of given fuel type (optional)
    """

    if isinstance(fuel, str):
        fuel = Fuel[fuel.upper()]

    return fuel.estimate_co2_g(
        litres=litres,
        co2_g_per_litre=co2_g_per_litre
    )
