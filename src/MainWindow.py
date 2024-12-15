from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont

from Application import Application as app
from Welcome import Welcome
from MainMenu import MainMenu
import Airlines, Airports, Flights, Planes, Tickets, DeleteDB
import db


class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)
        
        v = Welcome()
        self.setCentralWidget(v)
        
        main_menu.dropdb.triggered.connect(self.dropdb)
        
        main_menu.about.triggered.connect(self.about)
        main_menu.about_qt.triggered.connect(self.about_qt)
        
        main_menu.airline_mode_request.connect(self.airline_mode_on)
        main_menu.airport_mode_request.connect(self.airport_mode_on)
        main_menu.flight_mode_request.connect(self.flight_mode_on)
        main_menu.plane_mode_request.connect(self.plane_mode_on)
        main_menu.ticket_mode_request.connect(self.ticket_mode_on)
        
        main_menu.dropdb.triggered.connect(self.dropdb)
        
        self.font = QFont()
        self.font.setPixelSize(20)
    
    @pyqtSlot()
    def about(self):
        title = QApplication.translate('Main Window',
                                       'Database Management')
        text = QApplication.translate('MainWindow.Help',
                                      'Program for creating, deleting, managing\n'
                                      'and editing an AIRPORT database')
        mb = QMessageBox(QMessageBox.NoIcon, title, text, QMessageBox.Ok, self)
        mb.setFont(self.font)
        mb.exec_()
    
    @pyqtSlot()
    def about_qt(self):
        title = QApplication.translate('Main Window',
                                       'Database Management')
        QMessageBox.aboutQt(self, title)
    
    @pyqtSlot()
    def dropdb(self):
        dia = DeleteDB.Dialog(parent=self)
        if dia.exec():
            data = db.Database()
            dia.get(data)
            ok = data.drop()
            if ok:
                ans = QMessageBox.question(self, 'База данных', 'Вы уверены?')
                if ans == QMessageBox.Yes:
                    mb = QMessageBox(QMessageBox.Information, 'ВНИМАНИЕ',
                                     'База данных удалена.\n\n'
                                     'После закрытия этого окна произойдёт выход из приложения.\n\n'
                                     'База данных снова будет создана при следующем запуске.',
                                     QMessageBox.Ok, self)
                    mb.setFont(self.font)
                    if mb.exec():
                        app.quit()
    
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
        self.setCentralWidget(v.widget)
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
