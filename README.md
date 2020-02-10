# Sustainable Mobility API

This project consists of a Python library and HTTP API for estimating the environmental impact of personal mobility.

## Estimator

The estimator consists of a Python library to calculate CO2 emissions for a transport trip based on the distance and mode. The library has been published to the Python Package Index as [transport-co2](https://pypi.org/project/transport-co2/).

The [README](estimator/README.md) in the [estimator](estimator/) folder also have examples on the library responses, for various modes of transportation.

## API

The API provides an HTTP(s) endpoint to estimate the CO2 emissions for a transport trip. Internally, the API relies on the "transport-co2" estimator library.

Please go into [api](api/) folder to read more about running locally or deploying as docker container or serverless function.

## Roadmap

This project is intended as a proof-of-concept and to generate feedback for future development. See our [project roadmap](https://github.com/maasglobal/sustainable-mobility-api/milestones) for upcoming plans and ideas.

## Support or feedback

If you have ideas for this project or need assistance, please contact us via the [project issue tracker](https://github.com/maasglobal/sustainable-mobility-api/issues).
