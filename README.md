# Transport CO2

Calculate CO2 (equivalent) emissions for a given transport trip and provide a simple interpretation of the result.

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

Further improvements to the model may come from other sources, such as the following.

- IPCC AR5 [Chapter 8 - Transport](https://www.ipcc.ch/site/assets/uploads/2018/02/ipcc_wg3_ar5_chapter8.pdf)
- Wikipedia: [Environmental impact of transport](https://en.wikipedia.org/wiki/Environmental_impact_of_transport)

## Attribution

Initial package structure forked from [navdeep-G/setup.py](https://github.com/navdeep-G/setup.py).

Friendly nod to [jamiebull1/transport-carbon](https://github.com/jamiebull1/transport-carbon).
