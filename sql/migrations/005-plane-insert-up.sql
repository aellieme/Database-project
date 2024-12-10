START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 1, 'Airbus A320-200', 140 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 1, 'Airbus A321-200', 170 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 1, 'Boeing 737-800', 158 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 2, 'Airbus A320neo', 164 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 2, 'Boeing 737-800', 176 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 3, 'Boeing 737-800', 189 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 4, 'Boeing 757-200', 238 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 4, 'Boeing 767-300ER', 336 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 4, 'Boeing 777-300ER', 531 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 5, 'Airbus A319-100', 128 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 5, 'Sukhoi Superjet 100-95B', 87 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 6, 'Boeing 737-700', 148 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 6, 'Boeing 737-800', 189 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 7, 'SSj-100', 100 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 7, 'Boeing 777-200ER', 412 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 7, 'Tу-214', 194 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 8, 'ATR 72-500', 70 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 8, 'Boeing 737-500', 126 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 8, 'Boeing 737-800', 186 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 9, 'Airbus A320-200', 158 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 9, 'Airbus A321-200', 220 );

INSERT INTO Plane ( AirlineID, Model, Capacity )
VALUES ( 10, 'Sukhoi Superjet 100-95LR', 103 );

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;