import mysql.connector as mysqlc
import Searching as search

#login into your account
def qlogin(username,password):
    global storeVal
    #####Connect to DATABASE#####
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975", database='project_db20_up1046975')
    mycursor = mydb.cursor()
    ######check if username and password exist######
    strn = " select l.username from LOGIN l where  ( l.username = " + "\'" + username  + "\'" + " and l.password = " + "\'"  + password + "\'" + ")"
    mycursor.execute(strn)
    x = 0
    for x in mycursor:
        pass
    strn = "select l_id_user from LOGIN where username = " + "\'" + username  + "\'"
    mycursor.execute(strn)
    id = mycursor.fetchall()
    mydb.commit()
    mydb.close()
    if x == 0:
        return x
    else:
        return id


#Register (Create New Account)
def adduser(username,password,fname,lname,email,idnum,pnum,country,sex,addr,birth):
    #Connect to DATABASE
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975", database='project_db20_up1046975')
    mycursor = mydb.cursor()

    username = "\'" + username + "\'"
    str1 = "SELECT username from LOGIN where username = " + username
    mycursor.execute(str1)
    tempuse = 'ok'
    for tempuse in mycursor : pass
    tempuse = "\'" + tempuse[0] + "\'"
    if tempuse == username: return 1
    password = "\'" + password + "\'"
    if len(password) < 6 : return 0
    fname = "\'" + fname + "\'"
    if len(fname) < 3 and len(fname) > 20 : return 0
    lname = "\'" + lname + "\'"
    if len(lname) < 3 and len(lname) > 20: return 0
    idnum = "\'" + idnum + "\'"
    if len(idnum) != 10 : return 0
    email = "\'" + email + "\'"
    if len(email)<12 and len(email)>254: return 0
    pnum = "\'" + pnum + "\'"
    if len(pnum) <10 and len(pnum) > 17 : return 0
    country = "\'" + country + "\'"
    country.capitalize()
    if len(country)<3 and len(country)>20 : return 0
    sex = "\'" + sex + "\'"
    addr = "\'" + addr + "\'"
    if len(addr) < 4 and len(addr) > 40 : return 0
    birth = "\'" + birth + "\'"
    strn = "insert into USER ( first_name, surname, id_number, email, phone_number, country, sex, address, birthday) values"
    strn= strn + "(" + fname + "," + lname + "," + idnum + "," + email + "," + pnum + "," + country + "," + sex + "," + addr + "," + birth + ");"
    mycursor.execute(strn)
    mydb.commit()
    strn = "insert into LOGIN (l_id_user,password, username) values "
    strn = strn + "(last_insert_id()," + password + "," + username + " )"
    mycursor.execute(strn)
    mydb.commit()
    strn =  "insert into GUEST (id_guest, NOreservations, card_type, card_number, cvv, expire_date) values" \
            "(last_insert_id(), 0, null, null, null, null)"
    mycursor.execute(strn)
    mydb.commit()
    mydb.close()
    return 2



#search rooms in a specific city of a country
def availRoom(checkin , country , city,checkout,flag):
    #Connect to DATABASE
    if flag==0:
        country = '\'' + country + '\''
        city = '\'' + city + '\''
        checkin = '\'' + checkin + '\''
        checkout = '\'' + checkout + '\''
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975", database='project_db20_up1046975')
    mycursor = mydb.cursor()
    str = "SELECT datediff(" + checkout + "," + checkin + ") as days; "
    mycursor.execute(str)
    x = mycursor.fetchall()
    days = x[0][0]
    mycursor = mydb.cursor()
    #Create Select String
    str = "SELECT DISTINCT h.name ,  h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price, qty - count(*) as count , id_hotel , id_roomType" \
            " from HOTEL h join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel " \
            " join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType " \
            " join RESERVATION r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType  " \
            " where ( h.country = " + country + " and h.city = " + city + " and ( " \
            " ( " + checkin + " <=r.real_check_in  and " +checkout + " >= r.real_check_in and " + checkout + " <=r.real_check_out) or  " \
            " ( " + checkin + " >= r.real_check_in  and " + checkin + " <= r.real_check_out  and " + checkout + " >=r.real_check_in and " + checkout + "<=r.real_check_out) or " \
            "( " + checkin + " >= r.real_check_in  and  " + checkin + " <=r.real_check_out and " + checkout + " >= r.real_check_out) or " \
            " ( " +checkin + "<= r.real_check_in and " + checkout + " >= r.real_check_out)))" \
            " group by hr.hr_id_roomType,h.name, h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price ,qty , id_hotel having count>0"
    str = str + " union SELECT DISTINCT h.name ,  h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price, hr.QTY , id_hotel , id_roomType" \
                " from HOTEL h join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel " \
                " join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType " \
                " where h.country =" + country + " and h.city = " + city + "and " \
                " rt.id_roomType  not in(select r.r_id_roomType from RESERVATION r where hr.hr_id_hotel=r.r_id_hotel and  rt.id_roomType = r.r_id_roomType)"
    str = str + "UNION SELECT DISTINCT h.name ,  h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price, hr.QTY , id_hotel , id_roomType " \
                " from HOTEL h join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel " \
                " join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType " \
                " join RESERVATION r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType  " \
                "where ( h.country =  " + country + " and h.city = " +city+ " and ( " + checkout + " < r.real_check_in or " + checkin + "> r.real_check_out) )"
    mycursor.execute(str)
    #Print Results in GUI
    root = search.hotelTemplate(country,city,checkin,checkout)
    j = 2
    for x in mycursor:
        totalPay = x[9] * days
        search.printHotels(root, x, j,checkin,checkout,totalPay)
        j = j + 1
    mydb.commit()
    mydb.close()

#search rooms with preferences
def availRoomPref(checkin,country,city,checkout,capac,prRange,pref):
    #Connect to DATABASE
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975", database='project_db20_up1046975')
    mycursor = mydb.cursor()
    str = "SELECT datediff(" + checkout + "," + checkin + ") as days; "
    mycursor.execute(str)
    x = mycursor.fetchall()
    days = x[0][0]
    mycursor = mydb.cursor()
    root = search.hotelTemplate( country, city, checkin, checkout)
    str = "SELECT DISTINCT h.name ,  h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price, qty - count(*) as count , id_hotel , id_roomType" \
            " from HOTEL h join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel " \
            " join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType " \
            " join RESERVATION r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType  " \
            " where ( h.country = " + country + " and h.city = " + city + " and ( " \
            " ( " + checkin + " <=r.real_check_in  and " +checkout + " >= r.real_check_in and " + checkout + " <=r.real_check_out) or  " \
            " ( " + checkin + " >= r.real_check_in  and " + checkin + " <= r.real_check_out  and " + checkout + " >=r.real_check_in and " + checkout + "<=r.real_check_out) or " \
            "( " + checkin + " >= r.real_check_in  and  " + checkin + " <=r.real_check_out and " + checkout + " >= r.real_check_out) or " \
            " ( " +checkin + "<= r.real_check_in and " + checkout + " >= r.real_check_out)))"
    if pref[0] == '\'' + 'YES' + '\'':    str = str + " and  rt.suite= " + pref[0]
    if pref[1] == '\'' + 'YES' + '\'':    str = str + " and rt.pool= " + pref[1]
    if pref[2] == '\'' + 'YES' + '\'':    str = str + " and rt.hot_tub= " + pref[2]
    if pref[3] == '\'' + 'YES' + '\'':    str = str + " and rt.smokers= " + pref[3]
    if pref[4] == '\'' + 'YES' + '\'':    str = str + " and rt.kitchen= " + pref[4]
    if pref[5] == '\'' + 'YES' + '\'':    str = str + " and rt.bar= " + pref[5]
    if prRange[0] != '':
        str = str + " and price>= " + prRange[0]
        if prRange[1] != '': str = str + " and price<= " + prRange[1]
    if capac != '' :    str = str +  " and rt.capacity= " + capac
    str = str + " group by hr.hr_id_roomType,h.name, h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price ,qty , id_hotel having count>0 " \
                " union SELECT DISTINCT h.name ,  h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar,price, hr.QTY , id_hotel , id_roomType" \
                " from HOTEL h join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel " \
                " join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType " \
                " where h.country =" + country + " and h.city = " + city
    if pref[0] == '\'' + 'YES' + '\'':    str = str + " and  rt.suite= " + pref[0]
    if pref[1] == '\'' + 'YES' + '\'':    str = str + " and rt.pool= " + pref[1]
    if pref[2] == '\'' + 'YES' + '\'':    str = str + " and rt.hot_tub= " + pref[2]
    if pref[3] == '\'' + 'YES' + '\'':    str = str + " and rt.smokers= " + pref[3]
    if pref[4] == '\'' + 'YES' + '\'':    str = str + " and rt.kitchen= " + pref[4]
    if pref[5] == '\'' + 'YES' + '\'':    str = str + " and rt.bar= " + pref[5]
    if prRange[0] != '':
        str = str + " and price>= " + prRange[0]
        if prRange[1] != '': str = str + " and price<= " + prRange[1]
    if capac != '' :    str = str +  " and rt.capacity= " + capac
    str = str  + "  and rt.id_roomType  not in(select r.r_id_roomType from RESERVATION r where hr.hr_id_hotel=r.r_id_hotel and  rt.id_roomType = r.r_id_roomType )"
    str = str + "UNION SELECT DISTINCT h.name ,  h.stars, rt.capacity, rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar, price, hr.QTY , id_hotel , id_roomType " \
                " from HOTEL h join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel " \
                " join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType " \
                " join RESERVATION r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType  " \
                "where ( h.country =  " + country + " and h.city = " +city+ " and ( " + checkout + " < r.real_check_in or " + checkin + "> r.real_check_out) )"
    if pref[0] == '\'' + 'YES' + '\'':    str = str + " and  rt.suite= " + pref[0]
    if pref[1] == '\'' + 'YES' + '\'':    str = str + " and rt.pool= " + pref[1]
    if pref[2] == '\'' + 'YES' + '\'':    str = str + " and rt.hot_tub= " + pref[2]
    if pref[3] == '\'' + 'YES' + '\'':    str = str + " and rt.smokers= " + pref[3]
    if pref[4] == '\'' + 'YES' + '\'':    str = str + " and rt.kitchen= " + pref[4]
    if pref[5] == '\'' + 'YES' + '\'':    str = str + " and rt.bar= " + pref[5]
    if prRange[0] != '':
        str = str + " and price>= " + prRange[0]
        if prRange[1] != '': str = str + " and price<= " + prRange[1]
    if capac != '' :    str = str +  " and rt.capacity= " + capac
    mycursor.execute(str)
    j = 2
    for x in mycursor:
        totalPay = x[9] * days
        search.printHotels(root, x, j,checkin,checkout,totalPay)
        j = j + 1
    mydb.commit()
    mydb.close()


def qprof(id):
    root = search.profile(id)
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975", database='project_db20_up1046975')
    mycursor = mydb.cursor()
    ida = str(tuple(id))
    ida = ida.replace(')','')
    ida = ida.replace(',','')
    ida = ida.replace('(', '')
    if ida!='' :
        strn = "select username , first_name , surname , NOreservations " \
                    " from USER " \
                    " join GUEST on id_guest = id_user " \
                    " join LOGIN on l_id_user = id_user" \
                    " where id_user = " + ida
        mycursor.execute(strn)
    j = 1
    for x in mycursor:
        search.printInfo(root, x, j)
        j = j + 1
    mydb.commit()
    mydb.close()


def qshowRes(id):
    root = search.showRev()
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975", database='project_db20_up1046975')
    mycursor = mydb.cursor()
    ida = str(tuple(id))
    ida = ida.replace(')','')
    ida = ida.replace(',','')
    ida = ida.replace('(', '')
    if ida!='' :
        strn = "select name , capacity , reservation_date , real_check_in , real_check_out , amount_left , deposit , total_amount " \
              "from RESERVATION join MAKE on id_reservation = m_id_reservation " \
              "join HOTEL on id_hotel = r_id_hotel " \
              "join PAYMENT on id_payment = r_id_payment " \
              "join ROOM_TYPE on id_roomType = r_id_roomType " \
              "where m_id_guest = " + ida
        mycursor.execute(strn)
        x = mycursor.fetchall()
    j = 1
    for i in range (len(x)):
        search.printReser(root, x[i][:], j)
        j = j + 1
    mydb.commit()
    mydb.close()

def qmakeRev(id,arr,check,checkin,checkout,totAmount):
    ida = str(tuple(id))
    ida = ida.replace(')', '')
    ida = ida.replace(',', '')
    ida = ida.replace('(', '')
    if check == 1:
        mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975", database='project_db20_up1046975')
        mycursor = mydb.cursor()
        strn = "insert into PAYMENT (amount_per_day, total_amount , amount_left , deposit, payment_type, billing_address) values " \
               "(" + str(arr[-6]) +  "," + str(totAmount) + " ,0 , 0 ," + '\'' + arr[-1]  + '\'' + " , " + '\'' +  arr[-2] + '\'' + " )"
        mycursor.execute(strn)
        strn = "insert into RESERVATION ( reservation_date, check_in, check_out, real_check_in, real_check_out, r_id_payment,r_id_hotel,r_id_roomType) values " \
              "( curdate() , " + checkin + " , " + checkout + " , " + checkin + " , " + checkout + " , last_insert_id() , " + str(arr [-4])  + " , " + str(arr[-3]) + ")"
        mycursor.execute(strn)
        strn = "insert into `MAKE` (m_id_guest, m_id_reservation) values ( " + ida + "  , last_insert_id() )"
        mycursor.execute(strn)
        strn = "select NOreservations  from GUEST where id_guest =" + ida
        mycursor.execute(strn)
        x = mycursor.fetchall()
        strn = "update GUEST set NOreservations = " + str(x[0][0]+1) +  " where id_guest =  " + ida
        mycursor.execute(strn)
    else:
        deposit = totAmount * 20 / 100
        amountLeft = totAmount - deposit
        mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975",database='project_db20_up1046975')
        mycursor = mydb.cursor()
        strn = "insert into PAYMENT (amount_per_day, total_amount , amount_left , deposit, payment_type, billing_address) values " \
               "(" + str(arr[-6]) +  "," + str(totAmount) + ", " +  str(amountLeft)+ "," + str(deposit) + ' , \'' + arr[-1]  + '\'' + " , " + '\'' +  arr[-2] + '\'' + " )"
        mycursor.execute(strn)
        strn = "insert into RESERVATION ( reservation_date, check_in, check_out, real_check_in, real_check_out, r_id_payment,r_id_hotel,r_id_roomType) values " \
              "( curdate() , " + checkin + " , " + checkout + " , " + checkin + " , " + checkout + " , last_insert_id() , " + str(arr [-4])  + " , " + str(arr[-3]) + ")"
        mycursor.execute(strn)
        strn = "insert into `MAKE` (m_id_guest, m_id_reservation) values ( " + ida + "  , last_insert_id() )"
        mycursor.execute(strn)
        strn = "select NOreservations  from GUEST where id_guest =" + ida
        mycursor.execute(strn)
        for x in mycursor:
            strn = "update GUEST set NOreservations = " + str(x[0]+1) + " where id_guest =  " + ida
            mycursor.execute(strn)

    mydb.commit()
    mydb.close()


#OWNER
def qcheckOwner(id):
    ida = str(tuple(id))
    ida = ida.replace(')', '')
    ida = ida.replace(',', '')
    ida = ida.replace('(', '')
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975",database='project_db20_up1046975')
    mycursor = mydb.cursor()
    strn = "select id_owner from OWNER where id_owner = " +ida
    mycursor.execute(strn)
    x = mycursor.fetchall()
    if x != []:
        return 1
    else:
        return 0

def qshowOwnerHotels(id):
    root = search.showOwnerHotels()
    ida = str(tuple(id))
    ida = ida.replace(')', '')
    ida = ida.replace(',', '')
    ida = ida.replace('(', '')
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975",database='project_db20_up1046975')
    mycursor = mydb.cursor()
    strn = " select h.name , h.stars ,h.country,h.city,h.address , h.id_hotel " \
           " from MANAGE m  " \
           " join OWNER o on o.id_owner = m.m_id_owner " \
           " join HOTEL h on h.id_hotel = m.m_id_hotel where id_owner = " + ida
    mycursor.execute(strn)
    j = 2
    for x in mycursor:
        search.printOwnerHotels(root,x,j)
        j = j + 1
    mydb.commit()
    mydb.close()
def qshowAvailableRooms(idHotel):
    root = search.showAvailableRooms()
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975",database='project_db20_up1046975')
    mycursor = mydb.cursor()
    strn = "SELECT  DISTINCT  rt.id_roomType, qty as total,qty - count(*) as available ,price,id_hotel" \
           " from HOTEL h " \
           " join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel " \
           " join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType " \
           " join RESERVATION r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType  " \
           " where ( h.id_hotel = " + str(idHotel) + " and ( ( CURDATE() >=r.real_check_in and CURDATE() <=r.real_check_out))) " \
           " group by hr.hr_id_roomType , total , qty , price , id_hotel having available>0 " \
           " UNION SELECT  DISTINCT  rt.id_roomType, qty as total,qty as available ,price,id_hotel from HOTEL h " \
           " join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel " \
           " join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType " \
           " where h.id_hotel = " + str(idHotel) + " and  rt.id_roomType  not in(select r.r_id_roomType from RESERVATION r where hr.hr_id_hotel=r.r_id_hotel and  rt.id_roomType = r.r_id_roomType) " \
           " UNION SELECT  DISTINCT  rt.id_roomType, qty as total,qty as available ,price,id_hotel" \
           " from HOTEL h join HOTEL_ROOMS hr on h.id_hotel = hr.hr_id_hotel " \
           " join ROOM_TYPE rt on hr.hr_id_roomType = rt.id_roomType " \
           " join RESERVATION r on hr.hr_id_hotel=r.r_id_hotel and hr.hr_id_roomType = r.r_id_roomType  " \
           " where ( h.id_hotel=" + str(idHotel) + " and (  CURDATE() < r.real_check_in or  CURDATE()> r.real_check_out) )"
    mycursor.execute(strn)
    j = 2
    for x in mycursor:
        search.printAvailableRooms(root,x,j)
        j = j + 1
    mydb.commit()
    mydb.close()
def qshowRoomInfo(idRoom):
    root = search.RoomInfo()
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975",database='project_db20_up1046975')
    mycursor = mydb.cursor()
    strn = "select rt.capacity , rt.suite,rt.pool,rt.hot_tub,rt.smokers,rt.kitchen,rt.bar from ROOM_TYPE rt where id_roomType = " + str(idRoom)
    mycursor.execute(strn)
    j = 2
    for x in mycursor:
        search.printRoomInfo(root,x,j)
        j = j + 1
    mydb.commit()
    mydb.close()
def qupdatePrevRoom(idHot,idRoom,qty,price):
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975",database='project_db20_up1046975')
    mycursor = mydb.cursor()
    strn = "update HOTEL_ROOMS set qty= " + qty + ", price = " + price + " where hr_id_hotel= " + str(idHot) + " and hr_id_roomType = " + str(idRoom)
    mycursor.execute(strn)
    mydb.commit()
    mydb.close


#Hotel Addition
def qaddHotel(id,country,city,address,stars,name):
    ida = str(tuple(id))
    ida = ida.replace(')', '')
    ida = ida.replace(',', '')
    ida = ida.replace('(', '')
    country = '\'' + country + '\''
    city = '\'' + city + '\''
    address = '\'' + address + '\''
    name = '\'' + name + '\''

    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975",database='project_db20_up1046975')
    mycursor = mydb.cursor()
    if (qcheckOwner(id) == 0):
        strn = "insert into OWNER (id_owner) values ( " + ida + " ) ;"
        mycursor.execute(strn)
    strn = "insert into HOTEL (country, city, address, stars, name) values " \
           " ( " + country + "," + city + "," + address + ","  + stars + "," + name + ");"
    mycursor.execute(strn)
    strn = "select last_insert_id();"
    mycursor.execute(strn)
    id = mycursor.fetchall()
    hid = str(tuple(id))
    hid = hid.replace(')', '')
    hid = hid.replace(',', '')
    hid = hid.replace('(', '')
    mycursor = mydb.cursor()
    strn = "insert into `MANAGE` (m_id_owner, m_id_hotel) values ( " + ida + " , last_insert_id() ) ;"
    mycursor.execute(strn)
    mydb.commit()
    mydb.close()
    return hid
def qcheckRoomType(capac,suite,pool,hot_tub,smokers,kitchen,bar):
    suite = '\'' + suite + '\''
    pool = '\'' + pool + '\''
    hot_tub = '\'' + hot_tub + '\''
    smokers = '\'' + smokers + '\''
    kitchen = '\'' + kitchen + '\''
    bar = '\'' + bar + '\''
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975",database='project_db20_up1046975')
    mycursor = mydb.cursor()
    strn = "select id_roomType from ROOM_TYPE where capacity = " + capac + " and suite = " + suite + " and pool = " + pool + " and hot_tub = " \
            +hot_tub+ " and smokers = " + smokers + " and kitchen = " + kitchen + " and bar = " + bar
    mycursor.execute(strn)
    x = mycursor.fetchall()
    if x != []:
        id = x[0]
        ida = str(tuple(id))
        ida = ida.replace(')', '')
        ida = ida.replace(',', '')
        ida = ida.replace('(', '')
        mydb.commit()
        mydb.close()
        return ida
    else:
        mydb.commit()
        mydb.close()
        return 0
def qaddRoom(hotid,check,capac,suite,pool,hot_tub,smokers,kitchen,bar,qty,price):
    suite1 = '\'' + suite + '\''
    pool1 = '\'' + pool + '\''
    hot_tub1 = '\'' + hot_tub + '\''
    smokers1 = '\'' + smokers + '\''
    kitchen1 = '\'' + kitchen + '\''
    bar1 = '\'' + bar + '\''
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975",database='project_db20_up1046975')
    if (check == 0 ):
        mycursor = mydb.cursor()
        strn = "insert into `ROOM_TYPE`  (capacity,suite, pool, hot_tub, smokers, kitchen, bar) values " \
               " ( " + str(capac) + " , " + suite1 + " , " + pool1 + " , " + hot_tub1 + " , " + smokers1 + " , " + kitchen1 + " , " + bar1 + " ); "
        mycursor.execute(strn)
        mydb.commit()
        id = qcheckRoomType(capac,suite,pool,hot_tub,smokers,kitchen,bar)
        print(hotid, id)
        mycursor = mydb.cursor()
        strn = "insert into `HOTEL_ROOMS` (hr_id_hotel,hr_id_roomType,QTY, price) values " \
               " ( last_insert_id() , "  + str(id) + " , " + qty + " , " + price + " ) ;"
        mycursor.execute(strn)
    else :

        print(hotid,check)
        mycursor = mydb.cursor()
        strn = "insert into `HOTEL_ROOMS` (hr_id_hotel,hr_id_roomType,QTY, price) values " \
               " ( " +str(hotid)+ " , "   + str(check) + " , " + qty + " , " + price + " ) ;"
        mycursor.execute(strn)
    mydb.commit()
    mydb.close()

def qcheckHotRoom(hotid,roomid):
    mydb = mysqlc.connect(host="150.140.186.221", user="db20_up1046975", password="up1046975",database='project_db20_up1046975')
    mycursor = mydb.cursor()
    strn = "select hr_id_roomType from HOTEL_ROOMS where hr_id_hotel =" + str(hotid) + " and hr_id_roomType = " + str(roomid)
    mycursor.execute(strn)
    x=mycursor.fetchall()
    if x != []:
        return 1
    else:
        return 0