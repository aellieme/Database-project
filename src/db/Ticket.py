from dataclasses import dataclass
import psycopg2
import settings as st


INSERT = '''
    INSERT INTO Ticket ( FlightID, FullName, PassportNumber, SeatNumber, Meal )
    VALUES ( %s, %s, %s, %s, %s )
    RETURNING TicketID, Price;
'''


SELECT_ONE = '''
    SELECT FlightID, FullName, PassportNumber, SeatNumber, Meal, Price
    FROM Ticket
    WHERE TicketID = %s;
'''


UPDATE = '''
    UPDATE Ticket SET
        FlightID = %s,
        FullName = %s,
        PassportNumber = %s,
        SeatNumber = %s,
        Meal = %s
    WHERE TicketID = %s;
'''


DELETE = '''
    DELETE FROM Ticket
    WHERE TicketID = %s;
'''


@dataclass
class Ticket(object):
    
    ticketid: int = None
    flightid: int = None
    fullname: str = None
    passportnumber: str = None
    seatnumber: str = None
    meal: str = None
    price: float = None
    
    @property
    def ticket_data(self):
        return (self.flightid, self.fullname, self.passportnumber, self.seatnumber, self.meal)
    
    @property
    def ticket_upd_data(self):
        return (self.flightid, self.fullname, self.passportnumber, self.seatnumber, self.meal, self.ticketid)
    
    def insert(self):
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        cursor.execute(INSERT, self.ticket_data)
        (self.ticketid, self.price) = next(cursor)
        conn.commit()
        conn.close()
    
    def update(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(UPDATE, self.ticket_upd_data)
        finally:
            conn.close()
    
    def save(self):
        if self.ticketid is None:
            return self.insert()
        else:
            return self.update()
    
    def load(self):
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        cursor.execute(SELECT_ONE, (self.ticketid, ))
        (self.flightid, self.fullname, self.passportnumber, 
         self.seatnumber, self.meal, self.price) = next(cursor)
        conn.commit()
        conn.close()
        return self
    
    def delete(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(DELETE, (self.ticketid, ))
        finally:
            conn.close()
