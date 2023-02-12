<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://upload.wikimedia.org/wikipedia/en/a/a2/National_Football_League_logo.svg" alt="nfl logo"></a>
</p>

# NFL Players and Prediction REST API

RESTful API implementation for BBM479 - Hacettepe University CS Undergraduate Term Project Course. 

Data source of API: https://www.kaggle.com/c/nfl-big-data-bowl-2020/data

## API

#### /api/teams
* `GET` : Get all teams

#### /api/players/:season/:team
* `GET` : Get all players from :team who are played in :season

#### /predict
* `POST` : Get prediction result from learning model

## Usage
🐋

Assuming Docker is already installed in the system, build and create Postgres database :

```
docker-compose up db
```

In a new terminal tab, migrate Django models to create database tables:

```
docker-compose run web python manage.py migrate
```

After tables and fields are created, fill the database with "nfl-db_insert.sql" file. Run this command:
```
cat ./nfl-db_insert.sql | docker exec -i  bbm479-nfl-api_db_1 psql -U postgres -d nfldb
```

Finally, build and run all containers:

```
docker-compose up
```

Reach API Service from:

```
http://localhost:8000/
```
