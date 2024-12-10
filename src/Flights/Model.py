from PyQt5.QtSql import QSqlQueryModel


SELECT = '''
    SELECT FlightID, PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice
    FROM Flight;
'''


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fresh()
    
    def fresh(self):
        self.setQuery(SELECT)
