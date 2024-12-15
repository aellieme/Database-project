from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import Qt


SELECT = '''SELECT * FROM airport_select();'''

SEARCH = '''SELECT * FROM airport_search('{name}');'''


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fresh()
        
        self.setHeaderData(0, Qt.Horizontal, 'ID')
        self.setHeaderData(1, Qt.Horizontal, 'Название аэропорта')
        self.setHeaderData(2, Qt.Horizontal, 'Город')
    
    def fresh(self, *, name=None):
        if name:
            self.setQuery(SEARCH.format(name=name))
            self.setHeaderData(3, Qt.Horizontal, 'Схожесть')
        else:
            self.setQuery(SELECT)
