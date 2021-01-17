select name , capacity , reservation_date , real_check_in , real_check_out , amount
from reservation
join make on id_reservation = m_id_reservation
join hotel on id_hotel = r_id_hotel
join payment on id_payment = r_id_payment
join room_type on id_roomType = r_id_roomType
where m_id_guest = 'U2'
