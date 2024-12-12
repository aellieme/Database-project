from PyQt5.QtWidgets import QMenuBar, QActionGroup, QApplication
from PyQt5.QtCore import pyqtSlot, pyqtSignal


class MainMenu(QMenuBar):
    
    airline_mode_request = pyqtSignal()
    airport_mode_request = pyqtSignal()
    flight_mode_request = pyqtSignal()
    plane_mode_request = pyqtSignal()
    ticket_mode_request = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setMinimumHeight(30)
        font = self.font()
        font.setPointSize(14)
        self.setFont(font)
        
        title = QApplication.translate('MainMenu', 'Airline')
        airline_menu = self.addMenu(title)
        self.__airline_menu_action = airline_menu.menuAction()
        title = QApplication.translate('MainMenu.Airline', 'Add...')
        self.__add_airline = airline_menu.addAction(title)
        self.__add_airline.setFont(font)
        title = QApplication.translate('MainMenu.Airline', 'Edit...')
        self.__edit_airline = airline_menu.addAction(title)
        self.__edit_airline.setFont(font)
        title = QApplication.translate('MainMenu.Airline', 'Delete')
        self.__delete_airline = airline_menu.addAction(title)
        self.__delete_airline.setFont(font)
        title = QApplication.translate('MainMenu.Airline', 'Clear table')
        self.__clear_airline = airline_menu.addAction(title)
        self.__clear_airline.setFont(font)
        
        title = QApplication.translate('MainMenu', 'Airport')
        airport_menu = self.addMenu(title)
        self.__airport_menu_action = airport_menu.menuAction()
        title = QApplication.translate('MainMenu.Airport', 'Add...')
        self.__add_airport = airport_menu.addAction(title)
        self.__add_airport.setFont(font)
        title = QApplication.translate('MainMenu.Airport', 'Edit...')
        self.__edit_airport = airport_menu.addAction(title)
        self.__edit_airport.setFont(font)
        title = QApplication.translate('MainMenu.Airport', 'Delete')
        self.__delete_airport = airport_menu.addAction(title)
        self.__delete_airport.setFont(font)
        title = QApplication.translate('MainMenu.Airport', 'Clear table')
        self.__clear_airport = airport_menu.addAction(title)
        self.__clear_airport.setFont(font)
        
        title = QApplication.translate('MainMenu', 'Flight')
        flight_menu  = self.addMenu(title)
        self.__flight_menu_action = flight_menu.menuAction()
        title = QApplication.translate('MainMenu.Flight', 'Add...')
        self.__add_flight = flight_menu.addAction(title)
        self.__add_flight.setFont(font)
        title = QApplication.translate('MainMenu.Flight', 'Edit...')
        self.__edit_flight = flight_menu.addAction(title)
        self.__edit_flight.setFont(font)
        title = QApplication.translate('MainMenu.Flight', 'Delete')
        self.__delete_flight = flight_menu.addAction(title)
        self.__delete_flight.setFont(font)
        title = QApplication.translate('MainMenu.Flight', 'Clear table')
        self.__clear_flight = flight_menu.addAction(title)
        self.__clear_flight.setFont(font)
        
        title = QApplication.translate('MainMenu', 'Plane')
        plane_menu = self.addMenu(title)
        self.__plane_menu_action = plane_menu.menuAction()
        title = QApplication.translate('MainMenu.Plane', 'Add...')
        self.__add_plane = plane_menu.addAction(title)
        self.__add_plane.setFont(font)
        title = QApplication.translate('MainMenu.Plane', 'Edit...')
        self.__edit_plane = plane_menu.addAction(title)
        self.__edit_plane.setFont(font)
        title = QApplication.translate('MainMenu.Plane', 'Delete')
        self.__delete_plane = plane_menu.addAction(title)
        self.__delete_plane.setFont(font)
        title = QApplication.translate('MainMenu.Plane', 'Clear table')
        self.__clear_plane = plane_menu.addAction(title)
        self.__clear_plane.setFont(font)
        
        title = QApplication.translate('MainMenu', 'Ticket')
        ticket_menu = self.addMenu(title)
        self.__ticket_menu_action = ticket_menu.menuAction()
        title = QApplication.translate('MainMenu.Ticket', 'Add...')
        self.__add_ticket = ticket_menu.addAction(title)
        self.__add_ticket.setFont(font)
        title = QApplication.translate('MainMenu.Ticket', 'Edit...')
        self.__edit_ticket = ticket_menu.addAction(title)
        self.__edit_ticket.setFont(font)
        title = QApplication.translate('MainMenu.Ticket', 'Delete')
        self.__delete_ticket = ticket_menu.addAction(title)
        self.__delete_ticket.setFont(font)
        title = QApplication.translate('MainMenu.Ticket', 'Clear table')
        self.__clear_ticket = ticket_menu.addAction(title)
        self.__clear_ticket.setFont(font)
        
        title = QApplication.translate('MainMenu', 'Modes')
        mode_menu = mnu = self.addMenu(title)
        mode_action_group = ag = QActionGroup(self)
        
        title = QApplication.translate('MainMenu.Modes', 'Airlines')
        self.__airline_mode_action = act = mnu.addAction(title)
        act.setFont(font)
        act.setCheckable(True)
        act.toggled.connect(self.toggle_airline_mode)
        ag.addAction(act)
        
        title = QApplication.translate('MainMenu.Modes', 'Airports')
        self.__airport_mode_action = act = mnu.addAction(title)
        act.setFont(font)
        act.setCheckable(True)
        act.toggled.connect(self.toggle_airport_mode)
        ag.addAction(act)
        
        title = QApplication.translate('MainMenu.Modes', 'Flights')
        self.__flight_mode_action = act = mnu.addAction(title)
        act.setFont(font)
        act.setCheckable(True)
        act.toggled.connect(self.toggle_flight_mode)
        ag.addAction(act)
        
        title = QApplication.translate('MainMenu.Modes', 'Planes')
        self.__plane_mode_action = act = mnu.addAction(title)
        act.setFont(font)
        act.setCheckable(True)
        act.toggled.connect(self.toggle_plane_mode)
        ag.addAction(act)
        
        title = QApplication.translate('MainMenu.Modes', 'Tickets')
        self.__ticket_mode_action = act = mnu.addAction(title)
        act.setFont(font)
        act.setCheckable(True)
        act.toggled.connect(self.toggle_ticket_mode)
        ag.addAction(act)
        
        title = QApplication.translate('MainMenu', 'Help')
        help_menu = self.addMenu(title)
        title = QApplication.translate('MainMenu.Help', 'About...')
        self.__about = help_menu.addAction(title)
        self.__about.setFont(font)
        title = QApplication.translate('MainMenu.Help', 'About Qt...')
        self.__about_qt = help_menu.addAction(title)
        self.about_qt.setFont(font)
        
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
            self.__clear_airline.setEnabled(False)
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
            self.__clear_airport.setEnabled(False)
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
            self.__clear_flight.setEnabled(False)
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
            self.__clear_plane.setEnabled(False)
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
            self.__clear_ticket.setEnabled(False)
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
        self.__clear_airline.triggered.connect(widget.truncate)
        
        self.__add_airline.setEnabled(True)
        self.__edit_airline.setEnabled(True)
        self.__delete_airline.setEnabled(True)
        self.__clear_airline.setEnabled(True)
        self.__airline_menu_action.setEnabled(True)
        self.__airline_menu_action.setVisible(True)
    
    def set_mode_airport(self, widget):
        self.__add_airport.triggered.connect(widget.add)
        self.__edit_airport.triggered.connect(widget.update)
        self.__delete_airport.triggered.connect(widget.delete)
        self.__clear_airport.triggered.connect(widget.truncate)
        
        self.__add_airport.setEnabled(True)
        self.__edit_airport.setEnabled(True)
        self.__delete_airport.setEnabled(True)
        self.__clear_airport.setEnabled(True)
        self.__airport_menu_action.setEnabled(True)
        self.__airport_menu_action.setVisible(True)
    
    def set_mode_flight(self, widget):
        self.__add_flight.triggered.connect(widget.add)
        self.__edit_flight.triggered.connect(widget.update)
        self.__delete_flight.triggered.connect(widget.delete)
        self.__clear_flight.triggered.connect(widget.truncate)
        
        self.__add_flight.setEnabled(True)
        self.__edit_flight.setEnabled(True)
        self.__delete_flight.setEnabled(True)
        self.__clear_flight.setEnabled(True)
        self.__flight_menu_action.setEnabled(True)
        self.__flight_menu_action.setVisible(True)
    
    def set_mode_plane(self, widget):
        self.__add_plane.triggered.connect(widget.add)
        self.__edit_plane.triggered.connect(widget.update)
        self.__delete_plane.triggered.connect(widget.delete)
        self.__clear_plane.triggered.connect(widget.truncate)
        
        self.__add_plane.setEnabled(True)
        self.__edit_plane.setEnabled(True)
        self.__delete_plane.setEnabled(True)
        self.__clear_plane.setEnabled(True)
        self.__plane_menu_action.setEnabled(True)
        self.__plane_menu_action.setVisible(True)
    
    def set_mode_ticket(self, widget):
        self.__add_ticket.triggered.connect(widget.add)
        self.__edit_ticket.triggered.connect(widget.update)
        self.__delete_ticket.triggered.connect(widget.delete)
        self.__clear_ticket.triggered.connect(widget.truncate)
        
        self.__add_ticket.setEnabled(True)
        self.__edit_ticket.setEnabled(True)
        self.__delete_ticket.setEnabled(True)
        self.__clear_ticket.setEnabled(True)
        self.__ticket_menu_action.setEnabled(True)
        self.__ticket_menu_action.setVisible(True)
