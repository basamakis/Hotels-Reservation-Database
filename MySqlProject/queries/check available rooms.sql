SELECT h.name , rt.id_roomType, h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price ,qty - count(*) as count
from hotel h
join hotel_rooms hr on h.id_hotel = hr.hr_id_hotel
join room_type rt on hr.hr_id_roomType = rt.id_roomType
join reservation r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType 
where ( h.country = "Colombia" and h.city = 'Barranco de Loba' and ( 
( '2021-02-07' <=r.real_check_in  and'2021-02-15' >=r.real_check_in and '2021-02-15' <=r.real_check_out) or 
( '2021-02-07' >= r.real_check_in  and '2021-02-07' <= r.real_check_out  and '2021-02-15' >=r.real_check_in and '2021-02-15' <=r.real_check_out) or 
( '2021-02-07' >= r.real_check_in  and  '2021-02-07' <=r.real_check_out and '2021-02-15' >= r.real_check_out) or 
('2021-02-07'<= r.real_check_in and  '2021-02-15' >= r.real_check_out)))
group by hr.hr_id_roomType having count>0
UNION
SELECT DISTINCT h.name , rt.id_roomType, h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price , hr.QTY
from hotel h
join hotel_rooms hr on h.id_hotel = hr.hr_id_hotel
join room_type rt on hr.hr_id_roomType = rt.id_roomType
where h.country = "Colombia" and h.city = 'Barranco de Loba' and  rt.id_roomType  not in(select r.r_id_roomType from reservation r where hr.hr_id_hotel=r.r_id_hotel and  rt.id_roomType = r.r_id_roomType)
UNION
SELECT DISTINCT h.name , rt.id_roomType, h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price ,qty as count
from hotel h
join hotel_rooms hr on h.id_hotel = hr.hr_id_hotel
join room_type rt on hr.hr_id_roomType = rt.id_roomType
join reservation r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType 
where ( h.country = "Colombia" and h.city = 'Barranco de Loba'and ( '2021-02-15' < r.real_check_in or '2021-02-07'> r.real_check_out) )