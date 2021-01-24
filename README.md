# NFL Players REST API

## Usage
Assuming Docker is already installed in the system, build and create Postgres database :

```
docker-compose up db
```

While db instance is running, open a new terminal tab. 
To fill the database with information, use pg_restore:

```
docker cp latest.dump bbm479-nfl-api-1_db_1:/var/lib/postgresql/data
docker exec -i bbm479-nfl-api-1_db_1 pg_restore -U postgres -d nfldb < latest.dump
```

Finally, build and run all containers:

```
docker-compose up
```

Reach API Service from:

```
http://localhost:8000/
```