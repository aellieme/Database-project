from PyQt5.QtSql import QSqlQueryModel
import psycopg2
import settings as st


SELECT = '''
    SELECT AirportID, AirportName, City
    FROM Airport;
'''


#INSERT = '''
#    INSERT INTO Airport ( AirportName, City )
#    VALUES ( %s, %s );
#'''


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


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fresh()
    
    def fresh(self):
        self.setQuery(SELECT)
    
#    def add(self, name, city):
#        conn = psycopg2.connect(**st.db_params)
#        cursor = conn.cursor()
#        data = (name, city)
#        cursor.execute(INSERT, data)
#        conn.commit()
#        conn.close()
#        self.fresh()
    
    def update(self, id_airport, name, city):
        # @FIXME: При редактировании без выбора выдаёт ошибку
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        data = (name, city, id_airport)
        cursor.execute(UPDATE, data)
        conn.commit()
        conn.close()
        self.fresh()
    
    def delete(self, id_airport):
        # @FIXME: При удалении без выбора удаляется первый по списку
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        data = (id_airport,)
        cursor.execute(DELETE, data)
        conn.commit()
        conn.close()
        self.fresh()
