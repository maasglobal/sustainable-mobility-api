# Sustainable Mobility API server
This project provides an example server for the Sustainable Mobility API project.

## Prerequisites
In order to run the server, you will need a few system dependencies:

- Python 3
- pipenv

## Install the project
You can install the project with the following command from within the `api` directory:

```sh
pipenv install
```

### Launch the virtual environment
Once pipenv has installed the project, you can launch the virtual environment with this command:

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
We provide an `example_request.json` file in the `api` directory. Use the following command to test out the API from the command line:

```bash
curl -X POST -H "Content-Type: application/json" -d @example_request.json "http://localhost:8080/estimate-co2"
```

## Deploy with Docker

Use docker-compose to bring the docker container with API and documentation:

```bash
docker-compose up -d
```

## Deploy with serverless

You can use serverless framework to deploy estimate-co2 API to the AWS Lambda environment.

To deploy CloudFormation stack with function available publically via HTTPs, issue following commands:

```bash
npm i -g serverless
npm install
serverless deploy
```

### Invoke serverless function locally

```bash
pipenv run serverless invoke local -f post -p example_request.json
```
