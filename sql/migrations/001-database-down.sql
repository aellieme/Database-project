START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

DROP INDEX 		IF EXISTS idx_airport_name;

DROP TRIGGER 	IF EXISTS update_price ON Ticket;

DROP FUNCTION 	IF EXISTS can_register_passenger;
DROP FUNCTION 	IF EXISTS calculate_price;

DROP TABLE 		IF EXISTS Ticket;
DROP TABLE 		IF EXISTS Flight;
DROP TABLE 		IF EXISTS Plane;
DROP TABLE 		IF EXISTS Airline;
DROP TABLE 		IF EXISTS Airport;

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;