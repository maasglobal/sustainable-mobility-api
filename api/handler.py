import json
import os
from app import get_co2_estimate
from transport_co2 import Mode

def strtofloat(val):
    if isinstance(val, str):
        val = float(val)
    return val

def post(event, context):
    try:
        vars = event.get("queryStringParameters", dict())
        if vars != None:
            print(f'estimate-co2 sourceIp={event["requestContext"]["identity"]["sourceIp"]} userAgent={event["requestContext"]["identity"]["userAgent"]}, input={vars}')
            
            transport_mode = vars.get("transport_mode")
            if isinstance(transport_mode, str):
                transport_mode = Mode[transport_mode.upper()]

            distance_km = strtofloat(vars.get("distance_km"))
            vehicle_occupancy = strtofloat(vars.get("vehicle_occupancy"))
            origin_lat = strtofloat(vars.get("origin_lat"))
            origin_lon = strtofloat(vars.get("origin_lon"))
            destination_lat = strtofloat(vars.get("destination_lat"))
            destination_lon = strtofloat(vars.get("destination_lon"))

            estimate = get_co2_estimate(
                transport_mode = transport_mode,
                distance_km = distance_km,
                vehicle_occupancy = vehicle_occupancy, 
                origin_lat = origin_lat, 
                origin_lon = origin_lon,
                destination_lat = destination_lat, 
                destination_lon = destination_lon
            )

            if estimate.get("error") == None:
                response = {
                    "statusCode": 200,
                    "body": json.dumps({
                        "input": vars,
                        "result": estimate
                    })
                }
                return response
            else:
                response = {
                    "statusCode": 400,
                    "body": json.dumps({
                        "error:": estimate.get("error")
                    })
                }
                return response
        else:
            response = {
                "statusCode": 400,
                "body": json.dumps({
                    "error:": "No parameters provided",
                })
            }
            return response
    except Exception as err:
        print(f"Got exception processing request: {type(err)}: {err}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error:": "Internal server error processing request"
            })
        }