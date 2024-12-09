from PyQt5.QtWidgets import QMenuBar, QActionGroup
from PyQt5.QtCore import pyqtSlot, pyqtSignal


class MainMenu(QMenuBar):
    
    airline_mode_request = pyqtSignal()
    airport_mode_request = pyqtSignal()
    flight_mode_request = pyqtSignal()
    plane_mode_request = pyqtSignal()
    ticket_mode_request = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        airline_menu = self.addMenu('Авиакомпания')
        self.__airline_menu_action = airline_menu.menuAction()
        self.__add_airline = airline_menu.addAction('Добавить...')
        self.__edit_airline = airline_menu.addAction('Редактировать...')
        self.__delete_airline = airline_menu.addAction('Удалить')
        
        airport_menu = self.addMenu('Аэропорт')
        self.__airport_menu_action = airport_menu.menuAction()
        self.__add_airport = airport_menu.addAction('Добавить...')
        self.__edit_airport = airport_menu.addAction('Редактировать...')
        self.__delete_airport = airport_menu.addAction('Удалить')
        
        flight_menu  = self.addMenu('Рейс')
        self.__flight_menu_action = flight_menu.menuAction()
        self.__add_flight = flight_menu.addAction('Добавить...')
        self.__edit_flight = flight_menu.addAction('Редактировать...')
        self.__delete_flight = flight_menu.addAction('Удалить')
        
        plane_menu = self.addMenu('Самолет')
        self.__plane_menu_action = plane_menu.menuAction()
        self.__add_plane = plane_menu.addAction('Добавить...')
        self.__edit_plane = plane_menu.addAction('Редактировать...')
        self.__delete_plane = plane_menu.addAction('Удалить')
        
        ticket_menu = self.addMenu('Билет')
        self.__ticket_menu_action = ticket_menu.menuAction()
        self.__add_ticket = ticket_menu.addAction('Добавить...')
        self.__edit_ticket = ticket_menu.addAction('Редактировать...')
        self.__delete_ticket = ticket_menu.addAction('Удалить')
        
        mode_menu = mnu = self.addMenu('Режимы')
        mode_action_group = ag = QActionGroup(self)
        
        self.__airline_mode_action = act = mnu.addAction('Авиакомпании')
        act.setCheckable(True)
        act.toggled.connect(self.toggle_airline_mode)
        ag.addAction(act)
        
        self.__airport_mode_action = act = mnu.addAction('Аэропорты')
        act.setCheckable(True)
        act.toggled.connect(self.toggle_airport_mode)
        ag.addAction(act)
        
        self.__flight_mode_action = act = mnu.addAction('Рейсы')
        act.setCheckable(True)
        act.toggled.connect(self.toggle_flight_mode)
        ag.addAction(act)
        
        self.__plane_mode_action = act = mnu.addAction('Самолеты')
        act.setCheckable(True)
        act.toggled.connect(self.toggle_plane_mode)
        ag.addAction(act)
        
        self.__ticket_mode_action = act = mnu.addAction('Билеты')
        act.setCheckable(True)
        act.toggled.connect(self.toggle_ticket_mode)
        ag.addAction(act)
        
        help_menu = self.addMenu('Справка')
        self.__about = help_menu.addAction('О программе...')
        self.__about_qt = help_menu.addAction('О библиотеке Qt...')
        
        self.toggle_airline_mode(False)
        self.toggle_airport_mode(False)
        self.toggle_flight_mode(False)
        self.toggle_plane_mode(False)
        self.toggle_ticket_mode(False)
    
    @pyqtSlot(bool)
    def toggle_airline_mode(self, enable):
        print(f'Airline={enable}')
        if not enable:
            self.__add_airline.setEnabled(False)
            self.__edit_airline.setEnabled(False)
            self.__delete_airline.setEnabled(False)
            self.__airline_menu_action.setEnabled(False)
            self.__airline_menu_action.setVisible(False)
        else:
            self.airline_mode_request.emit()
    
    @pyqtSlot(bool)
    def toggle_airport_mode(self, enable):
        print(f'Airport={enable}')
        if not enable:
            self.__add_airport.setEnabled(False)
            self.__edit_airport.setEnabled(False)
            self.__delete_airport.setEnabled(False)
            self.__airport_menu_action.setEnabled(False)
            self.__airport_menu_action.setVisible(False)
        else:
            self.airport_mode_request.emit()
    
    @pyqtSlot(bool)
    def toggle_flight_mode(self, enable):
        print(f'Flight={enable}')
        if not enable:
            self.__add_flight.setEnabled(False)
            self.__edit_flight.setEnabled(False)
            self.__delete_flight.setEnabled(False)
            self.__flight_menu_action.setEnabled(False)
            self.__flight_menu_action.setVisible(False)
        else:
            self.flight_mode_request.emit()
    
    @pyqtSlot(bool)
    def toggle_plane_mode(self, enable):
        print(f'Plane={enable}')
        if not enable:
            self.__add_plane.setEnabled(False)
            self.__edit_plane.setEnabled(False)
            self.__delete_plane.setEnabled(False)
            self.__plane_menu_action.setEnabled(False)
            self.__plane_menu_action.setVisible(False)
        else:
            self.plane_mode_request.emit()
    
    @pyqtSlot(bool)
    def toggle_ticket_mode(self, enable):
        print(f'Ticket={enable}')
        if not enable:
            self.__add_ticket.setEnabled(False)
            self.__edit_ticket.setEnabled(False)
            self.__delete_ticket.setEnabled(False)
            self.__ticket_menu_action.setEnabled(False)
            self.__ticket_menu_action.setVisible(False)
        else:
            self.ticket_mode_request.emit()
    
    @property
    def about(self):
        return self.__about
    
    @property
    def about_qt(self):
        return self.__about_qt
    
    def set_mode_airline(self, widget):
        self.__add_airline.triggered.connect(widget.add)
        self.__edit_airline.triggered.connect(widget.update)
        self.__delete_airline.triggered.connect(widget.delete)
        
        self.__add_airline.setEnabled(True)
        self.__edit_airline.setEnabled(True)
        self.__delete_airline.setEnabled(True)
        self.__airline_menu_action.setEnabled(True)
        self.__airline_menu_action.setVisible(True)
    
    def set_mode_airport(self, widget):
        self.__add_airport.triggered.connect(widget.add)
        self.__edit_airport.triggered.connect(widget.update)
        self.__delete_airport.triggered.connect(widget.delete)
        
        self.__add_airport.setEnabled(True)
        self.__edit_airport.setEnabled(True)
        self.__delete_airport.setEnabled(True)
        self.__airport_menu_action.setEnabled(True)
        self.__airport_menu_action.setVisible(True)
    
    def set_mode_flight(self, widget):
        self.__add_flight.triggered.connect(widget.add)
        self.__edit_flight.triggered.connect(widget.update)
        self.__delete_flight.triggered.connect(widget.delete)
        
        self.__add_flight.setEnabled(True)
        self.__edit_flight.setEnabled(True)
        self.__delete_flight.setEnabled(True)
        self.__flight_menu_action.setEnabled(True)
        self.__flight_menu_action.setVisible(True)
    
    def set_mode_plane(self, widget):
        self.__add_plane.triggered.connect(widget.add)
        self.__edit_plane.triggered.connect(widget.update)
        self.__delete_plane.triggered.connect(widget.delete)
        
        self.__add_plane.setEnabled(True)
        self.__edit_plane.setEnabled(True)
        self.__delete_plane.setEnabled(True)
        self.__plane_menu_action.setEnabled(True)
        self.__plane_menu_action.setVisible(True)
    
    def set_mode_ticket(self, widget):
        self.__add_ticket.triggered.connect(widget.add)
        self.__edit_ticket.triggered.connect(widget.update)
        self.__delete_ticket.triggered.connect(widget.delete)
        
        self.__add_ticket.setEnabled(True)
        self.__edit_ticket.setEnabled(True)
        self.__delete_ticket.setEnabled(True)
        self.__ticket_menu_action.setEnabled(True)
        self.__ticket_menu_action.setVisible(True)
