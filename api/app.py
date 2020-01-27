import connexion
from transport_co2 import estimate_co2


def get_co2_estimate(transport_mode=None, distance_km=None):

    if transport_mode != None and distance_km != None:
        co2_estimate = estimate_co2(
            mode=transport_mode, distance_in_km=distance_km)

        return {
            "co2_estimate": co2_estimate,
        }


app = connexion.FlaskApp(__name__)
app.add_api("specification.json")
app.run(port=8080)
