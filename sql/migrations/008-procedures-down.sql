START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

DROP PROCEDURE IF EXISTS ticket_insert;
DROP PROCEDURE IF EXISTS ticket_truncate;
DROP PROCEDURE IF EXISTS ticket_delete;
DROP PROCEDURE IF EXISTS ticket_update;
DROP PROCEDURE IF EXISTS ticket_select_one;
DROP PROCEDURE IF EXISTS ticket_select;

/*----------------------------------------------------------------------------------------------------------*/

DROP PROCEDURE IF EXISTS flight_insert;
DROP PROCEDURE IF EXISTS flight_truncate;
DROP PROCEDURE IF EXISTS flight_delete;
DROP PROCEDURE IF EXISTS flight_update;
DROP PROCEDURE IF EXISTS flight_select_one;
DROP PROCEDURE IF EXISTS flight_select;

/*----------------------------------------------------------------------------------------------------------*/

DROP PROCEDURE IF EXISTS plane_insert;
DROP PROCEDURE IF EXISTS plane_truncate;
DROP PROCEDURE IF EXISTS plane_delete;
DROP PROCEDURE IF EXISTS plane_update;
DROP PROCEDURE IF EXISTS plane_select_one;
DROP PROCEDURE IF EXISTS plane_select;

/*----------------------------------------------------------------------------------------------------------*/

DROP PROCEDURE IF EXISTS airline_insert;
DROP PROCEDURE IF EXISTS airline_truncate;
DROP PROCEDURE IF EXISTS airline_delete;
DROP PROCEDURE IF EXISTS airline_update;
DROP PROCEDURE IF EXISTS airline_select_one;
DROP PROCEDURE IF EXISTS airline_select;

/*----------------------------------------------------------------------------------------------------------*/

DROP PROCEDURE IF EXISTS airport_search;
DROP PROCEDURE IF EXISTS airport_insert;
DROP PROCEDURE IF EXISTS airport_truncate;
DROP PROCEDURE IF EXISTS airport_delete;
DROP PROCEDURE IF EXISTS airport_update;
DROP PROCEDURE IF EXISTS airport_select_one;
DROP PROCEDURE IF EXISTS airport_select;

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;