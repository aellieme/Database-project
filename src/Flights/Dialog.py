from PyQt5.QtCore import pyqtSlot, QTime, QDateTime

from PyQt5.QtWidgets import QDialog # диалоговое окно
from PyQt5.QtWidgets import QLabel # надпись на окне
from PyQt5.QtWidgets import QLineEdit # текст из одной строчки
from PyQt5.QtWidgets import QDateTimeEdit # ввод даты и времени
from PyQt5.QtWidgets import QTimeEdit # ввод времени
from PyQt5.QtWidgets import QPushButton # кновка
from PyQt5.QtWidgets import QVBoxLayout # вертикальная разметка окна
from PyQt5.QtWidgets import QHBoxLayout # горизонтальная разметка окна

from PyQt5.Qt import QApplication

import db
from .constraints import constraint_check

from datetime import datetime, timedelta


def convert_to_datetime(qdatetime: QDateTime) -> datetime:
    return datetime(qdatetime.date().year(), qdatetime.date().month(), qdatetime.date().day(), qdatetime.time().hour(), qdatetime.time().minute())


def convert_to_timedelta(time: QTime) -> timedelta:
    return timedelta(hours=time.hour(), minutes=time.minute())


def convert_to_qdatetime(dt: datetime) -> QDateTime:
    return QDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute)


class Dialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        title = QApplication.translate('Flight.Dialog', 'Flight')
        self.setWindowTitle(title)
        
        title = QApplication.translate('Flight.Dialog', 'Plane ID')
        id_plane_lbl = QLabel(title, parent=self)
        self.__id_plane_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Flight.Dialog', 'Departure Airport ID')
        id_dairport_lbl = QLabel(title, parent=self)
        self.__id_dairport_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Flight.Dialog', 'Arrival Airport ID')
        id_aairport_lbl = QLabel(title, parent=self)
        self.__id_aairport_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Flight.Dialog', 'Departure date and time')
        ftime_lbl = QLabel(title, parent=self)
        self.__ftime_edt = QDateTimeEdit(parent=self)
        dt = QDateTime.currentDateTime()
        self.__ftime_edt.setDateTime(dt)
        
        title = QApplication.translate('Flight.Dialog', 'Flight duration')
        duration_lbl = QLabel(title, parent=self)
        self.__duration_edt = QTimeEdit()
        
        title = QApplication.translate('Flight.Dialog', 'Base Ticket Price')
        bprice_lbl = QLabel(title, parent=self)
        self.__bprice_edt = QLineEdit(parent=self)
        
        title = QApplication.translate('Flight.Dialog', 'OK')
        ok_btn = QPushButton(title, parent=self)
        title = QApplication.translate('Flight.Dialog', 'Cancel')
        cancel_btn = QPushButton(title, parent=self)
        
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
        if not constraint_check(
            ('PlaneID', 'DepartureAirportID', 'ArrivalAirportID', 'FlightTime', 'Duration', 'BaseTicketPrice'),
            (self.id_plane, self.id_dairport, self.id_aairport, self.ftime, self.duration, self.bprice)
            ):
            return 
        self.accept()
    
    @property
    def id_plane(self):
        result = self.__id_plane_edt.text().strip()
        if result and result.isdigit() and db.Plane(planeid=int(result)).exist_key():
            return int(result)
        return None
    
    @id_plane.setter
    def id_plane(self, value):
        self.__id_plane_edt.setText(str(value))
    
    @property
    def id_dairport(self):
        result = self.__id_dairport_edt.text().strip()
        if result and result.isdigit() and db.Airport(airportid=int(result)).exist_key():
            return int(result)
        return None
    
    @id_dairport.setter
    def id_dairport(self, value):
        self.__id_dairport_edt.setText(str(value))
    
    @property
    def id_aairport(self):
        result = self.__id_aairport_edt.text().strip()
        if result and result.isdigit() and db.Airport(airportid=int(result)).exist_key():
            return int(result)
        return None
    
    @id_aairport.setter
    def id_aairport(self, value):
        self.__id_aairport_edt.setText(str(value))
    
    @property
    def ftime(self):
        result = self.__ftime_edt.dateTime()
        return result
    
    @ftime.setter
    def ftime(self, value):
        self.__ftime_edt.setDateTime(value)
    
    @property
    def duration(self):
        result = self.__duration_edt.time()
        return result
    
    @duration.setter
    def duration(self, value):
        self.__duration_edt.setTime(value)
    
    @property
    def bprice(self):
        result = self.__bprice_edt.text().strip()
        if result and result.isdigit():
            return int(result)
        return None
    
    @bprice.setter
    def bprice(self, value):
        self.__bprice_edt.setText(str(value))
    
    def get(self, data):
        data.planeid = self.id_plane
        data.departureairportid = self.id_dairport
        data.arrivalairportid = self.id_aairport
        data.flighttime = convert_to_datetime(self.ftime)
        data.duration = convert_to_timedelta(self.duration)
        data.baseticketprice = self.bprice
    
    def put(self, data):
        self.id_plane = data.planeid
        self.id_dairport = data.departureairportid
        self.id_aairport = data.arrivalairportid
        self.ftime = convert_to_qdatetime(data.flighttime)
        self.duration = QTime(0, 0).addSecs(int(data.duration.total_seconds()))
        self.bprice = data.baseticketprice
