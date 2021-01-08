from tkinter import *
from tkinter import ttk
import queries as que
from tkinter import messagebox


gid = ''    # USER ID
hid = ''    # Hotel ID

#User Profile
def profile(id):
    global gid
    gid=id
    root = Tk()
    root.title("USER PROFILE")

    root.resizable(FALSE, FALSE)

    root.iconbitmap('dbic.ico')
    Label(root, text='Welcome : ', font=('Arial', '12','bold')).grid(row=0, column=0)
    Label(root, text='Name : ', font=('Arial', '12','bold')).grid(row=1, column=0)
    Label(root, text='Surname : ', font=('Arial', '12','bold')).grid(row=2, column=0)
    Label(root, text='Number of Reservations : ', font=('Arial', '12','bold')).grid(row=3, column=0)


    def search():
        root.destroy()
        StartingScreen()
    def checkRes():
        root.destroy()
        que.qshowRes(id)
    def manHot():
        root.destroy()
        que.qshowOwnerHotels(gid)
    def addHot():
        root.destroy()
        addHotel()


    Button(root, text='Search', width = 20 ,command=search,bg='gray25').grid(row=5, column=0)
    Button(root, text='Old  Reservations', width = 20, command=checkRes , bg='gray25').grid(row=5, column=2)
    check = que.qcheckOwner(id)
    Label(root, width = 20).grid(row=6, column=2)
    Button(root, text='Add Hotel', width=20, bg='skyblue4',command=addHot).grid(row=7, column=0)
    if check == 1:
        Button(root, text='Manage Hotels', width=20, bg='skyblue4',command=manHot).grid(row=7,column=2)
    return root
def printInfo(root,arr,ro):
    Label(root, text=str(arr[0]), font=('Arial', '12'), width=10, fg='purple3').grid(row=0, column=ro)
    for i in range(1, len(arr)):
        Label(root, text=str(arr[i]), font=('Arial', '12'), width=10).grid(row=i, column=ro)

#Starting Screen of Search
def StartingScreen():
    root = Tk()
    root.geometry("250x150")
    root.resizable(FALSE, FALSE)
    root.iconbitmap('dbic.ico')

    frame1 = Frame(root)
    frame1.pack(fill=X)
    lbl1 = Label(frame1, text="Country:",width = 8, font=('Arial' , '12')).pack(side = LEFT)
    e1 = Entry(frame1)
    e1.pack(padx=5,pady=5)


    frame2 = Frame(root)
    frame2.pack(fill=X)
    lbl2 = Label(frame2, text="City:",width=8 , font=('Arial' , '12')).pack(side=LEFT)
    e2 = Entry(frame2)
    e2.pack(padx=5,pady=5)


    frame3 = Frame(root)
    frame3.pack(fill=X)
    lbl3 = Label(frame3, text="Check in: ",width = 8,font=('Arial' , '12')).pack(side=LEFT)
    e3 = Entry(frame3)
    e3.pack(padx=5,pady=5)


    frame4 = Frame(root)
    frame4.pack(fill=X)
    lbl4 = Label(frame4, text="Check out:",width = 8 ,font=('Arial' , '12')).pack(side=LEFT)
    e4 = Entry(frame4)
    e4.pack(padx=5,pady=5)

    def search():
        country = e1.get()
        city = e2.get()
        checkin = e3.get()
        checkout = e4.get()
        root.destroy()
        que.availRoom(checkin,country,city,checkout,0)

    def back():
        root.destroy()
        que.qprof(gid)
    b0 = Button(root,command = back ,text='Back' , bg = 'red').pack(side=LEFT)
    b1 = Button(root,text = 'Search',command = search).pack(side=LEFT)

    root.mainloop()
    return root


#Template of Hotels and Rooms
def hotelTemplate(country,city,checkin,checkout):
    root = Tk()
    root.resizable(FALSE, FALSE)
    root.iconbitmap('dbic.ico')
    root.configure(bg='gray76')
    var1, var2, var3, var4, var5, var6 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()

    Label(root, text='Hotel Name', font=('Arial', '12'), bg='grey', width=10).grid(row=1, column=0)
    Label(root, text='Stars', font=('Arial', '12'), bg='grey', width=10).grid(row=1, column=1)

    com = ttk.Combobox(root, values=['1', '2', '3','4','5','6'], width=5)
    com.grid(row=0, column=2)
    Label(root, text='Room Capacity', font=('Arial', '12'), bg='grey', width=12).grid(row=1, column=2)

    Checkbutton(root, text='Suite', variable=var1, onvalue=1, offvalue=0).grid(row=0, column=3)
    Label(root, text='Suite', font=('Arial', '12'), bg='grey', width=10).grid(row=1, column=3)

    Checkbutton(root, text='Pool', variable=var2, onvalue=1, offvalue=0).grid(row=0, column=4)
    Label(root, text='Pool', font=('Arial', '12'), bg='grey', width=10).grid(row=1, column=4)

    Checkbutton(root, text='Hot Tub', variable=var3, onvalue=1, offvalue=0).grid(row=0, column=5)
    Label(root, text='Hot Tub', font=('Arial', '12'), bg='grey', width=10).grid(row=1, column=5)

    Checkbutton(root, text='Smokers', variable=var4, onvalue=1, offvalue=0).grid(row=0, column=6)
    Label(root, text='Smokers', font=('Arial', '12'), bg='grey', width=10).grid(row=1, column=6)

    Checkbutton(root, text='Kitchen', variable=var5, onvalue=1, offvalue=0).grid(row=0, column=7)
    Label(root, text='Kitchen', font=('Arial', '12'), bg='grey', width=10).grid(row=1, column=7)

    Checkbutton(root, text='Bar', variable=var6, onvalue=1, offvalue=0).grid(row=0, column=8)
    Label(root, text='Bar', font=('Arial', '12'), bg='grey', width=10).grid(row=1, column=8)


    Label(root, text='Room Price', font=('Arial', '12'), bg='grey', width=10).grid(row=1, column=9)
    e1=ttk.Combobox(root,text='Max/Min Value', values=['10-50', '50-100', '100-200','200-500','500-'], width=5)
    e1.grid(row=0,column=9)

    Label(root, text='Total Amount', font=('Arial', '12'), bg='grey', width=10).grid(row=1, column=10)
    def submit():
        pref=['','','','','','']
        prRange = e1.get()
        prRange = prRange.split('-')
        capac = com.get()
        if var1.get() == 1:
            pref[0]=('\'' + 'YES' + '\'')

        if var2.get() == 1:
            pref[1] = ('\'' + 'YES' + '\'')

        if var3.get() == 1:
            pref[2] = ('\'' + 'YES' + '\'')

        if var4.get() == 1:
            pref[3] = ('\'' + 'YES' + '\'')

        if var5.get() == 1:
            pref[4] = ('\'' + 'YES' + '\'')

        if var6.get() == 1:
            pref[5] = ('\'' + 'YES' + '\'')
        root.destroy()
        que.availRoomPref(checkin,country,city,checkout,capac,prRange,pref)
    def back():
        root.destroy()
        StartingScreen()
    Button(root, text='Submit', command=submit).grid(row=0,column=1)
    Button(root, text='Back', command=back,bg='red').grid(row=0, column=0)
    return root
def printHotels(root,arr,ro,checkin,checkout,totAmount):
    Label(root, text=str(arr[0]), font=('Arial', '12'), width=10,fg='OrangeRed3').grid(row=ro, column=0)
    for i in range(1, (len(arr) - 3)):
        Label(root, text=str(arr[i]), font=('Arial', '10'), width=5).grid(row=ro, column=i)
    Label(root, text=str(totAmount), font=('Arial', '10'), width=5).grid(row=ro, column=i+1)
    def reser():
        m = messagebox.askokcancel("Reservation", "Proceed to payment?")
        if m:
            lArr=list(arr)
            payScreen(lArr,checkin,checkout,totAmount)

    Button(root,text='Make Reservation',font=('Arial','10'),width=13,bg='gray25',fg='white',command=reser).grid(row=ro, column=len(arr)-1)



#Show User Reservations
def showRev():
    root = Tk()
    f1 = Frame(root)
    f1.grid(row=0, column=0, sticky="nsew")
    def back():
        root.destroy()
        que.qprof(gid)
    b1 = Button(f1, text='Back', width = 4, command=back,bg='red')
    b1.pack(side=LEFT)
    l1 = Label(f1, text='Hotel Name', font=('Arial', '10', 'bold'), bg='grey', width=13)
    l1.pack(side=LEFT)
    Label(root, text='Persons', font=('Arial', '10', 'bold'), bg='grey', width=13).grid(row=0, column=1)
    Label(root, text='Reservation Date', font=('Arial', '10', 'bold'), bg='grey', width=13).grid(row=0, column=2)
    Label(root, text='Check In', font=('Arial', '10', 'bold'), bg='grey', width=13).grid(row=0, column=3)
    Label(root, text='Check Out', font=('Arial', '10', 'bold'), bg='grey', width=13).grid(row=0, column=4)
    Label(root, text='Remaining Amount', font=('Arial', '10', 'bold'), bg='grey', width=14).grid(row=0, column=5)
    Label(root, text='Deposit', font=('Arial', '10', 'bold'), bg='grey', width=13).grid(row=0, column=6)
    Label(root, text='Reservation Price', font=('Arial', '10', 'bold'), bg='grey', width=13).grid(row=0, column=7)
    return root
def printReser(root,arr,ro) :
    Label(root, text=str(arr[0]), font=('Arial', '12'), width=10, fg='OrangeRed3').grid(row=ro, column=0)
    for i in range(1, len(arr)):
        Label(root, text=str(arr[i]), font=('Arial', '12'), width=10).grid(row=ro, column=i)
#Create Reservation
def payScreen(lArr,checkin,checkout,totAmount):
    root = Tk()

    root.iconbitmap('dbic.ico')

    Label(root, text="Payment Method", width=14, font=('Arial', '12')).grid(row=0, column=0,columnspan=2)
    com = ttk.Combobox(root, values=['DEBIT CARD', 'PAYPAL', 'BANK ACCOUNT'], width=13)
    com.grid(row=0, column=2)
    Label(root, text="Billing Address", width=14, font=('Arial', '12')).grid(row=1, column=0,columnspan=2)
    e = Entry(root, width=16)
    e.grid(row=1, column=2)

    def payFull():
        lArr.append(e.get())
        lArr.append(com.get())
        root.destroy()
        messagebox.showinfo('Reservation Suceed','Reservation Suceed')
        que.qmakeRev(gid,lArr,1,checkin,checkout,totAmount)

    def payDep():
        lArr.append(e.get())
        lArr.append(com.get())
        root.destroy()
        messagebox.showinfo('Reservation Suceed', 'Reservation Suceed')
        que.qmakeRev(gid, lArr, 0, checkin, checkout, totAmount)

    Label(root , text= "Amount" , font=('Arial', '12')).grid(row=2, column=0)
    Label(root , text= str(totAmount*1.0) + "€" , font=('Arial', '14','bold')).grid(row=2, column=2)
    Button (root, text = 'Pay Now' ,width=14,font=('Arial', '12','bold'),command = payFull ).grid(row=4, column=0)
    Label(root , text ='or' , width = 4 ,font=('Arial', '12')).grid(row=4, column=1)
    Button(root, text="Give Deposit", width=14, font=('Arial', '12','bold'),command = payDep).grid(row=4, column=2)
    Label(root, text='20 % : ', font=('Arial', '12')).grid(row=4, column=3)
    Label(root, text=str(totAmount * 20 / 100) + "€", font=('Arial', '14', 'bold')).grid(row=4, column=4)
    root.mainloop()



## OWNER

#Show Owner Hotels
def showOwnerHotels():
    root = Tk()
    f1 = Frame(root)
    f1.grid(row=0, column=0, sticky="nsew")
    def back():
        root.destroy()
        que.qprof(gid)
    b1 = Button(f1, text='Back', command=back,bg='red')
    b1.pack(side=LEFT)
    l1 = Label(f1, text='Hotel Name', font=('Arial', '12', 'bold'), bg='grey', width=13)
    l1.pack(side=LEFT)
    Label(root, text='Stars', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=0, column=1)
    Label(root, text='Country', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=0, column=2)
    Label(root, text='City', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=0, column=3)
    Label(root, text='Address', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=0, column=4)
    Label(root, text='12 Month Plentity', font=('Arial', '12', 'bold'), bg='grey', width=20).grid(row=0, column=5)
    return root
def printOwnerHotels(root,arr,ro) :
    def ManRoom():
        root.destroy()
        que.qshowAvailableRooms(arr[-1])
    Label(root, text=str(arr[0]), font=('Arial', '12'), width=10, fg='OrangeRed3').grid(row=ro, column=0)
    for i in range(1, len(arr)-1):
        Label(root, text=str(arr[i]), font=('Arial', '12'), width=20).grid(row=ro, column=i)
    plen = que.qHotelPlen(arr[-1])
    Label(root, text=str(plen) + '%', font=('Arial', '12'), width=10).grid(row=ro, column=i+1)
    Button(root, text='Manage Rooms', font=('Arial', '12'), width=20,bg='gray25',fg='white',command=ManRoom).grid(row=ro, column=i+2)

#Manage Rooms
def showAvailableRooms():
    root = Tk()
    f1 = Frame(root)
    f1.grid(row=0, column=0, sticky="nsew")
    def back():
        root.destroy()
        que.qshowOwnerHotels(gid)
    def add():
        root.destroy()
        addRoom(1)

    b1 = Button(f1, text='Back', command=back,bg='red')
    b1.pack(side=LEFT)
    l1 = Label(f1, text='Room ID', font=('Arial', '12', 'bold'), bg='grey', width=13)
    l1.pack(side=LEFT)
    Label(root, text='Total Rooms', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=0, column=1)
    Label(root, text='Available Rooms', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=0, column=2)
    Label(root, text='Price', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=0, column=3)
    Button(root,text='Add Room',bg='skyblue',command=add).grid(row=0,column=4)
    return root
def printAvailableRooms(root,arr,ro) :
    global hid
    hid = arr[-1]
    roomid = arr[0]
    def RoomInf():
        root.destroy()
        que.qshowRoomInfo(roomid)
    Label(root, text=str(arr[0]), font=('Arial', '12'), width=10, fg='OrangeRed3').grid(row=ro, column=0)
    def add():
        root.destroy()
    for i in range(1, len(arr)-1):
        Label(root, text=str(arr[i]), font=('Arial', '12'), width=20).grid(row=ro, column=i)
    Button(root, text='More Info', font=('Arial', '12'), width=20,bg='gray25',fg='white',command=RoomInf).grid(row=ro, column=i+1)

#Room Info
def RoomInfo():
    root = Tk()
    def back():
        root.destroy()
        que.qshowAvailableRooms(hid)
    b1 = Button(root, text='Back', command=back,bg='red').grid(row=0,column=0)
    l1 = Label(root, text='Capacity', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=1, column=1)
    Label(root, text='Suite', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=2, column=1)
    Label(root, text='Pool', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=3, column=1)
    Label(root, text='Hot Tub', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=4, column=1)
    Label(root, text='Smokers', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=5, column=1)
    Label(root, text='Kitchen', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=6, column=1)
    Label(root, text='Bar', font=('Arial', '12', 'bold'), bg='grey', width=13).grid(row=7, column=1)
    return root
def printRoomInfo(root,arr,ro):
    for i in range(1, len(arr)+1):
        Label(root, text=str(arr[i-1]), font=('Arial', '12'), width=20).grid(row=i, column=ro)

#Add Hotel
def addHotel():
    root = Tk()
    root.title('Add Hotel')
    def back():
        root.destroy()
        que.qprof(gid)

    def submit():
        global hid
        country = e1.get()
        city = e2.get()
        address = e3.get()
        stars = e4.get()
        name = e5.get()
        root.destroy()
        hid = que.qaddHotel(gid, country, city, address, stars, name)
        addRoom(0)

    Label(root, text='Country', font=('Arial', '12', 'bold'), width=13).grid(row=0, column=0)
    e1 = Entry(root)
    e1.grid(row=0, column=1)
    Label(root, text='City', font=('Arial', '12', 'bold'), width=13).grid(row=1, column=0)
    e2 = Entry(root)
    e2.grid(row=1, column=1)
    Label(root, text='Address', font=('Arial', '12', 'bold'), width=13).grid(row=2, column=0)
    e3 = Entry(root)
    e3.grid(row=2, column=1)
    Label(root, text='Stars', font=('Arial', '12', 'bold'), width=13).grid(row=3, column=0)
    e4 = Entry(root)
    e4.grid(row=3, column=1)
    Label(root, text='Name', font=('Arial', '12', 'bold'), width=13).grid(row=4, column=0)
    e5 = Entry(root)
    e5.grid(row=4, column=1)
    Button(root, text='Back', command=back, bg='red').grid(row=5, column=0)
    Button(root, text='Submit', width=15,command=submit).grid(row=5, column=1)

def addRoom(check):
    root = Tk()
    root.title('Add Room')
    Label(root, text='Capacity', font=('Arial', '12', 'bold'), width=13).grid(row=0, column=0)
    com1 = ttk.Combobox(root, values=['1', '2', '3', '4', '5', '6'], width=5)
    com1.grid(row=0, column=1)
    Label(root, text='Suite', font=('Arial', '12', 'bold'), width=13).grid(row=1, column=0)
    com2 = ttk.Combobox(root, values=['YES', 'NO'], width=5)
    com2.grid(row=1, column=1)
    Label(root, text='Pool', font=('Arial', '12', 'bold'), width=13).grid(row=2, column=0)
    com3 = ttk.Combobox(root, values=['YES', 'NO'], width=5)
    com3.grid(row=2, column=1)
    Label(root, text='Hot Tub', font=('Arial', '12', 'bold'), width=13).grid(row=3, column=0)
    com4 = ttk.Combobox(root, values=['YES', 'NO'], width=5)
    com4.grid(row=3, column=1)
    Label(root, text='Smokers', font=('Arial', '12', 'bold'), width=13).grid(row=4, column=0)
    com5 = ttk.Combobox(root, values=['YES', 'NO'], width=5)
    com5.grid(row=4, column=1)
    Label(root, text='Kitchen', font=('Arial', '12', 'bold'), width=13).grid(row=5, column=0)
    com6 = ttk.Combobox(root, values=['YES', 'NO'], width=5)
    com6.grid(row=5, column=1)
    Label(root, text='Bar', font=('Arial', '12', 'bold'), width=13).grid(row=6, column=0)
    com7 = ttk.Combobox(root, values=['YES', 'NO'], width=5)
    com7.grid(row=6, column=1)

    def add():
        capac = com1.get()
        suite = com2.get()
        pool = com3.get()
        hot_tub = com4.get()
        smokers = com5.get()
        kitchen = com6.get()
        bar = com7.get()
        Label(root, text='Quantity', font=('Arial', '12', 'bold'), width=13).grid(row=0, column=2)
        e1 = Entry(root)
        e1.grid(row=0, column=3)
        Label(root, text='Price', font=('Arial', '12', 'bold'), width=13).grid(row=1, column=2)
        e2 = Entry(root)
        e2.grid(row=1, column=3)

        def fill():
            qty = e1.get()
            price = e2.get()
            idRoom = que.qcheckRoomType(capac, suite, pool, hot_tub, smokers, kitchen, bar)
            check2 = que.qcheckHotRoom(hid,idRoom)
            if (check2==1):
                que.qupdatePrevRoom(hid,idRoom,qty,price)
            else:
                que.qaddRoom(hid, idRoom, capac, suite, pool, hot_tub, smokers, kitchen, bar, qty, price)

        Button(root, text='fill', width=15, command=fill).grid(row=7, column =2 )

    def back():
        if (check == 0) :
            root.destroy()
            addHotel()
        else:
            root.destroy()
            que.qshowAvailableRooms(hid)
    Button(root, text='Back', width=15, command=back,bg='red').grid(row=7, column=0)
    Button(root, text='Add Room', width=15, command=add).grid(row=7, column=1)
