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
        title = QApplication.translate('Flights.View', 'ID')
        model.setHeaderData(0, Qt.Horizontal, title)
        title = QApplication.translate('Flight.View', 'Plane ID')
        model.setHeaderData(1, Qt.Horizontal, title)
        title = QApplication.translate('Flight.View', 'Departure Airport ID')
        model.setHeaderData(2, Qt.Horizontal, title)
        title = QApplication.translate('Flight.View', 'Arrival Airport ID')
        model.setHeaderData(3, Qt.Horizontal, title)
        title = QApplication.translate('Flight.View', 'Departure date and time')
        model.setHeaderData(4, Qt.Horizontal, title)
        title = QApplication.translate('Flight.View', 'Flight duration')
        model.setHeaderData(5, Qt.Horizontal, title)
        title = QApplication.translate('Flight.View', 'Base Ticket Price')
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
        self.setWordWrap(False)
        
        vh = self.verticalHeader()
        vh.setSectionResizeMode(vh.Fixed)
        vh.setVisible(False)
        self.setVerticalHeader(vh)
        
        hh = self.horizontalHeader()
        hh.setSectionResizeMode(hh.ResizeToContents)
        hh.setStyleSheet("QHeaderView { font-size: 20pt; }")  
    
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
        if self.flightid:
            dia = Dialog(parent=self)
            data = db.Flight(flightid=self.flightid).load()
            dia.put(data)
            if dia.exec():
                dia.get(data)
                data.save()
                self.model().fresh()
        else:
            QMessageBox.warning(self, 'Рейс', 'Сначала выберете нужный рейс')
    
    @pyqtSlot()
    def delete(self):
        if self.flightid:
            title = QApplication.translate('Flights.View', 'Flight')
            q = QApplication.translate('Flights.View', 'Are you sure?')
            ans = QMessageBox.question(self, title, q)
            if ans == QMessageBox.Yes:
                db.Flight(flightid=self.flightid).delete()
                self.model().fresh()
        else:
            QMessageBox.warning(self, 'Рейс', 'Сначала выберете нужный рейс')
    
    @pyqtSlot()
    def truncate(self):
        title = QApplication.translate('Flights.View', 'Flight')
        q = QApplication.translate('Flights.View', 'Are you sure?')
        ans = QMessageBox.question(self, title, q)
        if ans == QMessageBox.Yes:
            db.Flight().truncate()
            self.model().fresh()
