select (1 - (sum(qty) - count(*))/sum(qty)) * 100 as Average from hotel_rooms 
where hr_id_hotel = '1'
group by hr_id_hotel having count(*) =
(select count(*) from hotel_rooms 
join reservation on r_id_hotel = hr_id_hotel and r_id_roomType = hr_id_roomType
where hr_id_hotel = 1 and  ( real_check_in <= curdate() and real_check_in >= date_sub(curdate() , interval 12 month) )
and ( real_check_out <= curdate() and real_check_out >= date_sub(curdate() , interval 12 month) ) group by hr_id_hotel )
