START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

CREATE EXTENSION pg_trgm;

/*----------------------------------------------------------------------------------------------------------*/


CREATE TABLE Airport (
	AirportID 	SERIAL PRIMARY KEY,
	AirportName VARCHAR(100) NOT NULL,
	City 		VARCHAR(100) NOT NULL
);

COMMENT ON TABLE Airport IS 'Сведения об аэропортах';
COMMENT ON COLUMN Airport.AirportID	IS 'название аэропорта';
COMMENT ON COLUMN Airport.AirportID	IS 'город, в котором находится аэропорт';

/*----------------------------------------------------------------------------------------------------------*/

CREATE INDEX idx_airport_name ON Airport USING gist (AirportName gist_trgm_ops);

COMMENT ON INDEX idx_airport_name IS 'Индекс по текстовому не ключевому полю AirportName в таблице Airport';

/*----------------------------------------------------------------------------------------------------------*/

CREATE TABLE Airline (
	AirlineID 	SERIAL PRIMARY KEY,
	AirlineName VARCHAR(100) 	NOT NULL,
	IATACode 	VARCHAR(3)		NOT NULL UNIQUE
);

COMMENT ON TABLE Airline IS 'Сведения об авиакомпаниях';
COMMENT ON COLUMN Airline.AirlineName	IS 'название авиакомпании';
COMMENT ON COLUMN Airline.IATACode		IS 'уникальный код авиакомпании';

/*----------------------------------------------------------------------------------------------------------*/

CREATE TABLE Plane (
	PlaneID 	SERIAL PRIMARY KEY,
	AirlineID 	INT 			REFERENCES Airline(AirlineID) ON DELETE CASCADE,
	Model 		VARCHAR(100) 	NOT NULL,
	Capacity 	INT 			NOT NULL CHECK (Capacity > 0)
);

COMMENT ON TABLE Plane IS 'Сведения о самолетах';
COMMENT ON COLUMN Plane.AirlineID	IS 'id авиакомпании, которой принадлежит самолет';
COMMENT ON COLUMN Plane.Model		IS 'модель самолета';
COMMENT ON COLUMN Plane.Capacity	IS 'вместимость самолета (чел.)';

/*----------------------------------------------------------------------------------------------------------*/

CREATE TABLE Flight (
    FlightID 			SERIAL PRIMARY KEY,                         
    PlaneID 			INT 		REFERENCES Plane(PlaneID) ON DELETE CASCADE, 
    DepartureAirportID 	INT 		REFERENCES Airport(AirportID) ON DELETE CASCADE, 
    ArrivalAirportID 	INT 		REFERENCES Airport(AirportID) ON DELETE CASCADE,   
    FlightTime 			TIMESTAMP 	NOT NULL,
    Duration 			INTERVAL 	NOT NULL,
    BaseTicketPrice 	INT 		NOT NULL CHECK (BaseTicketPrice > 0)
);

COMMENT ON TABLE Flight IS 'Сведения о рейсах';
COMMENT ON COLUMN Flight.PlaneID			IS 'id самолета';
COMMENT ON COLUMN Flight.DepartureAirportID	IS 'id аэропорта вылета';
COMMENT ON COLUMN Flight.ArrivalAirportID	IS 'id аэропорта прилета';
COMMENT ON COLUMN Flight.FlightTime			IS 'время вылета';
COMMENT ON COLUMN Flight.Duration			IS 'время в пути';
COMMENT ON COLUMN Flight.BaseTicketPrice	IS 'базовая стоимость билета (без учета обеда на борту)';

/*----------------------------------------------------------------------------------------------------------*/

CREATE TABLE Ticket (
    TicketID 		SERIAL PRIMARY KEY,               
    FlightID 		INT 			REFERENCES Flight(FlightID) ON DELETE CASCADE,  
    FullName 		VARCHAR(255) 	NOT NULL,              
    PassportNumber 	VARCHAR(10) 	NOT NULL,         
    SeatNumber 		VARCHAR(3) 		NOT NULL,                            
    Meal 			VARCHAR(3) 		CHECK (Meal IN ('YES', 'NO')),
	Price 			INT 			NOT NULL
);

COMMENT ON TABLE Ticket IS 'Сведения о билетах';
COMMENT ON COLUMN Ticket.FlightID		IS 'id рейса';
COMMENT ON COLUMN Ticket.FullName		IS 'ФИО пассажира';
COMMENT ON COLUMN Ticket.PassportNumber	IS 'серия и номер паспорта пассажира';
COMMENT ON COLUMN Ticket.SeatNumber		IS 'номер места в самолете';
COMMENT ON COLUMN Ticket.Meal			IS 'обед на борту (да/нет)';
COMMENT ON COLUMN Ticket.Price			IS 'итоговая стоимость билета (заполняется/изменяется триггером)';

/*----------------------------------------------------------------------------------------------------------*/

CREATE OR REPLACE FUNCTION calculate_price()
RETURNS TRIGGER AS $$
BEGIN
	IF NEW.Meal = 'NO' 		THEN
        NEW.Price := (SELECT BaseTicketPrice FROM Flight WHERE FlightID = NEW.FlightID);
    ELSIF NEW.Meal = 'YES' 	THEN
        NEW.Price := (SELECT BaseTicketPrice FROM Flight WHERE FlightID = NEW.FlightID) + 499;
	END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION calculate_price IS 'Функция подсчета итоговой стоимости билета в зависимости от наличия обеда на борту';

/*----------------------------------------------------------------------------------------------------------*/

CREATE OR REPLACE FUNCTION can_register_passenger(flight_id INT)
RETURNS BOOLEAN AS
$$
DECLARE
    occupied_seats INT;
    plane_capacity INT;
BEGIN
    SELECT COUNT(*) INTO occupied_seats
    FROM Ticket
    WHERE FlightID = flight_id;
    SELECT Capacity INTO plane_capacity
    FROM Plane 
    JOIN Flight ON Plane.PlaneID = Flight.PlaneID
    WHERE Flight.FlightID = flight_id;
    IF occupied_seats < plane_capacity THEN
        RETURN TRUE;  -- Можно 
    ELSE
        RETURN FALSE; -- Мест нет - нельзя
    END IF;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION can_register_passenger IS 'Проверка возможности регистрации нового пассажира на рейс';

/*----------------------------------------------------------------------------------------------------------*/

CREATE TRIGGER update_price
BEFORE INSERT OR UPDATE ON Ticket
FOR EACH ROW
EXECUTE FUNCTION calculate_price();

COMMENT ON TRIGGER update_price ON Ticket IS 'Триггер на таблицу со сведениями о билетах с применением функции подсчета итоговой стоимости билета';

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;
