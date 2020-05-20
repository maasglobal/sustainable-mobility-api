# Sustainable Mobility API server
This project provides an example server for the Sustainable Mobility API project.

## Running the server
In order to run the server, you will need a few dependencies:

- Python 3
- pipenv

### Install project dependencies
You can install the project dependencies with the following command from within the `api` directory:

```sh
pipenv install
```

### Launch the virtual environment
Once pipenv has installed the dependencies, you can launch the virtual environment with this command:

```sh
pipenv shell
```

### Run the server
Once the virtual environment is active and dependencies are installed, you can run the example server by running the following command:

```sh
python app.py
```

### Accessing the documentation UI

Once the server is running, you can access the documentation UI to try it out:

> http://127.0.0.1:8080/ui/

### Try the API from command line

```bash
curl "http://localhost:8080/estimate-co2?transport_mode=small_car&distance_km=1"
```

You should get a response like the following.
```json
{
  "co2_estimate": 112.0,
  "distance_km": 1.0,
  "transport_mode": "SMALL_CAR",
  "vehicle_occupancy": 1.5
}
```

## Deploy with Docker

You don't need to install Python if you have a docker environment available.
Use docker-compose to bring the docker container with API and documentation ready to be used:

```bash
docker-compose up -d
```

## Deploy the serverless function

You can use serverless framework to deploy estimate-co2 API to the AWS Lambda environment.

To deploy CloudFormation stack with function available publically via HTTPs, issue following commands:

```bash
npm i -g serverless
npm install
serverless deploy
```

This will generate output which contains dynamic endpoint url for your function:

```bash
Serverless: Generating requirements.txt from Pipfile...
Serverless: Parsed requirements.txt from Pipfile in .serverless/requirements.txt...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service estimate-co2.zip file to S3 (7.28 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..........
Serverless: Stack update finished...
Service Information
service: estimate-co2
stage: dev
region: eu-west-1
stack: estimate-co2-dev
resources: 10
api keys:
  None
endpoints:
  GET - https://NNNNNNNN.execute-api.eu-west-1.amazonaws.com/dev/estimate-co2
functions:
  estimate-co2: estimate-co2-dev-estimate-co2
layers:
  None
````

Invoke function by using endpoint URL:

```bash
curl https://NNNNNNNN.execute-api.eu-west-1.amazonaws.com/dev/estimate-co2?transport_mode=bus&distance_km=24&vehicle_occupancy=2
{
   "input" : {
      "vehicle_occupancy" : "2",
      "distance_km" : "24",
      "transport_mode" : "bus"
   },
   "result" : {
      "vehicle_occupancy" : 2,
      "co2_estimate" : 10356,
      "transport_mode" : "BUS"
   }
}
```

Invoke function locally:

```bash
pipenv run serverless invoke local -f post -d '{ "queryStringParameters": { "transport_mode": "small_car", "distance_km": 55 } }'
```
