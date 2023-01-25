from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
def from_kg():
    gram=float(e2_value.get())*1000
    pound=float(e2_value.get())*2.20462
    ounce=float(e2_value.get())*35.274


    t1.delete("1.0",END)
    t1.insert(END,gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END,ounce)

ttk.Label(frm, text="Kg").grid(column=0, row=0)
# ttk.Entry(frm).grid(column=1,row=0)
e2_value=StringVar()
e2=Entry(root,textvariable=e2_value)
e2.grid(row=0,column=1)
b1=Button(root, text="convert",command=from_kg)
b1.grid(row=0,column=2)
t1=Text(root,height=1,width=20)
t1.grid(row=1,column=0)
t2=Text(root,height=1,width=20)
t2.grid(row=1,column=1)
t3=Text(root,height=1,width=20)
t3.grid(row=1,column=2)
# ttk.Entry(frm).grid(column=1,row=1)
# b1=Button(root,text='converter')
# b1.grid(column=2,row=0)
root.mainloop()