from dataclasses import dataclass
import psycopg2
import settings as st


INSERT = '''
    INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
    VALUES ( %s, %s, %s, %s,  %s, %s)
    RETURNING FlightID;
'''


SELECT_ONE = '''
    SELECT PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice
    FROM Flight
    WHERE FlightID = %s;
'''


UPDATE = '''
    UPDATE Flight SET
        PlaneID = %s,
        DepartureAirportID = %s,
        ArrivalAirportID = %s,
        FlightTime = %s, 
        Duration = %s,
        BaseTicketPrice = %s
    WHERE FlightID = %s;
'''


DELETE = '''
    DELETE FROM Flight
    WHERE FlightID = %s;
'''


@dataclass
class Flight(object):
    
    flightid: int = None
    planeid: int = None
    departureairportid: int = None
    arrivalairportid: int = None
    flighttime: str = None
    duration: str = None
    baseticketprice: float = None
    
    @property
    def flight_data(self):
        return (self.planeid, self.departureairportid, self.arrivalairportid, 
                self.flighttime, self.duration, self.baseticketprice)
    
    @property
    def flight_upd_data(self):
        return (self.planeid, self.departureairportid, self.arrivalairportid, 
                self.flighttime, self.duration, self.baseticketprice, self.flightid)
    
    def insert(self):
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        cursor.execute(INSERT, self.flight_data)
        (self.flightid, ) = next(cursor)
        conn.commit()
        conn.close()
    
    def update(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(UPDATE, self.flight_upd_data)
        finally:
            conn.close()
    
    def save(self):
        if self.flightid is None:
            return self.insert()
        else:
            return self.update()
    
    def load(self):
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        cursor.execute(SELECT_ONE, (self.flightid, ))
        (self.planeid, self.departureairportid, self.arrivalairportid, self.flighttime, 
         self.duration, self.baseticketprice) = next(cursor)
        conn.commit()
        conn.close()
        return self
    
    def delete(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(DELETE, (self.flightid, ))
        finally:
            conn.close()
