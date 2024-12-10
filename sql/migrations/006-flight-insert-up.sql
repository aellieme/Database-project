START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 20, 1, 3, '2024-10-30 15:50:00', '8 hours 10 minutes', 14601 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 5, 1, 10, '2024-11-29 07:00:00', '1 hour 55 minutes', 10073 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 14, 2, 4, '2024-11-10 10:20:00', '8 hours 40 minutes', 49189 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 18, 2, 9, '2024-09-12 00:30:00', '12 hours 20 minutes', 62056 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 7, 3, 1, '2024-12-15 15:40:00', '8 hours 5 minutes', 14719 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 1, 3, 5, '2024-09-23 16:15:00', '2 hours 40 minutes', 9241 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 2, 4, 9, '2024-10-07 07:35:00', '1 hour 30 minutes', 7325 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 9, 4, 2, '2024-11-19 17:00:00', '8 hours 20 minutes', 27578 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 21, 5, 8, '2024-10-18 00:05:00', '1 hour 40 minutes', 3509 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 6, 5, 1, '2024-10-08 20:20:00', '2 hours 20 minutes', 6367 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 11, 6, 1, '2024-11-06 09:05:00', '2 hours 45 minutes', 6779 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 19, 6, 10, '2024-09-30 06:00:00', '3 hours 30 minutes', 5078 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 13, 7, 3, '2024-10-01 12:00:00', '3 hours 5 minutes', 7469 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 3, 7, 5, '2024-09-08 08:30:00', '1 hour 40 minutes', 3909 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 10, 8, 9, '2024-12-21 09:25:00', '1 hour 25 minutes', 5786 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 4, 8, 10, '2024-09-16 04:15:00', '3 hours 30 minutes', 8680 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 12, 9, 5, '2024-11-14 18:10:00', '1 hour 0 minutes', 10261 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 8, 9, 10, '2024-12-05 17:05:00', '3 hours 35 minutes', 12183 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 15, 10, 1, '2024-10-13 01:30:00', '1 hour 45 minutes', 13603 );

INSERT INTO Flight ( PlaneID, DepartureAirportID, ArrivalAirportID, FlightTime, Duration, BaseTicketPrice )
VALUES ( 17, 10, 4, '2024-09-18 02:40:00', '3 hours 45 minutes', 4313 );

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;