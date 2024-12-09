from PyQt5.QtSql import QSqlQueryModel
import psycopg2
import settings as st


SELECT = '''
    SELECT PlaneID, AirlineID, Model, Capacity
    FROM Plane;
'''


#INSERT = '''
#    INSERT INTO Plane ( AirlineID, Model, Capacity )
#    VALUES ( %s, %s, %s );
#'''


UPDATE = '''
    UPDATE Plane SET
        AirlineID = %s,
        Model = %s,
        Capacity = %s
    WHERE PlaneID = %s;
'''


DELETE = '''
    DELETE FROM Plane
    WHERE PlaneID = %s;
'''


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fresh()
    
    def fresh(self):
        self.setQuery(SELECT)
    
#    def add(self, id_airline, pmodel, capacity):
#        conn = psycopg2.connect(**st.db_params)
#        cursor = conn.cursor()
#        data = (id_airline, pmodel, capacity)
#        cursor.execute(INSERT, data)
#        conn.commit()
#        conn.close()
#        self.fresh()
    
    def update(self, id_plane, id_airline, pmodel, capacity):
        # @FIXME: При редактировании без выбора выдаёт ошибку
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        data = (id_airline, pmodel, capacity, id_plane)
        cursor.execute(UPDATE, data)
        conn.commit()
        conn.close()
        self.fresh()
    
    def delete(self, id_plane):
        # @FIXME: При удалении без выбора удаляется первый по списку
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        data = (id_plane,)
        cursor.execute(DELETE, data)
        conn.commit()
        conn.close()
        self.fresh()
