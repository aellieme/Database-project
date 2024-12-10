START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

CREATE USER "user" WITH PASSWORD '1234';
ALTER ROLE "user" CREATEDB;

GRANT SELECT, UPDATE, INSERT, DELETE, TRUNCATE ON Airport TO "user";
GRANT SELECT, UPDATE, INSERT, DELETE, TRUNCATE ON Airline TO "user";
GRANT SELECT, UPDATE, INSERT, DELETE, TRUNCATE ON Plane TO "user";
GRANT SELECT, UPDATE, INSERT, DELETE, TRUNCATE ON Flight TO "user";
GRANT SELECT, UPDATE, INSERT, DELETE, TRUNCATE ON Ticket TO "user";

GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO "user";

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;