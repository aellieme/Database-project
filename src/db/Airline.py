from dataclasses import dataclass
import psycopg2
import settings as st


INSERT = '''
    INSERT INTO Airline ( AirlineName, IATACode )
    VALUES ( %s, %s )
    RETURNING AirlineId;
'''


SELECT_ONE = '''
    SELECT AirlineName, IATACode
    FROM Airline
    WHERE AirlineID = %s;
'''


UPDATE = '''
    UPDATE Airline SET
        AirlineName = %s,
        IATACode = %s
    WHERE AirlineID = %s;
'''


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
        cursor = conn.cursor()
        cursor.execute(INSERT, self.airline_data)
        (self.airlineid, ) = next(cursor)
        conn.commit()
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
        cursor = conn.cursor()
        cursor.execute(SELECT_ONE, (self.airlineid, ))
        (self.airlinename, self.iatacode) = next(cursor)
        conn.commit()
        conn.close()
        return self
