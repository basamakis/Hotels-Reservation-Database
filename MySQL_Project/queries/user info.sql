select username , first_name , surname , NOreservations ,reservation_points
from user 
join guest on id_guest = id_user 
join login on l_id_user = id_user
where id_user = 'U1'