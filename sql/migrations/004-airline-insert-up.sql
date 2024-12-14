START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

INSERT INTO airline ( airlinename, iatacode )
VALUES ( 'Аэрофлот', 'SU' );

INSERT INTO airline ( airlinename, iatacode )
VALUES ( 'S7 Airlines', 'S7' );

INSERT INTO airline ( airlinename, iatacode )
VALUES ( 'Победа', 'DP' );

INSERT INTO airline ( airlinename, iatacode )
VALUES ( 'Azur Air', 'ZF' );

INSERT INTO airline ( airlinename, iatacode )
VALUES ( 'Россия', 'FV' );

INSERT INTO airline ( airlinename, iatacode )
VALUES ( 'Smartavia', '5N' );

INSERT INTO airline ( airlinename, iatacode )
VALUES ( 'Red Wings', 'WZ' );

INSERT INTO airline ( airlinename, iatacode )
VALUES ( 'Utair', 'UT' );

INSERT INTO airline ( airlinename, iatacode )
VALUES ( 'Уральские авиалинии', 'U6' );

INSERT INTO airline ( airlinename, iatacode )
VALUES ( 'Азимут', 'A4' );

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;