# -*- coding: utf-8 -*-

"""Serverless handler."""

import json
import logging

from transport_co2 import Mode

from api import get_co2_estimate

LOGGER = logging.getLogger(__name__)


def strtofloat(val):
    """Parse str to float."""
    if isinstance(val, str):
        val = float(val)
    return val


# pylint: disable=unused-argument
def post(event, context):
    """Serverless handler."""

    try:
        params = event.get("queryStringParameters", dict())
        if not params:
            response = {
                "statusCode": 400,
                "body": json.dumps({"error": "No parameters provided"}),
            }
            return response

        LOGGER.info(
            "estimate-co2 sourceIp=%s userAgent=%s, input=%s",
            event["requestContext"]["identity"]["sourceIp"]
            if event.get("requestContext")
            else "?",
            event["requestContext"]["identity"]["userAgent"]
            if event.get("requestContext")
            else "?",
            params,
        )

        transport_mode = params.get("transport_mode")
        if isinstance(transport_mode, str):
            transport_mode = Mode[transport_mode.upper()]

        distance_km = strtofloat(params.get("distance_km"))
        vehicle_occupancy = strtofloat(params.get("vehicle_occupancy"))
        origin_lat = strtofloat(params.get("origin_lat"))
        origin_lon = strtofloat(params.get("origin_lon"))
        destination_lat = strtofloat(params.get("destination_lat"))
        destination_lon = strtofloat(params.get("destination_lon"))

        estimate = get_co2_estimate(
            transport_mode=transport_mode,
            distance_km=distance_km,
            vehicle_occupancy=vehicle_occupancy,
            origin_lat=origin_lat,
            origin_lon=origin_lon,
            destination_lat=destination_lat,
            destination_lon=destination_lon,
        )

        if estimate.get("error"):
            response = {
                "statusCode": 400,
                "body": json.dumps({"error:": estimate.get("error")}),
            }
            return response

        response = {
            "statusCode": 200,
            "body": json.dumps({"input": params, "result": estimate}),
        }
        return response

    except Exception:
        LOGGER.exception("Got exception processing request: %r", event)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error processing request"}),
        }
