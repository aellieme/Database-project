from dataclasses import dataclass
import psycopg2
import settings as st


INSERT = '''
    INSERT INTO Plane ( AirlineID, Model, Capacity )
    VALUES ( %s, %s, %s )
    RETURNING PlaneID;
'''


SELECT_ONE = '''
    SELECT AirlineID, Model, Capacity
    FROM Plane
    WHERE PlaneID = %s;
'''


UPDATE = '''
    UPDATE Plane SET
        AirlineID = %s,
        Model = %s,
        Capacity = %s
    WHERE PlaneID = %s;
'''


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
        cursor = conn.cursor()
        cursor.execute(INSERT, self.plane_data)
        (self.planeid, ) = next(cursor)
        conn.commit()
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
        cursor = conn.cursor()
        cursor.execute(SELECT_ONE, (self.planeid, ))
        (self.airlineid, self.model, self.capacity) = next(cursor)
        conn.commit()
        conn.close()
        return self
    