select t2.cn*100 / t1.sm as average
from ( 	select sum(qty) as sm from HOTEL_ROOMS where hr_id_hotel = 22 ) t1
join (	select count(*) as cn from HOTEL_ROOMS 
		join RESERVATION on r_id_hotel = hr_id_hotel and r_id_roomType = hr_id_roomType
		where hr_id_hotel = 22 and  ( real_check_in <= curdate() and real_check_in >= date_sub(curdate() , interval 12 month) )
		and ( real_check_out <= curdate() and real_check_out >= date_sub(curdate() , interval 12 month) ) group by hr_id_hotel ) t2


