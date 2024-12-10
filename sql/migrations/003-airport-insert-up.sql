START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

INSERT INTO Airport ( AirportName, City )
VALUES ( 'Аэропорт имени Б. Н. Кустодиева', 'Астрахань' );

INSERT INTO Airport ( AirportName, City )
VALUES ( 'Кневичи', 'Владивосток' );

INSERT INTO Airport ( AirportName, City )
VALUES ( 'Северный', 'Грозный' );

INSERT INTO Airport ( AirportName, City )
VALUES ( 'Жуковский', 'Москва' );

INSERT INTO Airport ( AirportName, City )
VALUES ( 'Аэропорт имени Габдуллы Тукая', 'Казань' );

INSERT INTO Airport ( AirportName, City )
VALUES ( 'Внуково', 'Москва' );

INSERT INTO Airport ( AirportName, City )
VALUES ( 'Домодедово', 'Москва' );

INSERT INTO Airport ( AirportName, City )
VALUES ( 'Шереметьево', 'Москва' );

INSERT INTO Airport ( AirportName, City )
VALUES ( 'Стригино', 'Нижний Новгород' );

INSERT INTO Airport ( AirportName, City )
VALUES ( 'Адлер', 'Сочи' );

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;