SELECT h.name , rt.id_roomType, h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price ,qty - count(*) as count
from HOTEL h
join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel
join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType
join RESERVATION r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType 
where ( h.country = "Spain" and h.city = 'Granada' and ( 
( '2021-01-10' <=r.real_check_in  and'2021-01-19' >=r.real_check_in and '2021-01-19' <=r.real_check_out) or 
( '2021-01-10' >= r.real_check_in  and '2021-01-10' <= r.real_check_out  and '2021-01-19' >=r.real_check_in and '2021-01-19' <=r.real_check_out) or 
( '2021-01-10' >= r.real_check_in  and  '2021-01-10' <=r.real_check_out and '2021-01-19' >= r.real_check_out) or 
('2021-01-10'<= r.real_check_in and  '2021-01-19' >= r.real_check_out)))
group by hr.hr_id_roomType,h.name, h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price ,qty , id_hotel having count>0
UNION
SELECT DISTINCT h.name , rt.id_roomType, h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price , hr.QTY
from HOTEL h
join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel
join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType
where h.country = "spain" and h.city = 'granada' and  rt.id_roomType  not in(select r.r_id_roomType from RESERVATION r where hr.hr_id_hotel=r.r_id_hotel and  rt.id_roomType = r.r_id_roomType)
UNION
SELECT DISTINCT h.name , rt.id_roomType, h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price ,qty as count
from HOTEL h
join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel
join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType
join RESERVATION r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType 
where ( h.country = "spain" and h.city = 'granada'and ( '2021-01-19' < r.real_check_in or '2021-01-10'> r.real_check_out) )
and rt.id_roomType not in (
	SELECT id_roomType
	from HOTEL
	join HOTEL_ROOMS  on id_hotel = hr_id_hotel
	join ROOM_TYPE  on hr_id_roomType = id_roomType
	join RESERVATION  on hr_id_hotel=r_id_hotel and hr_id_roomType = r_id_roomType 
	where ( country = "spain" and city = 'granada' and ( 
	( '2021-01-10' <=real_check_in  and'2021-01-19' >=real_check_in and '2021-01-19' <=real_check_out) or 
	( '2021-01-10' >= real_check_in  and '2021-01-10' <= real_check_out  and '2021-01-19' >=real_check_in and '2021-01-19' <=real_check_out) or 
	( '2021-01-10' >= real_check_in  and  '2021-01-10' <=real_check_out and '2021-01-19' >= real_check_out) or 
	('2021-01-10'<= real_check_in and  '2021-01-19' >= real_check_out))))