select price,capacity,suite,pool,hot_tub,smokers,kitchen,bar
from hotel_rooms  
join room_type on id_roomType = hr_id_roomType
join hotel on id_hotel = hr_id_hotel
where name = 'Avamba'