#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from haversine import haversine
from transport_co2 import estimate_co2, Mode


def verify_coordinates_were_provided(origin, destination):
    """Ensure all origin/destination coordinates were provided."""
    return (
        origin
        and destination
        and origin["latitude"]
        and origin["longitude"]
        and destination["latitude"]
        and destination["longitude"]
    )


def get_co2_estimate(
    transport_mode=None,
    origin=None,
    destination=None,
    distance_km=None,
    vehicle_occupancy=None,
    *args,
    **kwargs
):
    """
    Estimate CO2 for a given leg, preserving original properties
    
    Note: we do not use the keyword arguments here.
    """

    coordinates_were_provided = verify_coordinates_were_provided(origin, destination)

    if distance_km is not None:
        # default to using provided distance
        pass
    elif coordinates_were_provided:
        # Calculate distance from origin/destination
        origin = (origin["latitude"], origin["longitude"])
        destination = (destination["latitude"], destination["longitude"])

        distance_km = haversine(origin, destination)
    else:
        return {
            "error_message": "Not enough information was provided to calculate CO2 estimate."
        }

    mode = Mode[transport_mode]

    if vehicle_occupancy is None:
        vehicle_occupancy = mode.avg_occupancy

    co2_estimate = mode.estimate_co2(
        distance_in_km=distance_km, occupancy=vehicle_occupancy
    )

    # CO2 estimate dictionary should only include the estimate
    # and component values used for the calculation
    return {
        "transport_mode": transport_mode,
        "vehicle_occupancy": vehicle_occupancy,
        "distance_km": distance_km,
        "co2_estimate": co2_estimate,
    }


def estimate_co2(body):
    # Create a dictionary with CO2 estimate and original request object
    co2_estimates = [
        {"co2_estimate": get_co2_estimate(**leg), "request_object": leg} for leg in body
    ]

    return co2_estimates
