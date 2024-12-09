from dataclasses import dataclass
import psycopg2
import settings as st


INSERT = '''
    INSERT INTO Airport ( AirportName, City )
    VALUES ( %s, %s )
    RETURNING AirportID;
'''


SELECT_ONE = '''
    SELECT AirportName, City
    FROM Airport
    WHERE AirportID = %s;
'''


UPDATE = '''
    UPDATE Airport SET
        AirportName = %s,
        City = %s
    WHERE AirportID = %s;
'''


DELETE = '''
    DELETE FROM Airport
    WHERE AirportID = %s;
'''


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
        cursor = conn.cursor()
        cursor.execute(INSERT, self.airport_data)
        (self.airportid, ) = next(cursor)
        conn.commit()
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
        cursor = conn.cursor()
        cursor.execute(SELECT_ONE, (self.airportid, ))
        (self.airportname, self.city) = next(cursor)
        conn.commit()
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
