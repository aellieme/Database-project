from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QDialog # диалоговое окно
from PyQt5.QtWidgets import QLabel # надпись на окне
from PyQt5.QtWidgets import QLineEdit # текст из одной строчки
from PyQt5.QtWidgets import QPushButton # кновка
from PyQt5.QtWidgets import QVBoxLayout # вертикальная разметка окна
from PyQt5.QtWidgets import QHBoxLayout # горизонтальная разметка окна

from PyQt5.Qt import QApplication


class Dialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        title = QApplication.translate('Plane.Dialog', 'Plane')
        self.setWindowTitle(title)
        
        title = QApplication.translate('Plane.Dialog', 'Airline ID')
        id_airline_lbl = QLabel(title, parent=self)
        self.__id_airline_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Plane.Dialog', 'Plane model')
        pmodel_lbl = QLabel(title, parent=self)
        self.__pmodel_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Plane.Dialog', 'Capacity')
        capacity_lbl = QLabel(title, parent=self)
        self.__capacity_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Plane.Dialog', 'OK')
        ok_btn = QPushButton(title, parent=self)
        title = QApplication.translate('Plane.Dialog', 'Cancel')
        cancel_btn = QPushButton(title, parent=self)
        
        lay = QVBoxLayout(self)
        
        lay_id_airline = QVBoxLayout()
        lay_id_airline.setSpacing(0)
        lay_id_airline.addWidget(id_airline_lbl)
        lay_id_airline.addWidget(self.__id_airline_edt)
        lay.addLayout(lay_id_airline)
        
        lay_pmodel = QVBoxLayout()
        lay_pmodel.setSpacing(0)
        lay_pmodel.addWidget(pmodel_lbl)
        lay_pmodel.addWidget(self.__pmodel_edt)
        lay.addLayout(lay_pmodel)
        
        lay_capacity = QVBoxLayout()
        lay_capacity.setSpacing(0)
        lay_capacity.addWidget(capacity_lbl)
        lay_capacity.addWidget(self.__capacity_edt)
        lay.addLayout(lay_capacity)
        
        layH = QHBoxLayout()
        layH.addStretch()
        layH.addWidget(ok_btn)
        layH.addWidget(cancel_btn)
        lay.addLayout(layH)
        
        cancel_btn.clicked.connect(self.reject)
        ok_btn.clicked.connect(self.finish)
    
    @pyqtSlot()
    def finish(self):
        if self.id_airline is None or self.pmodel is None or self.capacity is None:
            return 
        self.accept()
    
    @property
    def id_airline(self):
        result = self.__id_airline_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @id_airline.setter
    def id_airline(self, value):
        self.__id_airline_edt.setText(value)
    
    @property
    def pmodel(self):
        result = self.__pmodel_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @pmodel.setter
    def pmodel(self, value):
        self.__pmodel_edt.setText(value)
    
    @property
    def capacity(self):
        result = self.__capacity_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @capacity.setter
    def capacity(self, value):
        self.__capacity_edt.setText(value)
    
    def get(self, data):
        data.airlineid = self.id_airline
        data.model = self.pmodel
        data.capacity = self.capacity
    
    def put(self, data):
        self.id_airline = data.airlineid
        self.pmodel = data.model
        self.capacity = data.capacity
