select count(*) 
from MAKE 
join GUEST on id_guest = m_id_guest
join RESERVATION on id_reservation = m_id_reservation
where r_id_hotel = 2 and id_guest = 8
group by (m_id_guest)