from PyQt5.QtSql import QSqlQueryModel


SELECT = 'SELECT * FROM flight_select();'


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fresh()
    
    def fresh(self):
        self.setQuery(SELECT)
