from PyQt5.QtWidgets import QTableView, QMessageBox, QApplication
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont
import db

from .Model import Model
from .Dialog import Dialog


class View(QTableView):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        model = Model(parent=self)
        title = QApplication.translate('Tickets.View', 'ID')
        model.setHeaderData(0, Qt.Horizontal, title)
        title = QApplication.translate('Ticket.View', 'Flight ID')
        model.setHeaderData(1, Qt.Horizontal, title)
        title = QApplication.translate('Ticket.View', 'Passenger full name')
        model.setHeaderData(2, Qt.Horizontal, title)
        title = QApplication.translate('Ticket.View', 'Passport series and number')
        model.setHeaderData(3, Qt.Horizontal, title)
        title = QApplication.translate('Ticket.View', 'Seat number')
        model.setHeaderData(4, Qt.Horizontal, title)
        title = QApplication.translate('Ticket.View', 'Lunch on board')
        model.setHeaderData(5, Qt.Horizontal, title)
        title = QApplication.translate('Tickets.View', 'Price')
        model.setHeaderData(6, Qt.Horizontal, title)
        self.setModel(model)
        
        font = QFont()
        font.setPointSize(20)
        self.setFont(font)
                
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        self.setWordWrap(False)
        
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        self.hideColumn(0)
        self.setWordWrap(False)
        
        vh = self.verticalHeader()
        vh.setSectionResizeMode(vh.Fixed)
        vh.setVisible(False)
        self.setVerticalHeader(vh)
        
        hh = self.horizontalHeader()
        hh.setSectionResizeMode(hh.ResizeToContents)
        hh.setStyleSheet("QHeaderView { font-size: 20pt; }") 
    
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
        if self.ticketid:
            dia = Dialog(parent=self)
            data = db.Ticket(ticketid=self.ticketid).load()
            dia.put(data)
            if dia.exec():
                dia.get(data)
                data.save()
                self.model().fresh()
        else:
            QMessageBox.warning(self, 'Билет', 'Сначала выберете нужный билет')
    
    @pyqtSlot()
    def delete(self):
        if self.ticketid:
            title = QApplication.translate('Tickets.View', 'Ticket')
            q = QApplication.translate('Tickets.View', 'Are you sure?')
            ans = QMessageBox.question(self, title, q)
            if ans == QMessageBox.Yes:
                db.Ticket(ticketid=self.ticketid).delete()
                self.model().fresh()
        else:
            QMessageBox.warning(self, 'Билет', 'Сначала выберете нужный билет')
    
    @pyqtSlot()
    def truncate(self):
        title = QApplication.translate('Tickets.View', 'Ticket')
        q = QApplication.translate('Tickets.View', 'Are you sure?')
        ans = QMessageBox.question(self, title, q)
        if ans == QMessageBox.Yes:
            db.Ticket().truncate()
            self.model().fresh()
