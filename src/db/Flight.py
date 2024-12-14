from dataclasses import dataclass
import psycopg2
import settings as st

import datetime as dt


INSERT = 'SELECT * FROM flight_insert(%s, %s, %s, %s, %s, %s);'

SELECT_ONE = 'SELECT * FROM flight_select_one(%s);'

UPDATE = 'CALL flight_update(%s, %s, %s, %s, %s, %s, %s);'

DELETE = 'CALL flight_delete(%s);'

TRUNCATE = 'CALL flight_truncate();'


@dataclass
class Flight(object):
    
    flightid: int = None
    planeid: int = None
    departureairportid: int = None
    arrivalairportid: int = None
    flighttime: dt.datetime = None
    duration: dt.timedelta = None
    baseticketprice: int = None
    
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
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(INSERT, self.flight_data)
                    (self.flightid, ) = next(cursor)
        finally:
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
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(SELECT_ONE, (self.flightid, ))
                    (self.planeid, self.departureairportid, self.arrivalairportid, self.flighttime,
                     self.duration, self.baseticketprice) = next(cursor)
        finally:
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
                    cursor.execute(SELECT_ONE, (self.flightid, ))
                    result = cursor.fetchone()
        finally:
            conn.close()
        
        return result is not None
