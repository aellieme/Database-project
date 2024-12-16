START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

DROP FUNCTION 	IF EXISTS ticket_insert;
DROP FUNCTION 	IF EXISTS ticket_select_one;
DROP FUNCTION 	IF EXISTS ticket_select;

DROP FUNCTION 	IF EXISTS flight_insert;
DROP FUNCTION 	IF EXISTS flight_select_one;
DROP FUNCTION 	IF EXISTS flight_select;

DROP FUNCTION 	IF EXISTS plane_insert;
DROP FUNCTION 	IF EXISTS plane_select_one;
DROP FUNCTION 	IF EXISTS plane_select;

DROP FUNCTION 	IF EXISTS airline_insert;
DROP FUNCTION 	IF EXISTS airline_select_one;
DROP FUNCTION 	IF EXISTS airline_select;

DROP FUNCTION 	IF EXISTS airport_search;
DROP FUNCTION 	IF EXISTS airport_insert;
DROP FUNCTION 	IF EXISTS airport_select_one;
DROP FUNCTION 	IF EXISTS airport_select;

DROP TRIGGER 	IF EXISTS update_price_on_flight_update ON flight;
DROP TRIGGER 	IF EXISTS update_price 					ON ticket;

DROP FUNCTION 	IF EXISTS check_duplicate_flight_seatnumber;
DROP FUNCTION 	IF EXISTS check_duplicate_flight_passport;
DROP FUNCTION 	IF EXISTS can_register_passenger;
DROP FUNCTION 	IF EXISTS update_ticket_price CASCADE;
DROP FUNCTION 	IF EXISTS calculate_price;

DROP TABLE 		IF EXISTS ticket;
DROP TABLE 		IF EXISTS flight;
DROP TABLE 		IF EXISTS plane;
DROP TABLE 		IF EXISTS airline;
DROP INDEX 		IF EXISTS idx_airport_name;
DROP TABLE 		IF EXISTS airport;

DROP EXTENSION 	IF EXISTS pg_trgm;

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;