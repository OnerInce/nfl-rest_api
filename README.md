# NFL Players REST API

## Usage
Assuming Docker is already installed in the system, create containers :

```
docker-compose up
```

In a new terminal tab, fill the database with "nfl-db_insert.sql" file with this command:
```
cat db/nfl-db_insert.sql | docker exec -i  bbm479-nfl-api_db_1 psql -U postgres -d nfldb
```

Reach API Service from:

```
http://localhost:8000/
```