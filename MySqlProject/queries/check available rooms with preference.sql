SELECT DISTINCT h.name ,rt.id_roomType,h.stars,rt.capacity,rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar
from hotel_rooms hr
join reservation r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType
join hotel h on hr.hr_id_hotel = h.id_hotel
join room_type rt on rt.id_roomType = hr.hr_id_roomType
where ('2020-12-30' > r.real_check_out and h.country = 'Pakistan' and h.city = 'Kamālia'  and rt.suite='NO' and rt.pool='NO'
and rt.hot_tub='YES' and rt.smokers='YES'and rt.kitchen='YES' and rt.bar='YES')