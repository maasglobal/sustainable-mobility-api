import json
from app import get_co2_estimate
from transport_co2 import Mode

def post(event, context):
    vars = event.get("queryStringParameters", dict())
    estimate = get_co2_estimate(
        vars.get("transport_mode", None), 
        vars.get("distance_km", None), 
        vars.get("vehicle_occupancy", None), 
        vars.get("origin_lat", None), 
        vars.get("origin_lon", None), 
        vars.get("destination_lat", None), 
        vars.get("destination_lon", None)
    )

    response = {
        "statusCode": 200,
        "input:": json.dumps(vars),
        "result": estimate
    }

    return response
