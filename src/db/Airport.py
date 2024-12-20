from dataclasses import dataclass
import psycopg2
import settings as st


INSERT = 'SELECT * FROM airport_insert(%s, %s);'

SELECT_ONE = 'SELECT * FROM airport_select_one(%s);'

UPDATE = 'CALL airport_update(%s, %s, %s);'

DELETE = 'CALL airport_delete(%s);'

TRUNCATE = 'CALL airport_truncate();'


@dataclass
class Airport(object):
    
    airportid: int = None
    airportname: str = None
    city: str = None
    
    @property
    def airport_data(self):
        return (self.airportname, self.city)
    
    @property
    def airport_upd_data(self):
        return (self.airportname, self.city, self.airportid)
    
    def insert(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(INSERT, self.airport_data)
                    (self.airportid, ) = next(cursor)
        finally:
            conn.close()
    
    def update(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(UPDATE, self.airport_upd_data)
        finally:
            conn.close()
    
    def save(self):
        if self.airportid is None:
            return self.insert()
        else:
            return self.update()
    
    def load(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(SELECT_ONE, (self.airportid, ))
                    (self.airportname, self.city) = next(cursor)
        finally:
            conn.close()
        
        return self
    
    def delete(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(DELETE, (self.airportid, ))
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
                    cursor.execute(SELECT_ONE, (self.airportid, ))
                    result = cursor.fetchone()
        finally:
            conn.close()
        
        return result is not None
