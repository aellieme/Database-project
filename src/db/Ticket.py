from dataclasses import dataclass
import psycopg2
import settings as st


INSERT = 'SELECT * FROM ticket_insert(%s, %s, %s, %s, %s);'

SELECT_ONE = 'SELECT * FROM ticket_select_one(%s);'

UPDATE = 'CALL ticket_update(%s, %s, %s, %s, %s, %s);'

DELETE = 'CALL ticket_delete(%s);'

TRUNCATE = 'CALL ticket_truncate();'

CHECK_PASSPORT = 'SELECT check_duplicate_flight_passport(%s, %s);'

CHECK_SEATNUMBER = 'SELECT check_duplicate_flight_seatnumber(%s, %s);'


@dataclass
class Ticket(object):
    
    ticketid: int = None
    flightid: int = None
    fullname: str = None
    passportnumber: str = None
    seatnumber: str = None
    meal: str = None
    price: int = None
    
    @property
    def ticket_data(self):
        return (self.flightid, self.fullname, self.passportnumber, self.seatnumber, self.meal)
    
    @property
    def ticket_upd_data(self):
        return (self.flightid, self.fullname, self.passportnumber, self.seatnumber, self.meal, self.ticketid)
    
    def insert(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(INSERT, self.ticket_data)
                    (self.ticketid, ) = next(cursor)
        finally:
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
            conn = psycopg2.connect(**st.db_params)
            try:
                with conn:
                    with conn.cursor() as cursor:
                        cursor.execute(CHECK_PASSPORT, (self.flightid, self.passportnumber))
                        ok1 = next(cursor)[0]
                        cursor.execute(CHECK_SEATNUMBER, (self.flightid, self.seatnumber))
                        ok2 = next(cursor)[0]
                        if ok1 and ok2:
                            return self.insert()
                        elif not ok1:
                            return 'PASSPORT'
                        return 'SEATNUMBER'
            finally:
                conn.close()
        else:
            return self.update()
    
    def load(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(SELECT_ONE, (self.ticketid, ))
                    (self.flightid, self.fullname, self.passportnumber, 
                     self.seatnumber, self.meal, self.price) = next(cursor)
        finally:
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
    
    def truncate(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(TRUNCATE)
        finally:
            conn.close()
    
    def exist_key(self) -> bool:
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(SELECT_ONE, (self.ticketid, ))
                    result = cursor.fetchone()
        finally:
            conn.close()
        
        return result is not None
