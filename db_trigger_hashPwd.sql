DELIMITER $$

CREATE TRIGGER hash_password_trigger BEFORE INSERT ON user
FOR EACH ROW
BEGIN
    IF NEW.password IS NOT NULL THEN
        SET NEW.password = SHA2(NEW.password, 256);
    END IF;
END$$

DELIMITER ;