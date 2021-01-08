SELECT  h.name ,h.stars,  rt.id_roomType, price, qty as total,qty - count(*) as available
from hotel h
join hotel_rooms hr on h.id_hotel = hr.hr_id_hotel
join room_type rt on hr.hr_id_roomType = rt.id_roomType
join reservation r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType 
where ( h.id_hotel = 7 and ( 
( CURDATE() >=r.real_check_in and CURDATE() <=r.real_check_out)))
group by hr.hr_id_roomType having available>0
UNION
SELECT DISTINCT h.name , h.stars, rt.id_roomType,price , hr.QTY as total , qty as available
from hotel h
join hotel_rooms hr on h.id_hotel = hr.hr_id_hotel
join room_type rt on hr.hr_id_roomType = rt.id_roomType
where h.id_hotel = 7 and  rt.id_roomType  not in(select r.r_id_roomType from reservation r where hr.hr_id_hotel=r.r_id_hotel and  rt.id_roomType = r.r_id_roomType)
UNION
SELECT DISTINCT h.name , h.stars, rt.id_roomType,price ,qty as total,qty as available
from hotel h
join hotel_rooms hr on h.id_hotel = hr.hr_id_hotel
join room_type rt on hr.hr_id_roomType = rt.id_roomType
join reservation r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType 
where ( h.id_hotel=7 and (  CURDATE() < r.real_check_in or  CURDATE()> r.real_check_out) )