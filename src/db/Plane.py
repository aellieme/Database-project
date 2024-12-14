from dataclasses import dataclass
import psycopg2
import settings as st


INSERT = 'SELECT * FROM plane_insert(%s, %s, %s);'

SELECT_ONE = 'SELECT * FROM plane_select_one(%s);'

UPDATE = 'CALL plane_update(%s, %s, %s, %s);'

DELETE = 'CALL plane_delete(%s);'

TRUNCATE = 'CALL plane_truncate();'


@dataclass
class Plane(object):
    
    planeid: int = None
    airlineid: int = None
    model: str = None
    capacity: int = None
    
    @property
    def plane_data(self):
        return (self.airlineid, self.model, self.capacity)
    
    @property
    def plane_upd_data(self):
        return (self.airlineid, self.model, self.capacity, self.planeid)
    
    def insert(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(INSERT, self.plane_data)
                    (self.planeid, ) = next(cursor)
        finally:
            conn.close()
    
    def update(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(UPDATE, self.plane_upd_data)
        finally:
            conn.close()
    
    def save(self):
        if self.planeid is None:
            return self.insert()
        else:
            return self.update()
    
    def load(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(SELECT_ONE, (self.planeid, ))
                    (self.airlineid, self.model, self.capacity) = next(cursor)
        finally:
            conn.close()
        
        return self
    
    def truncate(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(TRUNCATE)
        finally:
            conn.close()
    
    def delete(self):
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(DELETE, (self.planeid, ))
        finally:
            conn.close()
    
    def exist_key(self) -> bool:
        conn = psycopg2.connect(**st.db_params)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(SELECT_ONE, (self.planeid, ))
                    result = cursor.fetchone()
        finally:
            conn.close()
        
        return result is not None
    