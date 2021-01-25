# NFL Players REST API

## Usage
Assuming Docker is already installed in the system, build and create Postgres database :

```
docker-compose up db
```

In a new terminal tab, migrate Django models to database:

```
docker-compose run web python manage.py migrate
```

After tables and fields are created, fill the database with "nfl-db_insert.sql" file. This can be done from terminal or Dbeaver (or similar) database client. Connect to db and execute .sql file:
```
jdbc:postgresql://localhost:6543/nfldb
```

Finally, build and run all containers:

```
docker-compose up
```

Reach API Service from:

```
http://localhost:8000/
```