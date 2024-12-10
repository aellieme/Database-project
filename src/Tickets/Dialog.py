from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QDialog # диалоговое окно
from PyQt5.QtWidgets import QLabel # надпись на окне
from PyQt5.QtWidgets import QLineEdit # текст из одной строчки
from PyQt5.QtWidgets import QComboBox # выбор YES/NO
from PyQt5.QtWidgets import QPushButton # кновка
from PyQt5.QtWidgets import QVBoxLayout # вертикальная разметка окна
from PyQt5.QtWidgets import QHBoxLayout # горизонтальная разметка окна

from PyQt5.Qt import QApplication

import db


class Dialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        title = QApplication.translate('Ticket.Dialog', 'Ticket')
        self.setWindowTitle(title)
        
        title = QApplication.translate('Ticket.Dialog', 'Flight ID')
        id_flight_lbl = QLabel(title, parent=self)
        self.__id_flight_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Ticket.Dialog', 'Passenger full name')
        name_lbl = QLabel(title, parent=self)
        self.__name_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Ticket.Dialog', 'Passport series and number')
        passport_lbl = QLabel(title, parent=self)
        self.__passport_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Ticket.Dialog', 'Seat number')
        seat_lbl = QLabel(title, parent=self)
        self.__seat_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Ticket.Dialog', 'Lunch on board')
        meal_lbl = QLabel(title, parent=self)
        self.__meal_edt = QComboBox(parent=self)
        self.__meal_edt.addItems(['NO', 'YES'])
        
        title = QApplication.translate('Ticket.Dialog', 'OK')
        ok_btn = QPushButton(title, parent=self)
        title = QApplication.translate('Ticket.Dialog', 'Cancel')
        cancel_btn = QPushButton(title, parent=self)
        
        lay = QVBoxLayout(self)
        
        lay_id_flight = QVBoxLayout()
        lay_id_flight.setSpacing(0)
        lay_id_flight.addWidget(id_flight_lbl)
        lay_id_flight.addWidget(self.__id_flight_edt)
        lay.addLayout(lay_id_flight)
        
        lay_name = QVBoxLayout()
        lay_name.setSpacing(0)
        lay_name.addWidget(name_lbl)
        lay_name.addWidget(self.__name_edt)
        lay.addLayout(lay_name)
        
        lay_passport = QVBoxLayout()
        lay_passport.setSpacing(0)
        lay_passport.addWidget(passport_lbl)
        lay_passport.addWidget(self.__passport_edt)
        lay.addLayout(lay_passport)
        
        lay_seat = QVBoxLayout()
        lay_seat.setSpacing(0)
        lay_seat.addWidget(seat_lbl)
        lay_seat.addWidget(self.__seat_edt)
        lay.addLayout(lay_seat)
        
        lay_meal = QVBoxLayout()
        lay_meal.setSpacing(0)
        lay_meal.addWidget(meal_lbl)
        lay_meal.addWidget(self.__meal_edt)
        lay.addLayout(lay_meal)
        
        layH = QHBoxLayout()
        layH.addStretch()
        layH.addWidget(ok_btn)
        layH.addWidget(cancel_btn)
        lay.addLayout(layH)
        
        cancel_btn.clicked.connect(self.reject)
        ok_btn.clicked.connect(self.finish)
    
    @pyqtSlot()
    def finish(self):
        print(self.meal)
        if self.id_flight is None or self.name is None or self.passport is None or self.seat is None:
            return 
        self.accept()
    
    @property
    def id_flight(self):
        result = self.__id_flight_edt.text().strip()
        if result and result.isdigit() and db.Flight(flightid=int(result)).exist_key():
            return int(result)
        return None
    
    @id_flight.setter
    def id_flight(self, value):
        self.__id_flight_edt.setText(str(value))
    
    @property
    def name(self):
        result = self.__name_edt.text().strip()
        return result if result else None
    
    @name.setter
    def name(self, value):
        self.__name_edt.setText(value)
    
    @property
    def passport(self):
        result = self.__passport_edt.text().strip()
        return result if result else None
    
    @passport.setter
    def passport(self, value):
        self.__passport_edt.setText(value)
    
    @property
    def seat(self):
        result = self.__seat_edt.text().strip()
        return result if result else None
    
    @seat.setter
    def seat(self, value):
        self.__seat_edt.setText(value)
    
    @property
    def meal(self):
        result = self.__meal_edt.currentText().strip()
        return result
    
    @meal.setter
    def meal(self, value):
        print(value)
        if value == 'YES':
            self.__meal_edt.setItemText(0, 'YES')
            self.__meal_edt.setItemText(1, 'NO')
    
    def get(self, data):
        data.flightid = self.id_flight
        data.fullname = self.name
        data.passportnumber = self.passport
        data.seatnumber = self.seat
        data.meal = self.meal
    
    def put(self, data):
        self.id_flight = data.flightid
        self.name = data.fullname
        self.passport = data.passportnumber
        self.seat = data.seatnumber
        self.meal = data.meal
