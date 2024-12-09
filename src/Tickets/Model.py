from PyQt5.QtSql import QSqlQueryModel
import psycopg2
import settings as st


SELECT = '''
    SELECT TicketID, FlightID, FullName, PassportNumber, SeatNumber, Meal, Price
    FROM Ticket;
'''


#INSERT = '''
#    INSERT INTO Ticket ( FlightID, FullName, PassportNumber, SeatNumber, Meal )
#    VALUES ( %s, %s, %s, %s, %s );
#'''


UPDATE = '''
    UPDATE Flight SET
        FlightID = %s,
        FullName = %s,
        PassportNumber = %s,
        SeatNumber = %s,
        Meal = %s
    WHERE FlightID = %s;
'''


DELETE = '''
    DELETE FROM Flight
    WHERE FlightID = %s;
'''


class Model(QSqlQueryModel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fresh()
    
    def fresh(self):
        self.setQuery(SELECT)
    
#    def add(self, id_flight, name, passport, seat, meal):
#        conn = psycopg2.connect(**st.db_params)
#        cursor = conn.cursor()
#        data = (id_flight, name, passport, seat, meal)
#        cursor.execute(INSERT, data)
#        conn.commit()
#        conn.close()
#        self.fresh()
    
    def update(self, id_ticket, id_flight, name, passport, seat, meal):
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        data = (id_flight, name, passport, seat, meal, id_ticket)
        cursor.execute(UPDATE, data)
        conn.commit()
        conn.close()
        self.fresh()
    
    def delete(self, id_ticket):
        conn = psycopg2.connect(**st.db_params)
        cursor = conn.cursor()
        data = (id_ticket,)
        cursor.execute(DELETE, data)
        conn.commit()
        conn.close()
        self.fresh()
