

DELIMITER //

CREATE PROCEDURE GetIncome()
BEGIN
SELECT COUNT(realised) FROM Payment;
END//

CREATE PROCEDURE GetSalaries()
BEGIN
SELECT COUNT(salary) FROM Employee;
END//

CREATE PROCEDURE GetFactoryCost()
BEGIN
SELECT COUNT(factorycosty) FROM Factory;
END//

CREATE PROCEDURE GetOfficeCost()
BEGIN
SELECT COUNT(officecost) FROM Office;
END//

CREATE PROCEDURE GetPartCost()
BEGIN
SELECT COUNT(price) FROM Supplier_Part;
END//

DELIMITER ;

