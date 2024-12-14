START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

CREATE PROCEDURE airport_update(
	airp_name VARCHAR(100), 
	airp_city VARCHAR(100), 
	airp_id INT
)
AS $$
BEGIN
    UPDATE airport SET
        airportname = airp_name,
        city = airp_city
    WHERE airportid = airp_id;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE airport_delete(airp_id INT)
AS $$
BEGIN
    DELETE FROM airport
    WHERE airportid = airp_id;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE airport_truncate()
AS $$
BEGIN
    TRUNCATE TABLE airport CASCADE;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

CREATE PROCEDURE airline_update(
	airl_name VARCHAR(100), 
	airl_code VARCHAR(3), 
	airl_id INT
)
AS $$
BEGIN
    UPDATE airline SET
        airlinename = airl_name,
        iatacode = airl_code
    WHERE airlineid = airl_id;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE airline_delete(airl_id INT)
AS $$
BEGIN
    DELETE FROM airline
    WHERE airlineid = airl_id;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE airline_truncate()
AS $$
BEGIN
    TRUNCATE TABLE airline CASCADE;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

CREATE PROCEDURE plane_update(
	airl_id INT, 
	p_model VARCHAR(100), 
	p_capacity INT, 
	p_id INT
)
AS $$
BEGIN
    UPDATE plane SET
        airlineid = airl_id,
        model = p_model,
        capacity = p_capacity
    WHERE planeid = p_id;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE plane_delete(p_id INT)
AS $$
BEGIN
    DELETE FROM plane
    WHERE planeid = p_id;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE plane_truncate()
AS $$
BEGIN
    TRUNCATE TABLE plane CASCADE;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

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
    UPDATE flight SET
        planeid = p_id,
        departureairportid = dairp_id,
        arrivalairportid = aairp_id,
        flighttime = f_time, 
        duration = f_duration,
        baseticketprice = f_bprice
    WHERE flightid = f_id;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE flight_delete(f_id INT)
AS $$
BEGIN
    DELETE FROM flight
    WHERE flightid = f_id;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE flight_truncate()
AS $$
BEGIN
    TRUNCATE TABLE flight CASCADE;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

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
    UPDATE ticket SET
        flightid = f_id,
        fullname = t_fname,
        passportnumber = t_passport,
        seatnumber = t_seat,
        meal = t_meal
    WHERE ticketid = t_id;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE ticket_delete(t_id INT)
AS $$
BEGIN
    DELETE FROM ticket
    WHERE ticketid = t_id;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE ticket_truncate()
AS $$
BEGIN
    TRUNCATE TABLE ticket CASCADE;
END;
$$ LANGUAGE plpgsql;

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;