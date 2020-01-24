import connexion


def hello_world():
    return "hello world"


app = connexion.FlaskApp(__name__)
app.add_api("specification.json")
app.run(port=8080)
