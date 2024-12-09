import sys
from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase
import settings as st


class Application(QApplication):
    
    def __init__(self, argv):
        super().__init__(argv)
        
        self.setup()
    
    def setup(self):
        self.connect_to_db()
        self.set_translation()
        return self
    
    def set_translation(self):
        trans = QTranslator(parent=self)
        ok = trans.load('airport_ru.qm')
        if ok:
            print('Translation loaded', file=sys.stderr)
        else:
            print('FAILED to load translation', file=sys.stderr)
        QApplication.installTranslator(trans)
    
    def connect_to_db(self):
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName(st.db_params['host'])
        db.setDatabaseName(st.db_params['dbname'])
        db.setPort(st.db_params['port'])
        db.setUserName(st.db_params['user'])
        db.setPassword(st.db_params['password'])
        ok = db.open()
        if ok:
            print('Connected to database', file=sys.stderr)
        else:
            print('Connection FAILED', file=sys.stderr)
        
