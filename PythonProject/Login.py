from tkinter import *
from tkinter import ttk
import queries as que


###
#### REGISTRATION GUI #####
###
def reg():
    # LABELS AND ENTRIES OF REGISTRATION
    root = Tk()
    root.title('Registration')
    root.iconbitmap('C:/Users/fwtis/Downloads/DataBasesProject/Python_Project/venv/Include/dbic.ico')
    root.resizable(FALSE, FALSE)
    Label(root, text="Username:", width=13, font=('Arial', '12')).grid(row=0, column=0)
    e1 = Entry(root)
    e1.grid(row=0, column=1)
    Label(root, text="Password:", width=13, font=('Arial', '12')).grid(row=1, column=0)
    e2 = Entry(root, show='*')
    e2.grid(row=1, column=1)
    Label(root, text="F.Name:", width=13, font=('Arial', '12')).grid(row=2, column=0)
    e3 = Entry(root)
    e3.grid(row=2, column=1)
    Label(root, text="L.Name:", width=13, font=('Arial', '12')).grid(row=3, column=0)
    e4 = Entry(root)
    e4.grid(row=3, column=1)
    Label(root, text="Email:", width=13, font=('Arial', '12')).grid(row=4, column=0)
    e5 = Entry(root)
    e5.grid(row=4, column=1)
    Label(root, text="ID number:", width=13, font=('Arial', '12')).grid(row=5, column=0)
    e6 = Entry(root)
    e6.grid(row=5, column=1)
    Label(root, text="Phone Number:", width=13, font=('Arial', '12')).grid(row=6, column=0)
    e7 = Entry(root)
    e7.grid(row=6, column=1)
    Label(root, text="Country:", width=13, font=('Arial', '12')).grid(row=7, column=0)
    e8 = Entry(root)
    e8.grid(row=7, column=1)
    Label(root, text="Sex:", width=13, font=('Arial', '12')).grid(row=8, column=0)
    e9 = ttk.Combobox(root, values=['male', 'female', 'other'], width=5)
    e9.grid(row=8, column=1)
    Label(root, text="Address:", width=13, font=('Arial', '12')).grid(row=9, column=0)
    e10 = Entry(root)
    e10.grid(row=9, column=1)
    Label(root, text="Birthday:", width=13, font=('Arial', '12')).grid(row=10, column=0)
    e11 = Entry(root)
    e11.grid(row=10, column=1)

    # Sumbit Button function
    def adduser():
        username = e1.get()
        password = e2.get()
        fname = e3.get()
        lname = e4.get()
        email = e5.get()
        idnum = e6.get()
        pnum = e7.get()
        country = e8.get()
        sex = e9.get()
        addr = e10.get()
        birth = e11.get()
        y = que.adduser(username, password, fname, lname, email, idnum, pnum, country, sex, addr, birth)
        if (y == 0):
            Label(root, text="Registration Failed", font=('Arial', '12'), fg='red').grid(row=12, column=1)
        elif (y == 1):
            Label(root, text="Invalid Username", font=('Arial', '12'), fg='red').grid(row=11, column=1)
        else:
            root.destroy()
            log()

    def back():
        root.destroy()
        log()

    b = Button(root, text='Submit', width=13, command=adduser)
    b.grid(row=11, column=1)
    b1 = Button(root, text='Back', width=5, command=back, bg='red')
    b1.grid(row=11, column=2)


###
#### LOGIN GUI #####
###
def log():
    # LABELS AND ENTRIES OF LOGIN
    root = Tk()
    root.title('Login Screen')
    root.geometry('270x150')
    root.resizable(FALSE, FALSE)
    root.iconbitmap('C:/Users/fwtis/Downloads/DataBasesProject/Python_Project/venv/Include/dbic.ico')
    lbl1 = Label(root, text="Username:", font=('Arial', '12')).place(x=25, y=15)
    e1 = Entry(root)
    e1.place(x=120, y=18)
    lbl2 = Label(root, text="Password:", font=('Arial', '12')).place(x=25, y=55)
    e2 = Entry(root, show="*")
    e2.place(x=120, y=58)

    def login():
        username = e1.get()
        password = e2.get()
        id = que.qlogin(username, password)
        if id == 0:
            root.geometry('270x170')
            lb = Label(root, text='*Incorrect Username or Password*', fg='red', font=('Arial', '12'))
            lb.place(x=20, y=148)
        else:
            root.destroy()
            que.qprof(id)

    def register():
        root.destroy()
        reg()

    b1 = Button(root, text='Login', command=login)
    b1.place(x=120, y=88)
    b2 = Button(root, text='Register', command=register)
    b2.place(x=115, y=118)
    root.mainloop()



