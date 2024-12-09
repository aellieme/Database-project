from PyQt5.QtSql import QSqlQueryModel
import psycopg2
import settings as st


SELECT = '''
    SELECT AirlineID, AirlineName, IATACode
    FROM Airline;
'''


UPDATE = '''
    UPDATE Airline SET
        AirlineName = %s,
        IATACode = %s
    WHERE AirlineID = %s;
'''


DELETE = '''
    DELETE FROM Airline
    WHERE AirlineID = %s;
'''


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fresh()
    
    def fresh(self):
        self.setQuery(SELECT)
    
    def update(self, id_airline, name, code):
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        data = (name, code, id_airline)
        cursor.execute(UPDATE, data)
        conn.commit()
        conn.close()
        self.fresh()
    
    def delete(self, id_airline):
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        data = (id_airline,)
        cursor.execute(DELETE, data)
        conn.commit()
        conn.close()
        self.fresh()
