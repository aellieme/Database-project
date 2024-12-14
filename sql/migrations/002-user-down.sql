START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

REASSIGN OWNED BY "user" TO postgres;
DROP OWNED BY "user";

REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM "user";
REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM "user";
REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM "user";

ALTER USER "user" WITH NOCREATEDB;
DROP USER "user";

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;