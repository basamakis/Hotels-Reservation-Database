select h.name , h.stars ,h.country,h.city,h.address
from manage m 
join owner o on o.id_owner = m.m_id_owner
join hotel h on h.id_hotel = m.m_id_hotel
where id_owner = 3