# Transport CO2

Calculate CO2 (equivalent) emissions for a given transport trip and provide a simple interpretation of the result.

Install from [PyPI](https://pypi.org/project/transport-co2/) via
```bash
pip install transport-co2
```

## Usage examples

You can list the currently supported modes like so:
```python
from transport_co2 import Mode
list(Mode)
```
Each `Mode` allows you to estimate the CO2 emission per passenger for a journey given its distance (in km):
```python
Mode.SMALL_CAR.estimate_co2(distance_in_km=100)
# 11200.0
```
This estimate is based on an average occupancy (in this example `1.5`). You can also specify the occupancy:
```python
Mode.SMALL_CAR.estimate_co2(distance_in_km=100, occupancy=3)
# 5600.0
```
If you don't want to work with the `Mode` enum, you can instead work with the `estimate_co2` function:
```python
from transport_co2 import estimate_co2
estimate_co2(mode="light_rail", distance_in_km=100)
# 1400.0
```
You can also specify the occupancy like above:
```python
estimate_co2(mode="light_rail", distance_in_km=100, occupancy=250)
# 873.6
```

## Running unit tests
In order to run the unit tests for this project:

1. activate the virtual environment with `pipenv shell`
2. run `pytest`

## Goals

This project is intended to be used to help raise awareness about the cost of transportation choices, so people can make informed decisions.

## Initial focus

We are initially focused on ground (road and rail) transport, as it is the most significant source on transport greenhouse gas emissions.

## API Design

This library intends to provide:

- a statistical estimate of greenhouse gase emissions given information about a trip (origin/destination, mode, and/or distance)
- a simple interpretation of the statistical emissions estimate, in terms such as "high" or "low"

## Research

The carbon estimates produced by this model may be based on the following resources. A full description of the model, including data sources, will be provided as the library takes shape.

- European Environment Agency [CO2 emissions from passenger transport](https://www.eea.europa.eu/media/infographics/co2-emissions-from-passenger-transport/view)

For modes not covered in the EEA infographic, we have used approximations and averages to provide estimates for all OpenTripPlanner modes.

For Ferry mode calculation we use the average of 6.8 MJ per passenger kilometer with an average occupancy of 184 (Schiller & Kenworthy, 2017, pp. 142–143). We then used the procedure described in the following section in order to map megajoules to grams CO2 per passenger kilometer.

With an average of 12g CO2 eq. per megajoule (The International Council on Clean Transportation, 2010), we estimate that each ferry passenger kilometer approximates to 81.6 g CO2.

### Bibliography
- The International Council on Clean Transportation. (2010). Carbon Intensity of Crude Oil in Europe. Retrieved from https://theicct.org/sites/default/files/ICCT_crudeoil_Eur_Dec2010_sum.pdf
- Schiller, P. L., & Kenworthy, J. R. (2017). An Introduction to Sustainable Transportation. Abingdon, United Kingdom: Routledge.


### Further reading
Further improvements to the model may come from other sources, such as the following.

- IPCC AR5 [Chapter 8 - Transport](https://www.ipcc.ch/site/assets/uploads/2018/02/ipcc_wg3_ar5_chapter8.pdf)
- Wikipedia: [Environmental impact of transport](https://en.wikipedia.org/wiki/Environmental_impact_of_transport)

## Attribution

Initial package structure forked from [navdeep-G/setup.py](https://github.com/navdeep-G/setup.py).

Friendly nod to [jamiebull1/transport-carbon](https://github.com/jamiebull1/transport-carbon).
