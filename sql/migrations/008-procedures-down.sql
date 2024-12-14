START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

DROP PROCEDURE IF EXISTS ticket_truncate;
DROP PROCEDURE IF EXISTS ticket_delete;
DROP PROCEDURE IF EXISTS ticket_update;

DROP PROCEDURE IF EXISTS flight_truncate;
DROP PROCEDURE IF EXISTS flight_delete;
DROP PROCEDURE IF EXISTS flight_update;

DROP PROCEDURE IF EXISTS plane_truncate;
DROP PROCEDURE IF EXISTS plane_delete;
DROP PROCEDURE IF EXISTS plane_update;

DROP PROCEDURE IF EXISTS airline_truncate;
DROP PROCEDURE IF EXISTS airline_delete;
DROP PROCEDURE IF EXISTS airline_update;

DROP PROCEDURE IF EXISTS airport_truncate;
DROP PROCEDURE IF EXISTS airport_delete;
DROP PROCEDURE IF EXISTS airport_update;

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;