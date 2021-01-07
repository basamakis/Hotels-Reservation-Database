--
-- USER TABLE
--
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `USER`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `USER` (
	`id_user` int auto_increment PRIMARY KEY,
	`first_name` varchar(20) NOT NULL,
	`surname` varchar(20) NOT NULL,
	`id_number` varchar(8) NOT NULL UNIQUE,
	`email` varchar(254) NOT NULL UNIQUE,
	`phone_number` varchar(17) NOT NULL UNIQUE,
	`country` varchar(20) NOT NULL,
	`sex` ENUM('female','male','other'),
	`address` varchar(40),
	`birthday` DATETIME NOT NULL
)ENGINE = InnoDB;





--
-- PAYMENT TABLE
--

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `PAYMENT`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `PAYMENT` (
	`id_payment` int auto_increment PRIMARY KEY ,	
	`amount_per_day` float NOT NULL default(1),
    `total_amount` float NOT NULL default(1),
    `amount_left` float NOT NULL default(1),
	`deposit` float NOT NULL default(1),
	`payment_type` ENUM ('BANK ACCOUNT','DEBIT CARD','PAYPAL'),
	`billing_address` varchar(40) NOT NULL
)ENGINE = InnoDB ;


--
-- HOTEL TABLE
--

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `HOTEL`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `HOTEL` (
	`id_hotel` int auto_increment PRIMARY KEY,
	`country` varchar(20) NOT NULL,
	`city` varchar(20) NOT NULL,
	`address` varchar(40) NOT NULL,
	`stars` INT(1) NOT NULL,
	`name` varchar(25) NOT NULL
)ENGINE = InnoDB ;



--
-- ROOM TYPE TABLE
--

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `ROOM_TYPE`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `ROOM_TYPE` (
	`id_roomType` int auto_increment PRIMARY KEY,
    `capacity` INT NOT NULL CHECK (`capacity`>=1 and `capacity`<=7),
	`suite` ENUM('YES','NO') NOT NULL,
	`pool`	ENUM('YES','NO') NOT NULL,
	`hot_tub` ENUM('YES','NO') NOT NULL,
	`smokers` ENUM('YES','NO')NOT NULL,
	`kitchen` ENUM('YES','NO') NOT NULL,
	`bar` ENUM('YES','NO') NOT NULL
)ENGINE = InnoDB ;


--
-- HOTEL ROOMS TABLE
--

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `HOTEL_ROOMS`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `HOTEL_ROOMS` (
	`hr_id_hotel` int,
    `hr_id_roomType` int,
    `QTY` INT NOT NULL,
    `price` int not null,
    PRIMARY KEY(`hr_id_hotel`,`hr_id_roomType`),
    CONSTRAINT `hotel_rooms_fk0` FOREIGN KEY (`hr_id_hotel`) REFERENCES `HOTEL`(`id_hotel`) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `hotel_rooms_fk1` FOREIGN KEY (`hr_id_roomType`) REFERENCES `ROOM_TYPE`(`id_roomType`) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB ;




--
-- RESERVATION TABLE
--

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `RESERVATION`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `RESERVATION` (
	`id_reservation` int auto_increment PRIMARY KEY,
	`reservation_date` DATE NOT NULL,
	`check_in` DATE NOT NULL,
	`check_out` DATE NOT NULL,
	`real_check_in` DATE,
	`real_check_out` DATE,
	`r_id_payment` int NOT NULL UNIQUE,
    `r_id_hotel`  int NOT NULL,
    `r_id_roomType` int NOT NULL,
    CONSTRAINT `reservation_fk0` FOREIGN KEY (`r_id_hotel`) REFERENCES `HOTEL_ROOMS`(`hr_id_hotel`) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `reservation_fk1` FOREIGN KEY (`r_id_roomType`) REFERENCES `HOTEL_ROOMS`(`hr_id_roomType`) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `reservation_fk2` FOREIGN KEY (`r_id_payment`) REFERENCES `PAYMENT`(`id_payment`) ON DELETE CASCADE ON UPDATE CASCADE
    )ENGINE = InnoDB ; 


--
-- LOGIN TABLE
--
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `LOGIN`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `LOGIN` (
	`l_id_user` int  PRIMARY KEY,
	`password` varchar(20) NOT NULL UNIQUE,
	`username` varchar(20) NOT NULL UNIQUE,
    CONSTRAINT `login_fk0` FOREIGN KEY (`l_id_user`) REFERENCES `USER`(`id_user`) ON DELETE CASCADE ON UPDATE CASCADE
    )ENGINE = InnoDB;



--
-- OWNER TABLE
--

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `OWNER`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `OWNER` (
	`id_owner` int PRIMARY KEY,
    CONSTRAINT `owner_fk0` FOREIGN KEY (`id_owner`) REFERENCES `USER`(`id_user`) ON DELETE CASCADE ON UPDATE CASCADE
    )ENGINE = InnoDB;



--
-- GUEST TABLE
--

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `GUEST`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `GUEST` (
	`id_guest` int PRIMARY KEY,
    `NOreservations` INT NOT NULL, /*VAMOS A VER*/
	`card_type` ENUM('MASTERCARD','VISA') ,
	`card_number` VARCHAR(16)  UNIQUE,
	`cvv` INT ,
	`expire_date` DATE,
    CONSTRAINT `guest_fk0` FOREIGN KEY (`id_guest`) REFERENCES `USER`(`id_user`) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB ;


SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `MAKE`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `MAKE` (
	`m_id_guest` int,
    `m_id_reservation` int ,
    PRIMARY KEY(`m_id_guest`,`m_id_reservation`),
    CONSTRAINT `make_fk0` FOREIGN KEY (`m_id_guest`) REFERENCES `GUEST`(`id_guest`) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `make_fk1` FOREIGN KEY (`m_id_reservation`) REFERENCES `RESERVATION`(`id_reservation`) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB;










--
-- MANAGE TABLE
--

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `MANAGE`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `MANAGE` (
	`m_id_owner` int ,
	`m_id_hotel` int ,
	PRIMARY KEY (`m_id_owner`,`m_id_hotel`),
    CONSTRAINT `manage_fk0` FOREIGN KEY (`m_id_owner`) REFERENCES `OWNER`(`id_owner`) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `manage_fk1` FOREIGN KEY (`m_id_hotel`) REFERENCES `HOTEL`(`id_hotel`) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB;