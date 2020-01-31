import connexion
import os
from haversine import haversine
from transport_co2 import estimate_co2, Mode

def verify_origin_destination_coordinates_were_provided(origin_lat, origin_lon, destination_lat, destination_lon):
    # Ensure all origin/destination coordinates were provided
    return (origin_lat and origin_lon and destination_lat and destination_lon)


def get_co2_estimate(transport_mode=None, distance_km=None, vehicle_occupancy=None, origin_lat=None, origin_lon=None, destination_lat=None, destination_lon=None):
    origin_destination_coordinates_were_provided = verify_origin_destination_coordinates_were_provided(
        origin_lat,
        origin_lon,
        destination_lat,
        destination_lon
    )

    if distance_km != None:
        # default to using provided distance
        pass
    elif origin_destination_coordinates_were_provided:
        # Calculate distance from origin/destination
        origin = (origin_lat, origin_lon)
        destination = (destination_lat, destination_lon)
        distance_km = haversine(origin, destination)
    else:
        return {
            "error": "Not enough information was provided to calculate CO2 estimate."
        }
    
    if isinstance(transport_mode, str):
        transport_mode = Mode[transport_mode.upper()]

    if vehicle_occupancy == None:
        vehicle_occupancy = transport_mode.average_occupancy

    co2_estimate = estimate_co2(mode=transport_mode, distance_in_km=distance_km, occupancy=vehicle_occupancy)

    return_data = {
        "transport_mode": str(transport_mode),
        "vehicle_occupancy": vehicle_occupancy,
        "distance_km": distance_km,
        "co2_estimate": co2_estimate
    }

    return return_data

if __name__ == "__main__":
    app = connexion.FlaskApp(__name__)
    app.add_api("specification.json")
    app.run(port=8080)
