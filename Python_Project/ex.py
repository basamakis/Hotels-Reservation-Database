from tkinter import *
from tkinter import ttk
import queries as que
from tkinter import messagebox



root = Tk()
root.title('Add Hotel')


def back():
    root.destroy()



Label(root, text='Hotel Name', font=('Arial', '12', 'bold'),  width=13).grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)
Label(root, text='City', font=('Arial', '12', 'bold'),  width=13).grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)
Label(root, text='Address', font=('Arial', '12', 'bold'),  width=13).grid(row=2, column=0)
e3 = Entry(root)
e3.grid(row=2, column=1)
Label(root, text='Stars', font=('Arial', '12', 'bold'), width=13).grid(row=3, column=0)
e4 = Entry(root)
e4.grid(row=3, column=1)
Label(root, text='Name', font=('Arial', '12', 'bold'),  width=13).grid(row=4, column=0)
e4 = Entry(root)
e4.grid(row=4, column=1)
Button(root, text='Back', command=back, bg='red').grid(row=5, column=0)
Button(root, text='Submit', width=15).grid(row=5, column=1)
root.mainloop()