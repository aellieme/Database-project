START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

CREATE PROCEDURE airport_select()
AS $$
BEGIN
    SELECT AirportID, AirportName, City
    FROM Airport;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE airport_select_one(airp_id INT)
AS $$
BEGIN
    SELECT AirportName, City
    FROM Airport
    WHERE AirportID = airp_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE airport_update(
	airp_name VARCHAR(100), 
	airp_city VARCHAR(100), 
	airp_id INT
)
AS $$
BEGIN
    UPDATE Airport SET
        AirportName = airp_name,
        City = airp_city
    WHERE AirportID = airp_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE airport_delete(airp_id INT)
AS $$
BEGIN
    DELETE FROM Airport
    WHERE AirportID = airp_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE airport_truncate()
AS $$
BEGIN
    TRUNCATE TABLE Airport CASCADE;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE airport_insert(
	airp_name VARCHAR(100), 
	airp_city VARCHAR(100),
	OUT airp_id INT
)
AS $$
BEGIN
    INSERT INTO Airport ( AirportName, City )
    VALUES ( airp_name, airp_city )
    RETURNING AirportID INTO airp_id;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

CREATE PROCEDURE airline_select()
AS $$
BEGIN
    SELECT AirlineID, AirlineName, IATACode
    FROM Airline;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE airline_select_one(airl_id INT)
AS $$
BEGIN
    SELECT AirlineName, IATACode
    FROM Airline
    WHERE AirlineID = airl_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE airline_update(
	airl_name VARCHAR(100), 
	airl_code VARCHAR(3), 
	airl_id INT
)
AS $$
BEGIN
    UPDATE Airline SET
        AirlineName = airl_name,
        IATACode = airl_code
    WHERE AirlineID = airl_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE airline_delete(airl_id INT)
AS $$
BEGIN
    DELETE FROM Airline
    WHERE AirlineID = airl_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE airline_truncate()
AS $$
BEGIN
    TRUNCATE TABLE Airline CASCADE;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE airline_insert(
	airl_name VARCHAR(100), 
	airl_code VARCHAR(3), 
	OUT airl_id INT
)
AS $$
BEGIN
    INSERT INTO Airline ( AirlineName, IATACode )
    VALUES ( airl_name, airl_code )
    RETURNING AirlineId INTO airl_id;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

CREATE PROCEDURE plane_select()
AS $$
BEGIN
    SELECT PlaneID, AirlineID, Model, Capacity
    FROM Plane;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE plane_select_one(p_id INT)
AS $$
BEGIN
    SELECT AirlineID, Model, Capacity
    FROM Plane
    WHERE PlaneID = p_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE plane_update(
	airl_id INT, 
	p_model VARCHAR(100), 
	p_capacity INT, 
	p_id INT
)
AS $$
BEGIN
    UPDATE Plane SET
        AirlineID = airl_id,
        Model = p_model,
        Capacity = p_capacity
    WHERE PlaneID = p_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE plane_delete(p_id INT)
AS $$
BEGIN
    DELETE FROM Plane
    WHERE PlaneID = p_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE plane_truncate()
AS $$
BEGIN
    TRUNCATE TABLE Plane CASCADE;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE plane_insert(
	airl_id INT, 
	p_model VARCHAR(100), 
	p_capacity INT, 
	OUT p_id INT
)
AS $$
BEGIN
    INSERT INTO Plane ( AirlineID, Model, Capacity )
    VALUES ( airl_id, p_model, p_capacity )
    RETURNING PlaneID INTO p_id;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

CREATE PROCEDURE flight_select()
AS $$
BEGIN
    SELECT FlightID, PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice
    FROM Flight;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE flight_select_one(f_id INT)
AS $$
BEGIN
    SELECT PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice
    FROM Flight
    WHERE FlightID = f_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE flight_update(
	p_id INT, 
	dairp_id INT, 
	aairp_id INT, 
	f_time TIMESTAMP, 
	f_duration INTERVAL, 
	f_bprice INT, 
	f_id INT
)
AS $$
BEGIN
    UPDATE Flight SET
        PlaneID = p_id,
        DepartureAirportID = dairp_id,
        ArrivalAirportID = aairp_id,
        FlightTime = f_time, 
        Duration = f_duration,
        BaseTicketPrice = f_bprice
    WHERE FlightID = f_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE flight_delete(f_id INT)
AS $$
BEGIN
    DELETE FROM Flight
    WHERE FlightID = f_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE flight_truncate()
AS $$
BEGIN
    TRUNCATE TABLE Flight CASCADE;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE flight_insert(
	p_id INT, 
	dairp_id INT, 
	aairp_id INT, 
	f_time TIMESTAMP, 
	f_duration INTERVAL, 
	f_bprice INT, 
	OUT f_id INT
)
AS $$
BEGIN
    INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
    VALUES ( p_id, dairp_id, aairp_id, f_time,  f_duration, f_bprice)
    RETURNING FlightID INTO f_id;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

CREATE PROCEDURE ticket_select()
AS $$
BEGIN
    SELECT TicketID, FlightID, FullName, PassportNumber, SeatNumber, Meal, Price
    FROM Ticket;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE ticket_select_one(t_id INT)
AS $$
BEGIN
    SELECT FlightID, FullName, PassportNumber, SeatNumber, Meal, Price
    FROM Ticket
    WHERE TicketID = t_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE ticket_update(
	f_id INT, 
	t_fname VARCHAR(255), 
	t_passport VARCHAR(10), 
	t_seat VARCHAR(3), 
	t_meal VARCHAR(3), 
	t_id INT
)
AS $$
BEGIN
    UPDATE Ticket SET
        FlightID = f_id,
        FullName = t_fname,
        PassportNumber = t_passport,
        SeatNumber = t_seat,
        Meal = t_meal
    WHERE TicketID = t_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE ticket_delete(t_id INT)
AS $$
BEGIN
    DELETE FROM Ticket
    WHERE TicketID = t_id;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE ticket_truncate()
AS $$
BEGIN
    TRUNCATE TABLE Ticket CASCADE;
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE ticket_insert(
	f_id INT, 
	t_fname VARCHAR(255), 
	t_passport VARCHAR(10), 
	t_seat VARCHAR(3), 
	t_meal VARCHAR(3), 
	OUT t_id INT,
	OUT t_price INT
)
AS $$
BEGIN
    INSERT INTO Ticket ( FlightID, FullName, PassportNumber, SeatNumber, Meal )
    VALUES ( f_id, t_fname, t_passport, t_seat, t_meal )
    RETURNING TicketID, Price INTO t_id, t_price;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;