#!/bin/bash
export PGPASSWORD="1234"

DB_NAME="airport"

cd ..

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/008-procedures-down.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/007-ticket-insert-down.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/006-flight-insert-down.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/005-plane-insert-down.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/004-airline-insert-down.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/003-airport-insert-down.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/002-user-down.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/001-database-down.sql")
test=$(psql -h localhost -U postgres -c "
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = '$DB_NAME'
AND pid <> pg_backend_pid();")
test=$(psql -h localhost -U postgres -c "DROP DATABASE $DB_NAME")
