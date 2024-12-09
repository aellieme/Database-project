START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

INSERT INTO Airline ( AirlineName, IATACode )
VALUES ( 'Аэрофлот', 'SU' );

INSERT INTO Airline ( AirlineName, IATACode )
VALUES ( 'S7 Airlines', 'S7' );

INSERT INTO Airline ( AirlineName, IATACode )
VALUES ( 'Победа', 'DP' );

INSERT INTO Airline ( AirlineName, IATACode )
VALUES ( 'Azur Air', 'ZF' );

INSERT INTO Airline ( AirlineName, IATACode )
VALUES ( 'Россия', 'FV' );

INSERT INTO Airline ( AirlineName, IATACode )
VALUES ( 'Smartavia', '5N' );

INSERT INTO Airline ( AirlineName, IATACode )
VALUES ( 'Red Wings', 'WZ' );

INSERT INTO Airline ( AirlineName, IATACode )
VALUES ( 'Utair', 'UT' );

INSERT INTO Airline ( AirlineName, IATACode )
VALUES ( 'Уральские авиалинии', 'U6' );

INSERT INTO Airline ( AirlineName, IATACode )
VALUES ( 'Азимут', 'A4' );

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;