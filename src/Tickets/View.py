from PyQt5.QtWidgets import QTableView, QMessageBox, QApplication
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
        self.hideColumn(0)
        self.setWordWrap(False)
        
        vh = self.verticalHeader()
        vh.setSectionResizeMode(vh.Fixed)
        
        hh = self.horizontalHeader()
        hh.setSectionResizeMode(hh.ResizeToContents)
    
    @property
    def ticketid(self):
        row = self.currentIndex().row()
        return self.model().record(row).value(0)
    
    @pyqtSlot()
    def add(self):
        dia = Dialog(parent=self)
        if dia.exec():
            data = db.Ticket()
            dia.get(data)
            data.save()
            self.model().fresh()
    
    @pyqtSlot()
    def update(self):
        dia = Dialog(parent=self)
        data = db.Ticket(ticketid=self.ticketid).load()
        dia.put(data)
        if dia.exec():
            dia.get(data)
            data.save()
            self.model().fresh()
    
    @pyqtSlot()
    def delete(self):
        title = QApplication.translate('Tickets.View', 'Ticket')
        q = QApplication.translate('Tickets.View', 'Are you sure?')
        ans = QMessageBox.question(self, title, q)
        if ans == QMessageBox.Yes:
            db.Ticket(ticketid=self.ticketid).delete()
            self.model().fresh()
    
    @pyqtSlot()
    def truncate(self):
        title = QApplication.translate('Tickets.View', 'Ticket')
        q = QApplication.translate('Tickets.View', 'Are you sure?')
        ans = QMessageBox.question(self, title, q)
        if ans == QMessageBox.Yes:
            db.Ticket().truncate()
            self.model().fresh()
