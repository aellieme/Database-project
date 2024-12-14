#!/bin/bash
export PGPASSWORD="1234"

DB_NAME="airport"

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 008-procedures-down.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 007-ticket-insert-down.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 006-flight-insert-down.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 005-plane-insert-down.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 004-airline-insert-down.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 003-airport-insert-down.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 002-user-down.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 001-database-down.sql")
echo $test

test=$(psql -h localhost -U postgres -c "
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = '$DB_NAME'
AND pid <> pg_backend_pid();")
echo $test

test=$(psql -h localhost -U postgres -c "DROP DATABASE $DB_NAME")
echo $test

