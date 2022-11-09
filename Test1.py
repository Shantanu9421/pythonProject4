from tkinter import *
import sqlite3
from tkinter import messagebox
import random as rd
import smtplib


def major():
    base = Tk()
    base.geometry("800x600")
    base.title("Welcome to banking backup")
    base.configure(bg='#856ff8')
    fon = ("Arial", 10)
    db = []

    def method_1():
        try:
            con = sqlite3.connect("Bank.db")
            quary = "Create table customer (customer_id primary key,Name,mobile,Addhar,Email VARCHAR,Balance)"
            con.execute(quary)
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Table created successfully")

        except:
            messagebox.showinfo("Error", "Table Already Created")

    def method_2():
        base.destroy()

        def data():
            en = ent.get()
            en1 = ent1.get()
            en2 = ent2.get()
            en3 = ent3.get()
            acc = rd.randint(10000000000, 99999999999)
            acc_in = str(acc)
            try:
                con = sqlite3.connect("Bank.db")
                q = "insert into customer(customer_id,Name,Mobile,Addhar,Email,Balance) values (" + acc_in + ",'" + en \
                    + "'," + en1 + "," + en2 + ",'" + en3 + "'," + "0" + ")"
                con.execute(q)
                con.commit()
                messagebox.showinfo("DATA", "INFO ADD SUCCESSFULLY")
                messagebox.showinfo("Account number :", en + " Account number is :" + acc_in)
                base1.destroy()
                con.close()

            except:
                messagebox.showinfo("Error", "Data was not enter properly")

        def data3():
            ent.delete(0, "end")
            ent1.delete(0, "end")
            ent2.delete(0, "end")
            ent3.delete(0, "end")
            ent.focus()

        def back():
            base1.destroy()
            major()

        base1 = Tk()
        base1.geometry("800x600")
        base1.title("Welcome to form")
        lab = Label(font=fon, text="Enter full name :")
        lab.place(x=250, y=70)
        ent = Entry()
        ent.place(x=350, y=75)
        lab1 = Label(font=fon, text="Mobile number :")
        lab1.place(x=250, y=120)
        ent1 = Entry()
        ent1.place(x=350, y=120)
        lab2 = Label(font=fon, text="Aaddhar card :")
        lab2.place(x=250, y=170)
        ent2 = Entry()
        ent2.place(x=350, y=170)
        lab2 = Label(font=fon, text="Email :")
        lab2.place(x=250, y=220)
        ent3 = Entry()
        ent3.place(x=350, y=220)
        but = Button(text="save", command=data)
        but.place(x=350, y=250)
        bu1 = Button(text="Reset", command=data3)
        bu1.place(x=400, y=250)
        but5 = Button(base1, text="<--", command=back)
        but5.place(x=1, y=1)
        base1.mainloop()

    def method_3():
        base.destroy()
        base1 = Tk()
        base1.geometry("800x600")
        base1.title("Welcome back")

        def data2():
            entr = ent.get()
            entr1 = ent1.get()
            bu['state'] = DISABLED
            try:
                con = sqlite3.connect("Bank.db")
                cur = con.cursor()
                q = "select customer_id,Name,mobile,Addhar,Email,Balance from customer where Name='" + entr \
                    + "'and mobile=" + entr1
                cur.execute(q)
                data = cur.fetchall()

                flat = [element for d in data for element in d]

                if flat == db:
                    messagebox.showinfo("Error", "No Such data Found")
                    ent.delete("0", "end")
                    ent1.delete("0", "end")
                    ent.focus()
                    bu['state'] = NORMAL
                else:
                    dat = str(flat[0])
                    da = str(flat[1])
                    da1 = str(flat[2])
                    da2 = str(flat[3])
                    da3 = str(flat[5])
                    da4 = str(flat[4])

                    txt3.insert(0, da)
                    txt4.insert(0, da1)
                    txt5.insert(0, da2)
                    txt6.insert(0, da3)
                    txt7.insert(0, dat)
                    txt8.insert(0, da4)

                cur.close()
                con.close()

            except:
                messagebox.showinfo("Error", "Data was not enter properly")

        def data3():
            ent.delete("0", "end")
            ent1.delete("0", "end")
            txt3.delete("0", "end")
            txt4.delete("0", "end")
            txt5.delete("0", "end")
            txt6.delete("0", "end")
            txt7.delete("0", "end")
            txt8.delete("0", "end")
            ent.focus()
            bu['state'] = NORMAL

        def back():
            base1.destroy()
            major()

        txt = Label(text="Enter your name :")
        txt.place(x=250, y=70)
        ent = Entry()
        ent.place(x=370, y=75)
        txt1 = Label(text="Enter mobile number :")
        txt1.place(x=240, y=120)
        ent1 = Entry()
        ent1.place(x=370, y=120)
        bu = Button(text="Submit", command=data2)
        bu.place(x=400, y=150)
        lab3 = Label(text="Name : ")
        lab3.place(x=250, y=200)
        txt3 = Entry()
        txt3.place(x=370, y=200)
        lab1 = Label(text="Mobile number : ")
        lab1.place(x=250, y=250)
        txt4 = Entry()
        txt4.place(x=370, y=250)
        lab3 = Label(text="Addhar : ")
        lab3.place(x=250, y=300)
        txt5 = Entry()
        txt5.place(x=370, y=300)
        lab4 = Label(text="Balance : ")
        lab4.place(x=250, y=350)
        txt6 = Entry()
        txt6.place(x=370, y=350)
        lab5 = Label(text="Account number : ")
        lab5.place(x=250, y=400)
        txt7 = Entry()
        txt7.place(x=370, y=400)
        lab6 = Label(text="Email :")
        lab6.place(x=250, y=450)
        txt8 = Entry()
        txt8.place(x=370, y=450)
        bu1 = Button(text="Reset", command=data3)
        bu1.place(x=400, y=500)
        bu2 = Button(base1, text="<--", command=back)
        bu2.place(x=1, y=1)
        base1.mainloop()

    def method_4():
        base.destroy()
        base1 = Tk()
        base1.geometry("800x600")
        base1.title("Delete menu")

        def check_db():
            try:
                con = sqlite3.connect("Bank.db")
                gta = ent.get()
                gta1 = ent1.get()
                q = "Delete from customer where Name='" + gta + "'and Mobile=" + gta1
                con.execute(q)
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Data was deleted")
                ent.delete("0", "end")
                ent1.delete("0", "end")
                ent.focus()

            except:
                messagebox.showinfo("Error", "Data was not enter properly")

        def reset():
            ent.delete("0", "end")
            ent1.delete("0", "end")
            ent.focus()

        def back():
            base1.destroy()
            major()

        lab = Label(base1, text="Enter Name : ")
        lab.place(x=250, y=70)
        ent = Entry()
        ent.place(x=330, y=73)
        lab1 = Label(base1, text="Enter mobile : ")
        lab1.place(x=250, y=120)
        ent1 = Entry()
        ent1.place(x=330, y=123)
        bu = Button(text="Enter", command=check_db)
        bu.place(x=330, y=155)
        bu1 = Button(text="Reset", command=reset)
        bu1.place(x=380, y=155)
        bu2 = Button(base1, text="<--", command=back)
        bu2.place(x=1, y=1)
        base1.mainloop()

    def method_5():

        server = smtplib.SMTP_SSL("smtp.gmail.com", 535)
        server.login("tempshantanu@gmail.com", "Pass@#1234")
        server.sendmail("tempshantanu@gmail.com", "sohamkharadkar123@gmail.com", "Hello, This mail is created by bank ")
        server.quit()

    but1 = Button(base, text="Create Table", font=fon, command=method_1)
    but1.pack()
    but2 = Button(base, text="New customer", font=fon, command=method_2)
    but2.pack()
    but3 = Button(base, text="Already Exist", command=method_3)
    but3.pack()
    but4 = Button(base, text="Delete Customer", command=method_4)
    but4.pack()
    but5 = Button(base, text="Send mail", command=method_5)
    but5.pack()
    base.mainloop()


major()
