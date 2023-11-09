<p align=center><img src=_src/assets/forecast.jpg><p>

# <h1 align=center> **Sara's Journal Weather API** </h1>

# Introduction

This repository aims create an API to keep a daily weather journal, and a weather forecast consultation. To keep track the weather journal it has implemented a SQL database using PostgreSQL. To request the weather forecast it has used the Open Weather Map API.

# Run the code

This code was developed using Python 3.10.12.

## Set environment variables

The first thing you have to do in order to run the code is to create a `.env` file with the following content:

```
# Database connection
DB_NAME=<database-name>
DB_USER=<username>
DB_PASS=<password>
DB_HOST=<ip addr>
DB_PORT=<db port>
# Auth
ACCESS_TOKEN_EXPIRE_MINUTES=1440
SECRET_KEY=<key for authentication>
# OpenWeatherMap
FORECAST_API_KEY=<OpenWeatherMap key>
```

For the `SECRET_KEY` it can be used **openssl rand -hex 32** if it is running Linux OS.
Example of the file:

```
# Database connection
DB_NAME=test1
DB_USER=ostrich
DB_PASS=ostrich
DB_HOST=localhost
DB_PORT=5432
# Auth
ACCESS_TOKEN_EXPIRE_MINUTES=1440
SECRET_KEY=6b3d75e968f26f3be3443503efefd761e22d5e173fea95646a3659e673ebb97b
# OpenWeatherMap
FORECAST_API_KEY=<OpenWeatherMap key>
```

>Note: Take in mind that DB_USER, DB_NAME and DB_PASS environment variable must be the same that variables defined in `docker-compose.yml` file named POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB.

## Virtual environment

Create a vrtual environment in order to install all the dependencies.

```
virtualenv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Run PostgreSQL

In order to run the following code it is necesary to install PostgreSQL manually or use the `docker-compose.yml` file provided in the repository.

### Running the docker container

```
docker compose up -d --build
```

## Run API

To run the API service:

```
uvicorn api.main:app --reload
```

To access the API locally http://127.0.0.1:8000/docs.
Where you can find all the API documentation and endpoints.

# API

The API is separeted in 3 sections:

- User: 
    - Create a new user
    - Login for access token
- Weather:
    - Get all elements od the database
    - Create a new element
    - Get an element by ID
    - Update an element by ID
    - Delet an element by ID
- Forecast
    - Get forecast by city name
    - Get forecast by latitude and longitude

The first thing to do is create a new user. Once the new user is created, authenticate to get access.

<p align=center><img src=_src/assets/create_user.png><p>

<p align=center><img src=_src/assets/auth.png><p>

The weather endpoints are the following:

<p align=center><img src=_src/assets/weather.png><p>

The forecast endpoints are the following:

<p align=center><img src=_src/assets/forecast.png><p>
