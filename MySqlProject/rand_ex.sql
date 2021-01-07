--
-- USER TABLE
--
insert into USER ( first_name, surname, id_number, email, phone_number, country, sex, address, birthday) values 
		( 'Sallyanne', 'Bloyes', 'HM499902', 'sbloyes0@phoca.cz', '+86 424 450 6974', 'China', 'male', 'Debra', '1983-06-02'),
		('Jeana', 'Farady', 'CW951599', 'jfarady1@usgs.gov', '+351 975 512 1811', 'Portugal', 'male', 'Dunning', '1980-01-15'),
		( 'Aube', 'Jahns', 'NZ506588', 'ajahns2@dedecms.com', '+30 262 122 8972', 'Greece', 'female', 'Shasta', '1980-05-22'),
		( 'Allistir', 'Platfoot', 'TF165472', 'aplatfoot3@google.co.jp', '+235 774 759 2920', 'Chad', 'female', 'Debs', '2010-11-16'),
		('Kesley', 'Jullian', 'IB428356', 'kjullian4@photobucket.com', '+976 642 643 8147', 'Mongolia', 'other', 'Larry', '1952-11-05'),
		('Justina', 'Bernardinelli', 'TV759258', 'jbernardinelli5@ft.com', '+228 462 629 1435', 'Togo', 'female', '1st', '2002-04-27'),
		( 'Homerus', 'Watkinson', 'JZ815420', 'hwatkinson6@hexun.com', '+95 747 997 5768', 'Myanmar', 'female', 'Meadow Vale', '2005-10-09'),
		( 'Gerick', 'Brookshaw', 'YF323460', 'gbrookshaw7@clickbank.net', '+81 347 700 4806', 'Japan', 'female', 'Banding', '1988-06-25'),
		( 'Yves', 'Trethowan', 'SY239417', 'ytrethowan8@mysql.com', '+81 971 397 7447', 'Japan', 'male', 'Anniversary', '1997-09-18'),
		( 'Gaynor', 'Sperring', 'JS566007', 'gsperring9@miitbeian.gov.cn', '+1 151 526 5643', 'Canada', 'other', 'Bonner', '1958-05-19');



--
-- LOGIN TABLE
--

insert into LOGIN (l_id_user, password, username) values 
		(1,'5LSLc9', 'fmenlove0'),
		(2,'Jf7zRa81DU', 'ceckly1'),
		(3,'OxZKHsH1H2F', 'lcoulter2'),
		(4,'FrybKYs7bj1w', 'tgiabucci3'),
		(5,'7ahR8yotx', 'ewellings4'),
		(6,'yGOxrL1UxO', 'mjohnys5'),
		(7,'IkxL4yusjM4l', 'glaurencot6'),
		(8,'BXc3UGICj', 'jriggey7'),
		(9,'q2lhXy', 'bforrestor8'),
		(10,'81TJ1RGyd', 'ysneden9');




--
-- OWNER TABLE
--

insert into OWNER (id_owner) values 
			(3),
			(5),
			(9);


--
-- GUEST TABLE
--

insert into GUEST (id_guest, NOreservations, card_type, card_number, cvv, expire_date) values 
				(10, 2, null, null, null, null),
				(3, 13, 'VISA', '491723268247404', 699, '2027-03-05'),
				(8, 11, 'MASTERCARD', '560221255666216', 378, '2025-08-21'),
				(2, 8,  null, null, null, null),
				(6, 14,  'VISA', '560340897379152', 323, '2027-11-20'),
				(4, 16,  'MASTERCARD', '301485321358403', 472, '2024-06-23'),
				(1, 13,'MASTERCARD', '33794111151043', 555, '2027-02-01'),
				(7, 9, 'VISA', '56022234425816', 611, '2027-06-28 ');


--
-- PAYMENT TABLE
--

insert into PAYMENT (deposit, payment_type, billing_address) values 
			(20, 'DEBIT CARD', 'Mayer'),
			(16, 'DEBIT CARD', 'Twin Pines'),
			(21, 'DEBIT CARD', 'Brentwood'),
			(21, 'PAYPAL', 'Farragut'),
			(12, 'PAYPAL', 'West'),
			(14, 'BANK ACCOUNT', 'Marquette'),
			(18, 'DEBIT CARD', 'Fisk'),
			(14, 'PAYPAL', 'Red Cloud'),
            (20, 'DEBIT CARD', 'add1'),
            (21, 'PAYPAL', 'add2'),
            (11, 'BANK ACCOUNT', 'add3'),
            (15, 'PAYPAL', 'add4'),
            (16, 'DEBIT CARD', 'add5'),
            (17, 'DEBIT CARD', 'add6'),
            (22, 'BANK ACCOUNT', 'add7'),
            (40, 'BANK ACCOUNT','add8'),
            (40, 'DEBIT CARD','add9'),
            (40, 'PAYPAL','add10'),
            (40, 'BANK ACCOUNT','add11'),
            (40, 'PAYPAL','add12'),
            (40, 'DEBIT CARD','add13'),
            (40, 'BANK ACCOUNT','add14'),
            (40, 'PAYPAL','add15'),
            (40, 'BANK ACCOUNT','add16'),
            (40, 'BANK ACCOUNT','add17')
            ;

--
-- HOTEL TABLE
--

insert into HOTEL (country, city, address, stars, name) values 
			('Sweden', 'Torsås', '93 Lawn Street', 5, 'Leexo'),
			('Pakistan', 'Kamālia', '74829 Park Meadow Circle', 4, 'Avamba'),
			('Colombia', 'Barranco de Loba', '47 Swallow Hill', 4, 'Skinte'),
			('China', 'Donggaocun', '25 Sauthoff Road', 3, 'Twitterbeat'),
			('Russia', 'Samashki', '2 Roth Parkway', 3, 'Buzzshare'),
            ('Greece', 'Athens', 'Plateia Syntagmatos', 5, 'Palace'),
            ('Greece', 'Athens', 'Monastiraki', 4, 'City View'),
            ('Greece', 'Arachova', 'Kentro', 4, 'Lodge'),
            ('Greece', 'Patra','Plateia Georgiou', 4, 'City Center'),
            ('Greece', 'Patra', 'Marina', 3, 'Marina View');



--
-- ROOM TYPE TABLE
--

insert into `ROOM_TYPE` (capacity,suite, pool, hot_tub, smokers, kitchen, bar) values
			(4,'YES','YES','YES','YES','YES','YES'),
            (4,'NO','NO','YES','YES','YES','YES'),
            (4,'NO','NO','NO','NO','NO','NO'),
            (3,'YES','YES','YES','YES','YES','YES'),
            (3,'NO','NO','YES','YES','YES','NO'),
            (2,'NO','NO','YES','YES','YES','NO'),
            (2,'NO','NO','NO','NO','NO','NO'),
            (1,'YES','YES','YES','YES','YES','YES'),
            (1,'NO','NO','NO','NO','NO','NO');
            

--
-- HOTEL ROOMS TABLE
--

insert into `HOTEL_ROOMS` (hr_id_hotel,hr_id_roomType,QTY, price) values
			(1, 1, 5, 100),
            (1, 2, 10, 120),
            (1, 3, 7, 130),
            (2, 2, 10, 90),
            (2, 4, 4, 80),
            (2, 6, 7, 60),
            (2, 8, 4, 80),
            (2, 9, 3, 90),
            (3, 2, 15, 70),
            (3, 4, 10, 60),
            (3, 5, 40, 100),
            (3, 7, 20, 90),
            (4, 1, 3, 80),
            (4, 3, 9, 70),
            (4, 6, 15, 80),
            (4, 8, 10, 90),
            (5, 2, 8, 100),
            (5, 4, 12, 60),
            (5, 6, 10, 70),
            (5, 8, 9, 80),
            (5, 9, 5, 60),
            (6, 1, 10, 150),
            (6, 2, 8, 140),
            (7, 3, 6, 120),
            (7, 4, 4, 100),
            (8, 5, 20, 80),
            (8, 6, 15, 90),
            (9, 7, 15, 90),
            (9, 8, 12, 70),
            (10, 9, 13, 60),
            (10, 1, 11, 95);
            
        

--
-- RESERVATION TABLE
--


insert into RESERVATION ( reservation_date, check_in, check_out, real_check_in, real_check_out, r_id_payment,r_id_hotel,r_id_roomType) values 
('2019-05-25', '2020-01-13', '2020-01-20', '2020-01-13', '2020-01-20', 1, 2, 2),
('2019-05-25', '2020-01-23', '2020-01-26', '2020-01-23', '2020-01-26', 2, 2, 2),
('2019-05-25', '2020-01-13', '2020-01-20', '2020-01-13', '2020-01-20', 3, 2, 2),
('2019-05-25', '2020-01-13', '2020-01-20', '2020-01-13', '2020-01-20', 4, 2, 2),
('2020-09-20', '2020-12-30', '2021-01-05', '2020-12-30', '2021-01-05', 5, 1, 1),
('2020-10-12', '2020-12-31', '2021-01-03', '2020-12-31', '2021-01-03', 6, 1, 1),
('2020-11-20', '2021-01-01', '2021-01-04', '2021-01-01', '2021-01-04', 7, 1, 2),
('2020-11-12', '2021-02-08', '2021-02-13', '2021-02-08', '2021-02-13', 8, 3, 4),
('2020-11-22', '2020-12-23', '2020-12-27', '2020-12-23', '2020-12-27',9, 3, 5),
('2020-11-25', '2020-12-24', '2020-12-29', '2020-12-24', '2020-12-29',10, 3, 7),
('2020-11-26', '2020-12-27', '2020-12-30', '2020-12-27', '2020-12-30',11, 4, 3),
('2020-12-03', '2020-12-28', '2021-01-02', '2020-12-28', '2021-01-02', 12, 4, 8),
('2020-12-05', '2020-12-30', '2021-01-05', '2020-12-30', '2021-01-05', 13, 5, 4),
('2020-12-16', '2020-12-31', '2021-01-05', '2020-12-31', '2021-01-05', 14, 5, 6),
('2020-12-17', '2021-01-02', '2021-01-04', '2021-01-02', '2021-01-04',15, 5, 8),
('2020-12-17', '2021-01-02', '2021-01-08', '2021-01-02', '2021-01-08',  16, 6, 1),
('2020-12-17', '2021-01-05', '2021-01-10', '2021-01-05', '2021-01-10',17, 6, 2),
('2020-12-18', '2021-02-10', '2021-02-16', '2021-02-10', '2021-02-16', 18, 7, 3),
('2020-12-20', '2021-02-02', '2021-02-06', '2021-02-02', '2021-02-06', 19, 7, 4),
('2020-12-21', '2021-02-20', '2021-02-25', '2021-02-20', '2021-02-25', 20, 8, 5),
('2020-12-23', '2021-03-02', '2021-03-08', '2021-03-02', '2021-03-08', 21, 8, 6),
('2020-12-24', '2021-03-10', '2021-03-14', '2021-03-10', '2021-03-14', 22, 9, 7),
('2020-12-26', '2021-03-15', '2021-03-21', '2021-03-15', '2021-03-21', 23, 9, 8),
('2020-12-27', '2021-06-02', '2021-06-08', '2021-06-02', '2021-06-08',  24, 10, 9),
('2020-12-27', '2021-07-20', '2021-07-25',  '2021-07-20', '2021-07-25',25, 10, 1)
;



-- 
-- MAKE TABLE
--

insert into `MAKE` (m_id_guest, m_id_reservation) values 
				(3, 1),
				(2, 2),
				(8, 3),
				(8, 4),
                (1,5),
                (4,6),
                (10,7),
                (7,8),
                (6,9),
                (10,10),
                (3,11),
                (1,12),
                (4,13),
                (6,14),
                (7,15),
                (1,16),
                (2,17),
                (3,18),
                (4,19),
                (6,20),
                (7,21),
                (8,22),
                (10,23),
                (3,24),
                (7,25);




        
 

                
                




--
-- MANAGE TABLE
--

insert into `MANAGE` (m_id_owner, m_id_hotel) values 
		(3, 1),
		(9, 2),
		(9, 3),
		(5, 4),
		(9, 5),
        (3, 6),
        (3, 8),
        (5, 7),
        (5, 9),
        (9, 10);
        
-- payment update
update `PAYMENT` p
	join `RESERVATION` r
    on p.id_payment = r.r_id_payment
	join `HOTEL_ROOMS` hr
    on  hr.hr_id_hotel = r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType
	set p.amount_per_day = hr.price;
    

update `PAYMENT` p
	join `RESERVATION` r
    on p.id_payment = r.r_id_payment
    join `HOTEL_ROOMS` hr
    on  hr.hr_id_hotel = r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType
     set p.total_amount = datediff(r.real_check_out, r.real_check_in)*hr.price;

update `PAYMENT` p
	join `RESERVATION` r
    on p.id_payment = r.r_id_payment
    join `HOTEL_ROOMS` hr
    on  hr.hr_id_hotel = r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType
     set p.deposit = (20/100) * datediff(r.real_check_out, r.real_check_in)*hr.price;
     
     
update `PAYMENT` p
	join `RESERVATION` r
    on p.id_payment = r.r_id_payment
    join `HOTEL_ROOMS` hr
    on  hr.hr_id_hotel = r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType
     set p.deposit = 0
     where p.id_payment = 0 or  p.id_payment = 2 or p.id_payment = 4 or p.id_payment = 5 or p.id_payment = 8;
     
update `PAYMENT` p
	join `RESERVATION` r
    on p.id_payment = r.r_id_payment
    join `HOTEL_ROOMS` hr
    on  hr.hr_id_hotel = r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType
     set p.amount_left = 0
     where p.deposit = 0  or r.real_check_out < curdate();
     
update `PAYMENT` p
	join `RESERVATION` r
    on p.id_payment = r.r_id_payment
    join `HOTEL_ROOMS` hr
    on  hr.hr_id_hotel = r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType
     set p.amount_left = p.total_amount - p.deposit
     where p.deposit != 0  and r.real_check_out >= curdate();
     
-- Guest reservation update
SET SQL_SAFE_UPDATES = 0;
update `GUEST` g
	set g.NOreservations = (
		select count(id_guest) from `MAKE` m where m.m_id_guest = g.id_guest group by id_guest);
SET SQL_SAFE_UPDATES = 1;
