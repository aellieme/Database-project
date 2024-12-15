from PyQt5.QtWidgets import QTableView, QMessageBox, QApplication
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
#import emoji


import db

from .Model import Model
from .Dialog import Dialog


class View(QTableView):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__model = Model(parent=self)
        self.setModel(self.__model)
        
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
        
        # widget
        self.__widget = QWidget()
        lay = QVBoxLayout()
        
        font = QFont()
        font.setPointSize(15)
        
        lbl = QLabel('Поиск по названию аэропорта:')
        lbl.setFont(font)
        lay.addWidget(lbl)
        
        lay_hor = QHBoxLayout()
        self.__name_edt = QLineEdit()
        self.__name_edt.setMinimumHeight(30)
        self.__name_edt.setFont(font)
        self.srch_btn = QPushButton('Найти')#emoji.emojize('Найти :magnifying_glass_tilted_right:', language='alias'))
        self.srch_btn.setMinimumWidth(200)
        self.srch_btn.setFont(font)
        lay_hor.addWidget(self.__name_edt)
        lay_hor.addWidget(self.srch_btn)
        
        lay.addLayout(lay_hor)
        lay.addWidget(self)
        self.widget.setLayout(lay)
        
        self.srch_btn.clicked.connect(self.search)
    
    @property
    def widget(self):
        return self.__widget
    
    @property
    def name(self):
        result = self.__name_edt.text().strip()
        return result if result else None
    
    @property
    def airportid(self):
        row = self.currentIndex().row()
        return self.model().record(row).value(0)
    
    @pyqtSlot()
    def add(self):
        self.setModel(self.__model)
        dia = Dialog(parent=self)
        if dia.exec():
            data = db.Airport()
            dia.get(data)
            data.save()
            self.model().fresh()
    
    @pyqtSlot()
    def update(self):
        self.setModel(self.__model)
        dia = Dialog(parent=self)
        data = db.Airport(airportid=self.airportid).load()
        dia.put(data)
        if dia.exec():
            dia.get(data)
            data.save()
            self.model().fresh()
    
    @pyqtSlot()
    def delete(self):
        self.setModel(self.__model)
        title = QApplication.translate('Airports.View', 'Airport')
        q = QApplication.translate('Airports.View', 'Are you sure?')
        ans = QMessageBox.question(self, title, q)
        if ans == QMessageBox.Yes:
            db.Airport(airportid=self.airportid).delete()
            self.model().fresh()
    
    @pyqtSlot()
    def truncate(self):
        self.setModel(self.__model)
        title = QApplication.translate('Airports.View', 'Airport')
        q = QApplication.translate('Airports.View', 'Are you sure?')
        ans = QMessageBox.question(self, title, q)
        if ans == QMessageBox.Yes:
            db.Airport().truncate()
            self.model().fresh()
    
    @pyqtSlot()
    def search(self):
        self.setModel(Model(parent=self, name=self.name))
        self.model().fresh()
