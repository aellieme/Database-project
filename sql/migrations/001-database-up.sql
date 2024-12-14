START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

CREATE EXTENSION pg_trgm;

/*----------------------------------------------------------------------------------------------------------*/


CREATE TABLE airport (
	airportid 	SERIAL PRIMARY KEY,
	airportname VARCHAR(100) NOT NULL,
	city 		VARCHAR(100) NOT NULL
);

COMMENT ON TABLE airport IS 'Сведения об аэропортах';
COMMENT ON COLUMN Airport.airportname	IS 'название аэропорта';
COMMENT ON COLUMN Airport.city			IS 'город, в котором находится аэропорт';

/*----------------------------------------------------------------------------------------------------------*/

CREATE INDEX idx_airport_name ON airport USING gist (airportname gist_trgm_ops);

COMMENT ON INDEX idx_airport_name IS 'Индекс по текстовому не ключевому полю AirportName в таблице airport';

/*----------------------------------------------------------------------------------------------------------*/

CREATE TABLE airline (
	airlineid 	SERIAL PRIMARY KEY,
	airlinename VARCHAR(100) 	NOT NULL,
	iatacode 	VARCHAR(3)		NOT NULL UNIQUE
);

COMMENT ON TABLE airline IS 'Сведения об авиакомпаниях';
COMMENT ON COLUMN airline.airlinename	IS 'название авиакомпании';
COMMENT ON COLUMN airline.iatacode		IS 'уникальный код авиакомпании';

/*----------------------------------------------------------------------------------------------------------*/

CREATE TABLE plane (
	planeid 	SERIAL PRIMARY KEY,
	airlineid 	INT 			REFERENCES airline(airlineid) ON DELETE CASCADE,
	model 		VARCHAR(100) 	NOT NULL,
	capacity 	INT 			NOT NULL CHECK (capacity > 0)
);

COMMENT ON TABLE plane IS 'Сведения о самолетах';
COMMENT ON COLUMN plane.airlineid	IS 'id авиакомпании, которой принадлежит самолет';
COMMENT ON COLUMN plane.model		IS 'модель самолета';
COMMENT ON COLUMN plane.capacity	IS 'вместимость самолета (чел.)';

/*----------------------------------------------------------------------------------------------------------*/

CREATE TABLE flight (
    flightid 			SERIAL PRIMARY KEY,                         
    planeid 			INT 		REFERENCES plane(planeid) ON DELETE CASCADE, 
    departureairportID 	INT 		REFERENCES airport(airportid) ON DELETE CASCADE, 
    arrivalairportID 	INT 		REFERENCES airport(airportid) ON DELETE CASCADE,   
    flighttime 			TIMESTAMP 	NOT NULL,
    duration 			INTERVAL 	NOT NULL,
    baseticketprice 	INT 		NOT NULL CHECK (baseticketprice > 0)
);

COMMENT ON TABLE flight IS 'Сведения о рейсах';
COMMENT ON COLUMN flight.planeid			IS 'id самолета';
COMMENT ON COLUMN flight.departureairportid	IS 'id аэропорта вылета';
COMMENT ON COLUMN flight.arrivalairportid	IS 'id аэропорта прилета';
COMMENT ON COLUMN flight.flighttime			IS 'время вылета';
COMMENT ON COLUMN flight.duration			IS 'время в пути';
COMMENT ON COLUMN flight.baseticketprice	IS 'базовая стоимость билета (без учета обеда на борту)';

/*----------------------------------------------------------------------------------------------------------*/

CREATE TABLE ticket (
    ticketID 		SERIAL PRIMARY KEY,               
    flightID 		INT 			REFERENCES flight(flightid) ON DELETE CASCADE,  
    fullname 		VARCHAR(255) 	NOT NULL,              
    passportnumber 	VARCHAR(10) 	NOT NULL,         
    seatnumber 		VARCHAR(3) 		NOT NULL,                            
    meal 			VARCHAR(3) 		CHECK (meal IN ('YES', 'NO')),
	price 			INT 			NOT NULL
);

COMMENT ON TABLE ticket IS 'Сведения о билетах';
COMMENT ON COLUMN ticket.flightid		IS 'id рейса';
COMMENT ON COLUMN ticket.fullname		IS 'ФИО пассажира';
COMMENT ON COLUMN ticket.passportnumber	IS 'серия и номер паспорта пассажира';
COMMENT ON COLUMN ticket.seatnumber		IS 'номер места в самолете';
COMMENT ON COLUMN ticket.meal			IS 'обед на борту (да/нет)';
COMMENT ON COLUMN ticket.price			IS 'итоговая стоимость билета (заполняется/изменяется триггером)';

/*----------------------------------------------------------------------------------------------------------*/

CREATE OR REPLACE FUNCTION calculate_price()
RETURNS TRIGGER AS $$
BEGIN
	IF NEW.meal = 'NO' 		THEN
        NEW.price := (SELECT baseticketprice FROM flight WHERE flightid = NEW.flightid);
    ELSIF NEW.meal = 'YES' 	THEN
        NEW.price := (SELECT baseticketprice FROM flight WHERE Flightid = NEW.flightid) + 499;
	END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION calculate_price IS 'Функция подсчета итоговой стоимости билета в зависимости от наличия обеда на борту';

/*----------------------------------------------------------------------------------------------------------*/

CREATE OR REPLACE FUNCTION update_ticket_price()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE ticket
  SET price = (
    SELECT baseticketprice
    FROM flight
    WHERE flightid = OLD.flightid
  )
  WHERE flightid = OLD.flightid;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION update_ticket_price IS 'Функция меняющая итоговую стоимость билета при обновлении базовой';

/*----------------------------------------------------------------------------------------------------------*/

CREATE OR REPLACE FUNCTION can_register_passenger(flight_id INT)
RETURNS BOOLEAN AS
$$
DECLARE
    occupied_seats INT;
    plane_capacity INT;
BEGIN
    SELECT COUNT(*) INTO occupied_seats
    FROM ticket
    WHERE flightid = flight_id;
    SELECT capacity INTO plane_capacity
    FROM plane 
    JOIN flight ON plane.planeid = flight.planeid
    WHERE flight.flightid = flight_id;
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
BEFORE INSERT OR UPDATE ON ticket
FOR EACH ROW
EXECUTE FUNCTION calculate_price();

COMMENT ON TRIGGER update_price ON ticket IS 'Триггер на таблицу со сведениями о билетах с применением функции подсчета итоговой стоимости билета';

/*----------------------------------------------------------------------------------------------------------*/

CREATE TRIGGER update_price_on_flight_update
AFTER UPDATE ON flight
FOR EACH ROW
EXECUTE FUNCTION update_ticket_price();

COMMENT ON TRIGGER update_price_on_flight_update ON flight IS 'Триггер на таблицу со сведениями о рейсах с применением функции обновления итоговой стоимости билета';

/*----------------------------------------------------------------------------------------------------------*/

CREATE OR REPLACE FUNCTION airport_select()
RETURNS TABLE(
	aid INT, 
	nam VARCHAR(100),
	cit VARCHAR(100)
) AS $$
BEGIN
	RETURN QUERY 
	SELECT airportid, airportname, city 
	FROM airport
	ORDER BY airportid;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION airport_select_one(airp_id INT)
RETURNS TABLE(
	nam VARCHAR(100),
	cit VARCHAR(100)
) AS $$
BEGIN
	RETURN QUERY
	SELECT airportname, city 
	FROM airport 
	WHERE airportid = airp_id;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION airport_insert(
	airp_name VARCHAR(100), 
	airp_city VARCHAR(100)
)
RETURNS INT AS $$
DECLARE airp_id INT;
BEGIN
    INSERT INTO airport ( airportname, city )
    VALUES ( airp_name, airp_city )
    RETURNING airportid INTO airp_id;
    RETURN airp_id;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION airport_search(airp_name VARCHAR(100))
RETURNS TABLE(
	nam VARCHAR(100),
	sim REAL
) AS $$
BEGIN
	RETURN QUERY
	SELECT airportname, similarity(airportname, $1) AS similarity 
	FROM airport 
	WHERE airportname % $1
	ORDER BY similarity DESC;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

CREATE OR REPLACE FUNCTION airline_select()
RETURNS TABLE(
	aid INT, 
	nam VARCHAR(100),
	cod VARCHAR(3)
) AS $$
BEGIN
	RETURN QUERY 
	SELECT airlineid, airlinename, iatacode
	FROM airline
	ORDER BY airlineid;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION airline_select_one(airl_id INT)
RETURNS TABLE(
	nam VARCHAR(100),
	cod VARCHAR(3)
) AS $$
BEGIN
	RETURN QUERY
	SELECT airlinename, iatacode
	FROM airline 
	WHERE airlineid = airl_id;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION airline_insert(
	airl_name VARCHAR(100), 
	airl_code VARCHAR(3)
)
RETURNS INT AS $$
DECLARE airl_id INT;
BEGIN
	INSERT INTO airline ( airlinename, iatacode )
    VALUES ( airl_name, airl_code )
    RETURNING airlineId INTO airl_id;
    RETURN airl_id;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

CREATE OR REPLACE FUNCTION plane_select()
RETURNS TABLE(
	pid INT,
	aid INT, 
	mod VARCHAR(100),
	cap INT
) AS $$
BEGIN
	RETURN QUERY 
	SELECT planeid, airlineid, model, capacity
	FROM plane
	ORDER BY planeid;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION plane_select_one(p_id INT)
RETURNS TABLE(
	aid INT, 
	mod VARCHAR(100),
	cap INT
) AS $$
BEGIN
	RETURN QUERY
	SELECT airlineid, model, capacity
	FROM plane 
	WHERE planeid = p_id;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION plane_insert(
	airl_id INT, 
	p_model VARCHAR(100), 
	p_capacity INT
)
RETURNS INT AS $$
DECLARE p_id INT;
BEGIN
	INSERT INTO plane ( airlineid, model, capacity )
    VALUES ( airl_id, p_model, p_capacity )
    RETURNING planeid INTO p_id;
    RETURN p_id;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

CREATE OR REPLACE FUNCTION flight_select()
RETURNS TABLE(
	fid INT,
	pid INT, 
	daid INT, 
	aaid INT,
	tim TIMESTAMP,
	dur INTERVAL,
	btp INT
) AS $$
BEGIN
	RETURN QUERY 
	SELECT flightid, planeid, departureairportid, arrivalairportid, flighttime, duration, baseticketprice
	FROM flight
	ORDER BY flightid;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION flight_select_one(f_id INT)
RETURNS TABLE(
	pid INT, 
	daid INT, 
	aaid INT,
	tim TIMESTAMP,
	dur INTERVAL,
	btp INT
) AS $$
BEGIN
	RETURN QUERY
	SELECT planeid, departureairportid, arrivalairportid, flighttime, duration, baseticketprice
	FROM flight 
	WHERE flightid = f_id;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION flight_insert(
	p_id INT, 
	dairp_id INT, 
	aairp_id INT, 
	f_time TIMESTAMP, 
	f_duration INTERVAL, 
	f_bprice INT
)
RETURNS INT AS $$
DECLARE f_id INT;
BEGIN
	INSERT INTO flight ( planeid, departureairportid, arrivalairportid, flighttime, duration, baseticketprice )
    VALUES ( p_id, dairp_id, aairp_id, f_time,  f_duration, f_bprice)
    RETURNING flightid INTO f_id;
    RETURN f_id;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

CREATE OR REPLACE FUNCTION ticket_select()
RETURNS TABLE(
	tid INT,
	fid INT, 
	fn VARCHAR(255), 
	pn VARCHAR(10),
	sn VARCHAR(3),
	ml VARCHAR(3),
	pr INT
) AS $$
BEGIN
	RETURN QUERY 
	SELECT ticketid, flightid, fullname, passportnumber, seatnumber, meal, price
	FROM ticket
	ORDER BY ticketid;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION ticket_select_one(t_id INT)
RETURNS TABLE(
	fid INT, 
	fn VARCHAR(255), 
	pn VARCHAR(10),
	sn VARCHAR(3),
	ml VARCHAR(3),
	pr INT
) AS $$
BEGIN
	RETURN QUERY
	SELECT flightid, fullmame, passportnumber, seatnumber, meal, price
	FROM ticket 
	WHERE ticketid = t_id;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION ticket_insert(
	f_id INT, 
	t_fname VARCHAR(255), 
	t_passport VARCHAR(10), 
	t_seat VARCHAR(3), 
	t_meal VARCHAR(3)
)
RETURNS INT AS $$
DECLARE t_id INT;
BEGIN
	INSERT INTO ticket ( flightid, fullname, passportnumber, seatnumber, meal )
    VALUES ( f_id, t_fname, t_passport, t_seat, t_meal )
    RETURNING ticketid INTO t_id;
    RETURN t_id;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;
