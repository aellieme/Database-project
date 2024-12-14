from dataclasses import dataclass
import psycopg2
import settings as st


INSERT = 'SELECT * FROM airline_insert(%s, %s);'

SELECT_ONE = 'SELECT * FROM airline_select_one(%s);'

UPDATE = 'CALL airline_update(%s, %s, %s);'

DELETE = 'CALL airline_delete(%s);'

TRUNCATE = 'CALL airline_truncate();'


@dataclass
class Airline(object):
    
    airlineid: int = None
    airlinename: str = None
    iatacode: str = None
    
    @property
    def airline_data(self):
        return (self.airlinename, self.iatacode)
    
    @property
    def airline_upd_data(self):
        return (self.airlinename, self.iatacode, self.airlineid)
        
    def insert(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(INSERT, self.airline_data)
                    (self.airlineid, ) = next(cursor)
        finally:
            conn.close()

    def update(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(UPDATE, self.airline_upd_data)
        finally:
            conn.close()
    
    def save(self):
        if self.airlineid is None:
            return self.insert()
        else:
            return self.update()
            
    def load(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(SELECT_ONE, (self.airlineid, ))
                    (self.airlinename, self.iatacode) = next(cursor)
        finally:
            conn.close()
        
        return self
    
    def delete(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(DELETE, (self.airlineid, ))
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
                    cursor.execute(SELECT_ONE, (self.airlineid, ))
                    result = cursor.fetchone()
        finally:
            conn.close()
        
        return result is not None
