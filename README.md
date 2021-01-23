# bbm479-nfl-api

Use

docker cp latest.dump bbm479-nfl-api-1_db_1:/var/lib/postgresql/data
docker exec -i bbm479-nfl-api-1_db_1 pg_restore -t playersdb -U postgres -d nfldb < latest.dump

Restore the database. 