from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot, Qt
from MainMenu import MainMenu
import Airlines, Airports, Flights, Planes, Tickets


TEXT = '''
ХИХИК

ЭЛЯ ЖДУ...

ХИХИК
'''


class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)
        
        # Начальное сообщение на главном окне
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        
        lbl = QLabel(TEXT)
        lbl.setFont(font)
        lbl.setAlignment(Qt.AlignCenter)
        
        lay = QVBoxLayout()
        lay.addWidget(lbl)
        lay.setAlignment(Qt.AlignCenter)
        
        widget = QWidget()
        widget.setLayout(lay)
        self.setCentralWidget(widget)
        
        main_menu.about.triggered.connect(self.about)
        main_menu.about_qt.triggered.connect(self.about_qt)
        
        main_menu.airline_mode_request.connect(self.airline_mode_on)
        main_menu.airport_mode_request.connect(self.airport_mode_on)
        main_menu.flight_mode_request.connect(self.flight_mode_on)
        main_menu.plane_mode_request.connect(self.plane_mode_on)
        main_menu.ticket_mode_request.connect(self.ticket_mode_on)
    
    @pyqtSlot()
    def about(self):
        title = QApplication.translate('Main Window',
                                       'Database Management')
        text = QApplication.translate('MainWindow.Help',
                                      'Program for creating, deleting, managing\n'
                                      'and editing an AIRPORT database')
        QMessageBox.about(self, title, text)
    
    @pyqtSlot()
    def about_qt(self):
        title = QApplication.translate('Main Window',
                                       'Database Management')
        QMessageBox.aboutQt(self, title)
    
    @pyqtSlot()
    def airline_mode_on(self):
        old = self.centralWidget()
        v = Airlines.View(parent=self)
        self.setCentralWidget(v)
        self.menuBar().set_mode_airline(v)
        if old is not None:
            old.deleteLater()
    
    @pyqtSlot()
    def airport_mode_on(self):
        old = self.centralWidget()
        v = Airports.View(parent=self)
        self.setCentralWidget(v)
        self.menuBar().set_mode_airport(v)
        if old is not None:
            old.deleteLater()
    
    @pyqtSlot()
    def flight_mode_on(self):
        old = self.centralWidget()
        v = Flights.View(parent=self)
        self.setCentralWidget(v)
        self.menuBar().set_mode_flight(v)
        if old is not None:
            old.deleteLater()
    
    @pyqtSlot()
    def plane_mode_on(self):
        old = self.centralWidget()
        v = Planes.View(parent=self)
        self.setCentralWidget(v)
        self.menuBar().set_mode_plane(v)
        if old is not None:
            old.deleteLater()
    
    @pyqtSlot()
    def ticket_mode_on(self):
        old = self.centralWidget()
        v = Tickets.View(parent=self)
        self.setCentralWidget(v)
        self.menuBar().set_mode_ticket(v)
        if old is not None:
            old.deleteLater()
