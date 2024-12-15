START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

CREATE USER "user" WITH PASSWORD '1234';

GRANT SELECT, UPDATE, INSERT, DELETE, TRUNCATE ON airport TO "user";
GRANT SELECT, UPDATE, INSERT, DELETE, TRUNCATE ON airline TO "user";
GRANT SELECT, UPDATE, INSERT, DELETE, TRUNCATE ON plane TO "user";
GRANT SELECT, UPDATE, INSERT, DELETE, TRUNCATE ON flight TO "user";
GRANT SELECT, UPDATE, INSERT, DELETE, TRUNCATE ON ticket TO "user";

GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO "user";

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;