SELECT  distinct h.name ,h.stars,  rt.id_roomType, price, qty as total,qty - count(*) as available
from HOTEL h
join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel
join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType
join RESERVATION r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType 
where ( h.id_hotel = 22 and ( 
( CURDATE() >=r.real_check_in and CURDATE() <=r.real_check_out)))
group by hr.hr_id_roomType having available>0
UNION
SELECT DISTINCT h.name , h.stars, rt.id_roomType,price , hr.QTY as total , qty as available
from HOTEL h
join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel
join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType
where h.id_hotel = 22 and  rt.id_roomType  not in(select r.r_id_roomType from RESERVATION r where hr.hr_id_hotel=r.r_id_hotel and  rt.id_roomType = r.r_id_roomType)
UNION
SELECT DISTINCT h.name , h.stars, rt.id_roomType,price ,qty as total,qty as available
from HOTEL h
join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel
join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType
join RESERVATION r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType 
where ( h.id_hotel=22 and (  CURDATE() < r.real_check_in or  CURDATE()> r.real_check_out) )
and id_roomType not in (
	SELECT id_roomType
	from HOTEL
	join HOTEL_ROOMS  on id_hotel = hr_id_hotel
	join ROOM_TYPE  on hr_id_roomType = id_roomType
	join RESERVATION  on hr_id_hotel=r_id_hotel and hr_id_roomType = r_id_roomType 
	where ( id_hotel = 22 and ( ( CURDATE() >=real_check_in and CURDATE() <=real_check_out))))
