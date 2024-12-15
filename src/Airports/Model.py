from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import Qt


SELECT = '''SELECT * FROM airport_select();'''

SEARCH = '''SELECT * FROM airport_search('{name}');'''


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None, name=None):
        super().__init__(parent)
        self.__name = name
        self.fresh()
        
        self.setHeaderData(0, Qt.Horizontal, 'ID')
        self.setHeaderData(1, Qt.Horizontal, 'Название аэропорта')
        self.setHeaderData(2, Qt.Horizontal, 'Город')
        if self.__name is not None:
            self.setHeaderData(3, Qt.Horizontal, 'Схожесть')
    
    def fresh(self):
        if self.__name is not None:
            self.setQuery(SEARCH.format(name=self.__name))
        else:
            self.setQuery(SELECT)
