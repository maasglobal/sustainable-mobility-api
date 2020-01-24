import connexion
from transport_co2 import estimate_co2


def get_co2_estimate():
    return "hello world"


app = connexion.FlaskApp(__name__)
app.add_api("specification.json")
app.run(port=8080)
