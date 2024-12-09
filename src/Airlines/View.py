from PyQt5.QtWidgets import QTableView, QMessageBox
from PyQt5.QtCore import pyqtSlot
import psycopg2
import settings as st
import db

from .Model import Model
from .Dialog import Dialog


SELECT_ONE = '''
    SELECT AirlineName, IATACode
    FROM Airline
    WHERE AirlineID = %s;
'''


class View(QTableView):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        model = Model(parent=self)
        self.setModel(model)
        
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        self.hideColumn(0)
        self.setWordWrap(False)
        
        vh = self.verticalHeader()
        vh.setSectionResizeMode(vh.Fixed)
        
        hh = self.horizontalHeader()
        hh.setSectionResizeMode(hh.ResizeToContents)
    
    @property
    def airlineid(self):
        row = self.currentIndex().row()
        return self.model().record(row).value(0)
    
    @pyqtSlot()
    def add(self):
        dia = Dialog(parent=self)
        if dia.exec():
            data = db.Airline()
            dia.get(data)
            data.save()
            self.model().fresh()
    
    @pyqtSlot()
    def update(self):
        # @FIXME: При редактировании без выбора выдаёт ошибку
        dia = Dialog(parent=self)
        data = db.Airline(airlineid=self.airlineid).load()
        dia.put(data)
        if dia.exec():
            dia.get(data)
            data.save()
            self.model().fresh()
    
    @pyqtSlot()
    def delete(self):
        # @FIXME: При удалении без выбора удаляется первый по списку
        row = self.currentIndex().row()
        id_airline = self.model().record(row).value(0)
        ans = QMessageBox.question(self, 'Авиакомпания', 'Вы уверены?')
        if ans == QMessageBox.Yes:
            self.model().delete(id_airline)
