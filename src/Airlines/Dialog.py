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
        
        title = QApplication.translate('Airline.Dialog', 'Airline')
        self.setWindowTitle(title)
        
        title = QApplication.translate('Airline.Dialog', 'Airline Name')
        name_lbl = QLabel(title, parent=self)
        self.__name_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Airline.Dialog', 'IATA Code')
        code_lbl = QLabel(title, parent=self)
        self.__code_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Airline.Dialog', 'OK')
        ok_btn = QPushButton(title, parent=self)
        title = QApplication.translate('Airline.Dialog', 'Cancel')
        cancel_btn = QPushButton(title, parent=self)
        
        lay = QVBoxLayout(self)
        
        lay_name = QVBoxLayout()
        lay_name.setSpacing(0)
        lay_name.addWidget(name_lbl)
        lay_name.addWidget(self.__name_edt)
        lay.addLayout(lay_name)
        
        lay_code = QVBoxLayout()
        lay_code.setSpacing(0)
        lay_code.addWidget(code_lbl)
        lay_code.addWidget(self.__code_edt)
        lay.addLayout(lay_code)
        
        layH = QHBoxLayout()
        layH.addStretch()
        layH.addWidget(ok_btn)
        layH.addWidget(cancel_btn)
        lay.addLayout(layH)
        
        cancel_btn.clicked.connect(self.reject)
        ok_btn.clicked.connect(self.finish)
    
    @pyqtSlot()
    def finish(self):
        if self.name is None or self.code is None:
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
    def code(self):
        result = self.__code_edt.text().strip()
        if result == '':
            return None
        else:
            return result
    
    @code.setter
    def code(self, value):
        self.__code_edt.setText(value)
    
    def get(self, data):
        data.airlinename = self.name
        data.iatacode = self.code
    
    def put(self, data):
        self.name = data.airlinename
        self.code = data.iatacode
