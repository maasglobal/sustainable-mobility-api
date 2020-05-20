"""Connexion web app"""

import connexion

app = connexion.FlaskApp(__name__)
app.add_api("specification.json") 


if __name__ == "__main__":
    app.run(port=8080)