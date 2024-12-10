from PyQt5.QtSql import QSqlQueryModel


SELECT = '''
    SELECT PlaneID, AirlineID, Model, Capacity
    FROM Plane;
'''


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fresh()
    
    def fresh(self):
        self.setQuery(SELECT)
