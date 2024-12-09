from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QDialog # диалоговое окно
from PyQt5.QtWidgets import QLabel # надпись на окне
from PyQt5.QtWidgets import QLineEdit # текст из одной строчки
from PyQt5.QtWidgets import QPushButton # кновка
from PyQt5.QtWidgets import QVBoxLayout # вертикальная разметка окна
from PyQt5.QtWidgets import QHBoxLayout # горизонтальная разметка окна


class Dialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Рейс')
        
        id_plane_lbl = QLabel('ID самолета', parent=self)
        self.__id_plane_edt = QLineEdit(parent=self)
        
        id_dairport_lbl = QLabel('ID аэропорта отпраления', parent=self)
        self.__id_dairport_edt = QLineEdit(parent=self)
        
        id_aairport_lbl = QLabel('ID аэропорта прибытия', parent=self)
        self.__id_aairport_edt = QLineEdit(parent=self)
        
        ftime_lbl = QLabel('Дата и время отправления', parent=self)
        self.__ftime_edt = QLineEdit(parent=self)
        
        duration_lbl = QLabel('Время полета', parent=self)
        self.__duration_edt = QLineEdit(parent=self)
        
        bprice_lbl = QLabel('Базовая стоимость билета', parent=self)
        self.__bprice_edt = QLineEdit(parent=self)
        
        ok_btn = QPushButton('ОК', parent=self)
        cancel_btn = QPushButton('Отмена', parent=self)
        
        lay = QVBoxLayout(self)
        
        lay_id_plane = QVBoxLayout()
        lay_id_plane.setSpacing(0)
        lay_id_plane.addWidget(id_plane_lbl)
        lay_id_plane.addWidget(self.__id_plane_edt)
        lay.addLayout(lay_id_plane)
        
        lay_id_dairport = QVBoxLayout()
        lay_id_dairport.setSpacing(0)
        lay_id_dairport.addWidget(id_dairport_lbl)
        lay_id_dairport.addWidget(self.__id_dairport_edt)
        lay.addLayout(lay_id_dairport)
        
        lay_id_aairport = QVBoxLayout()
        lay_id_aairport.setSpacing(0)
        lay_id_aairport.addWidget(id_aairport_lbl)
        lay_id_aairport.addWidget(self.__id_aairport_edt)
        lay.addLayout(lay_id_aairport)
        
        lay_ftime = QVBoxLayout()
        lay_ftime.setSpacing(0)
        lay_ftime.addWidget(ftime_lbl)
        lay_ftime.addWidget(self.__ftime_edt)
        lay.addLayout(lay_ftime)
        
        lay_duration = QVBoxLayout()
        lay_duration.setSpacing(0)
        lay_duration.addWidget(duration_lbl)
        lay_duration.addWidget(self.__duration_edt)
        lay.addLayout(lay_duration)
        
        lay_bprice = QVBoxLayout()
        lay_bprice.setSpacing(0)
        lay_bprice.addWidget(bprice_lbl)
        lay_bprice.addWidget(self.__bprice_edt)
        lay.addLayout(lay_bprice)
        
        layH = QHBoxLayout()
        layH.addStretch()
        layH.addWidget(ok_btn)
        layH.addWidget(cancel_btn)
        lay.addLayout(layH)
        
        cancel_btn.clicked.connect(self.reject)
        ok_btn.clicked.connect(self.finish)
    
    @pyqtSlot()
    def finish(self):
        if self.id_plane is None or self.id_dairport is None or self.id_aairport or self.ftime is None or self.duration is None:
            return 
        self.accept()
    
    @property
    def id_plane(self):
        result = self.__id_plane_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @id_plane.setter
    def id_plane(self, value):
        self.__id_plane_edt.setText(value)
    
    @property
    def id_dairport(self):
        result = self.__id_dairport_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @id_dairport.setter
    def id_dairport(self, value):
        self.__id_dairport_edt.setText(value)
    
    @property
    def id_aairport(self):
        result = self.__id_aairport_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @id_aairport.setter
    def id_aairport(self, value):
        self.__id_aairport_edt.setText(value)
    
    @property
    def ftime(self):
        result = self.__ftime_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @ftime.setter
    def ftime(self, value):
        self.__ftime_edt.setText(value)
    
    @property
    def duration(self):
        result = self.__duration_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @duration.setter
    def duration(self, value):
        self.__duration_edt.setText(value)
    
    @property
    def bprice(self):
        result = self.__bprice_edt.text().strip()
        if result == '':
            return '0.00'
        else:
            return result
    
    @bprice.setter
    def bprice(self, value):
        self.__bprice_edt.setText(value)
    
    def get(self, data):
        data.planeid = self.id_plane
        data.departureairportid = self.id_dairport
        data.arrivalairportid = self.id_aairport
        data.flighttime = self.ftime
        data.duration = self.duration
        data.baseticketprice = self.bprice
    
    def put(self, data):
        self.id_plane = data.planeid
        self.id_dairport = data.departureairportid
        self.id_aairport = data.arrivalairportid
        self.ftime = data.flighttime
        self.duration = data.duration
        self.bprice = data.baseticketprice
