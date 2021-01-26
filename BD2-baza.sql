
CREATE SCHEMA IF NOT EXISTS database_;

CREATE TABLE Office(
Officeid INT AUTO_INCREMENT PRIMARY KEY,
city VARCHAR(255) NOT NULL,
employees INT NOT NULL,
officecost INT NOT NULL
);
CREATE TABLE Factory( 
Factoryid INT AUTO_INCREMENT PRIMARY KEY, 
city VARCHAR(255) NOT NULL, 
employees INT NOT NULL,
factorycost INT NOT NULL
);
CREATE TABLE Employee( 
Employeeid INT AUTO_INCREMENT PRIMARY KEY, 
Officeid INT REFERENCES Office(Officeid), 
Factoryid INT REFERENCES Factory (Factoryid), 
salary INT NOT NULL,
job VARCHAR(255) NOT NULL,
first_name VARCHAR(255),
surname VARCHAR(255) 
);
CREATE TABLE Client_( 
Clientid INT AUTO_INCREMENT PRIMARY KEY, 
Employeeid INT REFERENCES Employee(Employeeid), 
clientname VARCHAR(255) NOT NULL, 
city VARCHAR(255) NOT NULL, 
client_address VARCHAR(255) NOT NULL
);

CREATE TABLE Payment(
Paymentid INT AUTO_INCREMENT PRIMARY KEY,  
Clientid INT REFERENCES Client_(Clientid),
total INT NOT NULL,
realised BOOLEAN NOT NULL
);

CREATE TABLE Order_(
Orderid INT AUTO_INCREMENT PRIMARY KEY,
Clientid INT REFERENCES Client_(Clientid),
Paymentid INT REFERENCES Payment(Paymentid),
ordertime DATETIME NOT NULL,
orderstatus VARCHAR(255) NOT NULL
);


CREATE TABLE Car( 
Carid INT AUTO_INCREMENT PRIMARY KEY,
Factoryid INT REFERENCES Factory(Factoryid),
Orderid INT REFERENCES Order_(Orderid),
real_status VARCHAR(255) NOT NULL,
order_status VARCHAR(255) NOT NULL,
cartype VARCHAR(255) NOT NULL,
colour VARCHAR(255) NOT NULL,
carmodel VARCHAR(255) NOT NULL,
interior VARCHAR(255) NOT NULL,
caryear INT NOT NULL
);

CREATE TABLE Part(
Partid INT AUTO_INCREMENT PRIMARY KEY,
partname VARCHAR(255) NOT NULL,
qty INT NOT NULL
);

CREATE TABLE Supplier(
Supplierid INT AUTO_INCREMENT PRIMARY KEY,
suppliername VARCHAR(255) NOT NULL
);

CREATE TABLE Part_Car(
Carid INT REFERENCES Car(Carid),
Partid INT REFERENCES Part(Partid) 
);

CREATE TABLE Supplier_Part(
Partid INT REFERENCES Part(Partid),
Supplierid INT REFERENCES Supplier(Supplierid),
price INT NOT NULL
);


CREATE TABLE Logs(
LogDate DATE NOT NULL,
Info VARCHAR(45) NOT NULL,
TableName VARCHAR(45) NOT NULL
);

CREATE TRIGGER Delete_Office
AFTER DELETE ON Office
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Office deleted','Office');

CREATE TRIGGER Change_Office
AFTER UPDATE ON Office
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Office changed','Office');

CREATE TRIGGER Delete_Factory
AFTER DELETE ON Factory
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Factory deleted','Factory');

CREATE TRIGGER Change_Factory
AFTER UPDATE ON Factory
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Factory changed','Factory');

CREATE TRIGGER Delete_Employee
AFTER DELETE ON Employee
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Employee deleted','Employee');

CREATE TRIGGER Change_Employee
AFTER UPDATE ON Employee
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Employee changed','Employee');

CREATE TRIGGER Delete_Client_
AFTER DELETE ON Client_
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Client deleted','Client_');

CREATE TRIGGER Change_Client_
AFTER UPDATE ON Client_
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Client changed','Client_');

CREATE TRIGGER Delete_Car
AFTER DELETE ON Car
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Car deleted','Car');

CREATE TRIGGER Change_Car
AFTER UPDATE ON Car
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Car changed','Car');

CREATE TRIGGER Delete_Part
AFTER DELETE ON Part
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Part deleted','Part');

CREATE TRIGGER Change_Part
AFTER UPDATE ON Part
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Part changed','Part');

CREATE TRIGGER Delete_Supplier
AFTER DELETE ON Supplier
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Supplier deleted','Supplier');

CREATE TRIGGER Change_Supplier
AFTER UPDATE ON Supplier
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Supplier changed','Supplier');

CREATE TRIGGER Delete_Order_
AFTER DELETE ON Order_
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Order deleted','Order_');

CREATE TRIGGER Change_Order_
AFTER UPDATE ON Order_
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Order changed','Order_');

CREATE TRIGGER Delete_Payment
AFTER DELETE ON Payment
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Payment deleted','Payment');

CREATE TRIGGER Change_Payment
AFTER UPDATE ON Payment
FOR EACH ROW
INSERT INTO Logs VALUES(SYSDATE,'Payment changed','Payment');

DELIMITER //

CREATE PROCEDURE GetAllEmployees()
BEGIN
	SELECT *  FROM Employee;
END //

CREATE PROCEDURE GetAllCars()
BEGIN
	SELECT *  FROM Car;
END //

CREATE PROCEDURE GetFactory()
BEGIN
	SELECT *  FROM Factory
    WHERE city = Wroclaw;
END //
DELIMITER ;

-- wprowadzenie danych
INSERT INTO Office(city, employees, officecost)
VALUES 
("Wrocław", 10, 15000),
("Warszawa", 5, 20000);

INSERT INTO Factory(city, employees, factorycost)
VALUES 
("Wrocław", 10, 15000);

INSERT INTO Employee(Officeid, Factoryid, salary, job, first_name, surname)
VALUES 
(1, null, 16000, "manager", "Zbigniew", "Żelazny"),
(1, null, 8000, "manager", "Nadia", "Jaworska"),
(1, null, 5000, "sales", "Agnieszka", "Górska"),
(1, null, 5000, "sales", "Przemysław", "Rutkowski"),
(1, null, 5000, "sales", "Szymon", "Sobczak"),
(1, null, 5000, "sales", "Justyna", "Czerwińska"),
(1, null, 5000, "sales", "Klemens", "Adamczyk"),
(1, null, 5000, "sales", "Paweł", "Dąbrowski"),
(1, null, 3000, "accountant", "Małgorzata", "Maciejewska"),
(1, null, 3000, "accountant", "Mirosław", "Duda"),
(2, null, 8000, "manager", "Norbert", "Ostrowski"),
(2, null, 5000, "sales", "Bartłomiej", "Nowak"),
(2, null, 5000, "sales", "Krzysztof", "Kwiatkowski"),
(2, null, 5000, "sales", "Zuzanna", "Borkowska"),
(2, null, 3000, "accountant", "Anna", "Chmielewska"),
(null, 1, 6000, "production", "Konstanty", "Zieliński"),
(null, 1, 6000, "production", "Ksawery", "Nowakowski"),
(null, 1, 6000, "production", "Bogusław", "Kalinowski"),
(null, 1, 5000, "production", "Ferdynand", "Sawicki"),
(null, 1, 5000, "production", "Weronika", "Kozłowska"),
(null, 1, 4500, "production", "Bartosz", "Tomaszewski"),
(null, 1, 4500, "production", "Marcin", "Majewski"),
(null, 1, 4500, "production", "Wojciech", "Jasiński"),
(null, 1, 3500, "production", "Maksymilian", "Olszewski"),
(null, 1, 3500, "production", "Walenty", "Lichocki");

INSERT INTO Client_(Employeeid, clientname, city, client_address)
VALUES
(3, "Salon Nowe Auto", "Wrocław", "Chrobrego 14/2"),
(4, "Salon Magnolia", "Wrocław", "Złota 27"),
(4, "Salon Biskupin", "Wrocław", "Tramwajowa 11"),
(13, "Salon Mokotów", "Warszawa", "Inżynierska 119");

INSERT INTO Payment(Clientid, total, realised)
VALUES
(1, 80000, TRUE),
(2, 70000, TRUE),
(2, 110000, FALSE),
(4, 115000, FALSE);

-- możliwa będzie zmiana kolumn o nazwie status na typ ENUM
-- przed etapem implementacyjnym aplikacji pozstawiamy jako typ VARCHAR.

-- przykladowy orderstatus: (jeśli będzie typem ENUM)
-- new, preparing, delivery, finished
INSERT INTO Order_(Clientid, Paymentid, ordertime, orderstatus)
VALUES
(1, 1, '2015-03-01 10:01:33', "Finished"),
(2, 2, '2016-07-04 12:44:21', "Delivery"),
(2, 3, '2017-08-17 11:58:07', "New"),
(2, 4, '2018-11-19 17:39:52', "New");

-- sytuacja analogiczna do j.w.
-- real statusy : planned, assembled, finished)
-- order statusy : free, reserved, sold
INSERT INTO Car(Factoryid, Orderid, real_status, order_status, cartype, colour, carmodel, interior, caryear)
VALUES
(1, 1, "Finished", "Sold", "Sedan", "Red", "Poseidon", "Basic", 2014);

INSERT INTO Part(partname, qty)
VALUES
("Siłownik", 40),
("Felga 19 cali", 25),
("Filtr cząstek stałych", 15);

INSERT INTO Supplier(suppliername)
VALUES
("Marekpol"),
("Tungsten Industries"),
("Nitride");

INSERT INTO Part_Car(Carid, Partid)
VALUES
(1,1),
(1,2);

INSERT INTO Supplier_Part(Partid, Supplierid, price)
VALUES
(1, 1, 40),
(2, 1, 30),
(3, 3, 2000);


CREATE USER 'owner'@'localhost' IDENTIFIED BY 'owner';
CREATE USER 'production'@'localhost' IDENTIFIED BY 'production';
CREATE USER 'accountant'@'localhost' IDENTIFIED BY 'accountant';
CREATE USER 'seller'@'localhost' IDENTIFIED BY 'seller';

CREATE ROLE 'db_owner', 'db_production', 'db_accountant', 'db_seller';

GRANT ALL ON database_.* TO 'owner'@'localhost';

GRANT ALL ON database_.Supplier TO 'db_production';
GRANT ALL ON database_.Part TO 'db_production';
GRANT UPDATE ON database_.Order_ TO 'db_production';
GRANT UPDATE ON database_.Car TO 'db_production';

GRANT ALL ON database_.Client_ TO 'seller'@'localhost';
GRANT ALL ON database_.Order_ TO 'seller'@'localhost';
GRANT ALL ON database_.Car TO 'seller'@'localhost';

GRANT ALL ON database_.Payment TO 'db_accountant';

GRANT 'db_owner' TO 'owner'@'localhost';
GRANT 'db_seller' TO 'seller'@'localhost';
GRANT 'db_accountant' TO 'accountant'@'localhost';
GRANT 'db_production' TO 'production'@'localhost';