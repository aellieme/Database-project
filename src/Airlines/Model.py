from PyQt5.QtSql import QSqlQueryModel


SELECT = '''
    SELECT AirlineID, AirlineName, IATACode
    FROM Airline;
'''


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fresh()
    
    def fresh(self):
        self.setQuery(SELECT)
