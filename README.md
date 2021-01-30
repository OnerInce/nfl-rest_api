# NFL Players REST API

## Usage
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