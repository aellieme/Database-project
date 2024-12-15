#!/bin/bash
export PGPASSWORD="1234"

DB_NAME="airport"

cd ..
test=$(psql -h localhost -U postgres -c "CREATE DATABASE $DB_NAME;")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/001-database-up.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/002-user-up.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/003-airport-insert-up.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/004-airline-insert-up.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/005-plane-insert-up.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/006-flight-insert-up.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/007-ticket-insert-up.sql")
test=$(psql -h localhost -U postgres -d $DB_NAME -c "\ir sql/migrations/008-procedures-up.sql")
