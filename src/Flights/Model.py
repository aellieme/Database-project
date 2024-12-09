from PyQt5.QtSql import QSqlQueryModel
import psycopg2
import settings as st


SELECT = '''
    SELECT FlightID, PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice
    FROM Flight;
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


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fresh()
    
    def fresh(self):
        self.setQuery(SELECT)
    
    def update(self, id_flight, id_plane, id_dairport, id_aairport, ftime, duration, bprice):
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        data = (id_plane, id_dairport, id_aairport, ftime, duration, bprice, id_flight)
        cursor.execute(UPDATE, data)
        conn.commit()
        conn.close()
        self.fresh()
    
    def delete(self, id_flight):
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        data = (id_flight,)
        cursor.execute(DELETE, data)
        conn.commit()
        conn.close()
        self.fresh()
