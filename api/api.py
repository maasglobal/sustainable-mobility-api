#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from haversine import haversine
from transport_co2 import estimate_co2, Mode


def verify_coordinates_were_provided(
    origin_lat, origin_lon, destination_lat, destination_lon
):
    """Ensure all origin/destination coordinates were provided."""
    return origin_lat and origin_lon and destination_lat and destination_lon


def get_co2_estimate(
    transport_mode=None,
    distance_km=None,
    vehicle_occupancy=None,
    origin_lat=None,
    origin_lon=None,
    destination_lat=None,
    destination_lon=None,
):
    """Entry point for connexion as specified by operationId in specification.json"""

    coordinates_were_provided = verify_coordinates_were_provided(
        origin_lat, origin_lon, destination_lat, destination_lon
    )

    if distance_km is not None:
        # default to using provided distance
        pass
    elif coordinates_were_provided:
        # Calculate distance from origin/destination
        origin = (origin_lat, origin_lon)
        destination = (destination_lat, destination_lon)
        distance_km = haversine(origin, destination)
    else:
        return {
            "error": "Not enough information was provided to calculate CO2 estimate."
        }, 400

    if isinstance(transport_mode, str):
        transport_mode = Mode[transport_mode.upper()]

    if vehicle_occupancy is None:
        vehicle_occupancy = transport_mode.average_occupancy

    co2_estimate = estimate_co2(
        mode=transport_mode, distance_in_km=distance_km, occupancy=vehicle_occupancy
    )

    return_data = {
        "transport_mode": transport_mode.name
        if isinstance(transport_mode, Mode)
        else transport_mode,
        "vehicle_occupancy": vehicle_occupancy,
        "distance_km": distance_km,
        "co2_estimate": co2_estimate,
    }

    return return_data, 200
