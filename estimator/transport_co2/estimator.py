# -*- coding: utf-8 -*-

"""Estimator as a function."""

from typing import Optional, Union
from .model import Mode


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
