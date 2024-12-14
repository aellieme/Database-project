#!/bin/bash
export PGPASSWORD="1234"

DB_NAME="airport"

test=$(psql -h localhost -U postgres -c "CREATE DATABASE $DB_NAME;")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 001-database-up.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 002-user-up.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 003-airport-insert-up.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 004-airline-insert-up.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 005-plane-insert-up.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 006-flight-insert-up.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 007-ticket-insert-up.sql")
echo $test

test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir 008-procedures-up.sql")
echo $test
