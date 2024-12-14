START TRANSACTION;

/*----------------------------------------------------------------------------------------------------------*/

INSERT INTO airport ( airportname, city )
VALUES ( 'Аэропорт имени Б. Н. Кустодиева', 'Астрахань' );

INSERT INTO airport ( airportname, city )
VALUES ( 'Кневичи', 'Владивосток' );

INSERT INTO airport ( airportname, city )
VALUES ( 'Северный', 'Грозный' );

INSERT INTO airport ( airportname, city )
VALUES ( 'Жуковский', 'Москва' );

INSERT INTO airport ( airportname, city )
VALUES ( 'Аэропорт имени Габдуллы Тукая', 'Казань' );

INSERT INTO airport ( airportname, city )
VALUES ( 'Внуково', 'Москва' );

INSERT INTO airport ( airportname, city )
VALUES ( 'Домодедово', 'Москва' );

INSERT INTO airport ( airportname, city )
VALUES ( 'Шереметьево', 'Москва' );

INSERT INTO airport ( airportname, city )
VALUES ( 'Стригино', 'Нижний Новгород' );

INSERT INTO airport ( airportname, city )
VALUES ( 'Адлер', 'Сочи' );

/*----------------------------------------------------------------------------------------------------------*/

COMMIT TRANSACTION;