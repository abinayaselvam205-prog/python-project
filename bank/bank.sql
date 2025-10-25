USE abinaya;
CREATE TABLE bank_info(
id INT AUTO_INCREMENT PRIMARY KEY,
account_holder VARCHAR(20) NOT NULL UNIQUE,
pin CHAR(4) NOT NULL,
balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO bank_info(account_holder,pin,balance) VALUES
("abinaya selvam",1112,20000);
SELECT * FROM bank_info;