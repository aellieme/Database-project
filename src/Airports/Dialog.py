from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QDialog # диалоговое окно
from PyQt5.QtWidgets import QLabel # надпись на окне
from PyQt5.QtWidgets import QLineEdit # текст из одной строчки
from PyQt5.QtWidgets import QPushButton # кновка
from PyQt5.QtWidgets import QVBoxLayout # вертикальная разметка окна
from PyQt5.QtWidgets import QHBoxLayout # горизонтальная разметка окна


SELECT_ONE = '''
    SELECT AirportName, City
    FROM Airport
    WHERE AirportID = %s;
'''


class Dialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Аэропорт')
        
        name_lbl = QLabel('Название аэропорта', parent=self)
        self.__name_edt = QLineEdit(parent=self)
        
        city_lbl = QLabel('Город', parent=self)
        self.__city_edt = QLineEdit(parent=self)
        
        ok_btn = QPushButton('ОК', parent=self)
        cancel_btn = QPushButton('Отмена', parent=self)
        
        lay = QVBoxLayout(self)
        
        lay_name = QVBoxLayout()
        lay_name.setSpacing(0)
        lay_name.addWidget(name_lbl)
        lay_name.addWidget(self.__name_edt)
        lay.addLayout(lay_name)
        
        lay_city = QVBoxLayout()
        lay_city.setSpacing(0)
        lay_city.addWidget(city_lbl)
        lay_city.addWidget(self.__city_edt)
        lay.addLayout(lay_city)
        
        layH = QHBoxLayout()
        layH.addStretch()
        layH.addWidget(ok_btn)
        layH.addWidget(cancel_btn)
        lay.addLayout(layH)
        
        cancel_btn.clicked.connect(self.reject)
        ok_btn.clicked.connect(self.finish)
    
    @pyqtSlot()
    def finish(self):
        if self.name is None or self.city is None:
            return 
        self.accept()
    
    @property
    def name(self):
        result = self.__name_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @name.setter
    def name(self, value):
        self.__name_edt.setText(value)
    
    @property
    def city(self):
        result = self.__city_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @city.setter
    def city(self, value):
        self.__city_edt.setText(value)
    
    def get(self, data):
        data.airportname = self.name
        data.city = self.city
    
    def put(self, data):
        self.name = data.airportname
        self.city = data.city
