from PyQt5.QtWidgets import QTableView, QMessageBox
from PyQt5.QtCore import pyqtSlot
import db

from .Model import Model
from .Dialog import Dialog


class View(QTableView):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        model = Model(parent=self)
        self.setModel(model)
        
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        self.setWordWrap(False)
        
        vh = self.verticalHeader()
        vh.setSectionResizeMode(vh.Fixed)
        
        hh = self.horizontalHeader()
        hh.setSectionResizeMode(hh.ResizeToContents)
    
    @property
    def flightid(self):
        row = self.currentIndex().row()
        return self.model().record(row).value(0)
    
    @pyqtSlot()
    def add(self):
        dia = Dialog(parent=self)
        if dia.exec():
            data = db.Flight()
            dia.get(data)
            data.save()
            self.model().fresh()
    
    @pyqtSlot()
    def update(self):
        # @FIXME: При редактировании без выбора выдаёт ошибку
        dia = Dialog(parent=self)
        data = db.Flight(flightid=self.flightid).load()
        dia.put(data)
        if dia.exec():
            dia.get(data)
            data.save()
            self.model().fresh()
    
    @pyqtSlot()
    def delete(self):
        # @FIXME: При удалении без выбора удаляется первый по списку
        ans = QMessageBox.question(self, 'Рейс', 'Вы уверены?')
        if ans == QMessageBox.Yes:
            db.Flight(flightid=self.flightid).delete()
            self.model().fresh()
