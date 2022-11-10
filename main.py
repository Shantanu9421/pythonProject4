from tkinter import *
import sqlite3
from tkinter import messagebox


def major():
    db = []
    base = Tk()
    base.geometry("800x600")
    base.title("User inter face")
    ds = []

    def balance():
        base.destroy()
        base3 = Tk()
        base3.geometry("800x600")
        base3.title("User Face")

        def data():
            but['state'] = NORMAL
            ent.delete("0", "end")
            ent2.delete("0", "end")
            ent.focus()

        def method():
            qu = ent.get()
            but['state'] = DISABLED
            try:
                con = sqlite3.connect("Bank.db")
                q = "select Balance from customer where customer_id=" + qu
                cur = con.cursor()
                cur.execute(q)
                fet = cur.fetchall()
                pic = [element for d in fet for element in d]

                if pic == db:
                    messagebox.showinfo("Error", "Try again..check your data ")
                    but['state'] = NORMAL
                else:
                    ent2.insert(0, str(pic[0]))
                cur.close()
                con.close()

            except:
                messagebox.showinfo("ERROR", "DATA WAS NOT ENTER PROPERLY")

        def back():
            base3.destroy()
            major()

        lab = Label(text="Enter account number : ")
        lab.place(x=200, y=70)
        ent = Entry()
        ent.place(x=350, y=75)
        lab2 = Label(text="Balance")
        lab2.place(x=250, y=170)
        ent2 = Entry()
        ent2.place(x=350, y=173)
        but = Button(text="Save", command=method)
        but.place(x=350, y=205)
        bu1 = Button(text="Reset", command=data)
        bu1.place(x=400, y=205)
        but4 = Button(text="<--", command=back)
        but4.place(x=1, y=1)
        base3.mainloop()

    def withdraw():
        base.destroy()
        base2 = Tk()
        base2.title("Withdraw face")
        base2.geometry("800x600")

        def submit():
            but5["state"] = DISABLED
            gu = ent.get()
            gu1 = ent1.get()
            try:
                con = sqlite3.connect("Bank.db")
                cur = con.cursor()
                quart = "select Balance from customer where customer_id=" + gu
                cur.execute(quart)
                data = cur.fetchall()
                cur.close()
                con.close()

                if ds == data:
                    messagebox.showinfo("Error", "Incorrect data")
                else:
                    flat = [element for d in data for element in d]
                    da1 = int(flat[0])
                    da = int(gu1)
                    da1 = da1 - da
                    if flat[0] >= da:
                        con = sqlite3.connect("Bank.db")
                        da2 = str(da1)
                        quary = "update customer set Balance=" + da2 + " where customer_id=" + gu
                        con.execute(quary)
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Thank for banking")
                        reset()

                    else:
                        messagebox.showinfo("Error", "Insufficient Balance")
                        reset()
            except:
                messagebox.showinfo("ERROR",  "DATA WAS NOT ENTER PROPERLY")

        def reset():
            but5["state"] = NORMAL
            ent1.delete(0, "end")
            ent.delete(0, "end")
            ent.focus()

        def back():
            base2.destroy()
            major()

        lab = Label(base2, text="Enter Account number : ")
        lab.place(x=200, y=70)
        ent = Entry()
        ent.place(x=350, y=75)
        lab1 = Label(base2, text="Enter amount for withdraw : ")
        lab1.place(x=195, y=120)
        ent1 = Entry()
        ent1.place(x=350, y=125)
        but5 = Button(base2, text="Submit", command=submit)
        but5.place(x=350, y=150)
        but6 = Button(base2, text="Reset", command=reset)
        but6.place(x=400, y=150)
        but7 = Button(base2, text="<--", command=back)
        but7.place(x=1, y=1)

    def deposit():
        base.destroy()
        base2 = Tk()
        base2.title("Withdraw face")
        base2.geometry("800x600")

        def submit():
            but4["state"] = DISABLED
            gu = ent.get()
            gu1 = ent1.get()
            try:
                con = sqlite3.connect("Bank.db")
                cur = con.cursor()
                quart = "select Balance from customer where customer_id=" + gu
                cur.execute(quart)
                data = cur.fetchall()
                cur.close()
                con.close()

                if ds == data:
                    messagebox.showinfo("Error", "Incorrect data")
                else:
                    for fir in data:
                        for sec in fir:
                            da1 = int(sec)
                            da = int(gu1)
                            da1 = da1 + da
                            if da1 > -1:
                                con = sqlite3.connect("Bank.db")
                                da2 = str(da1)
                                quary = "update customer set Balance=" + da2 + " where customer_id=" + gu
                                con.execute(quary)
                                con.commit()
                                con.close()
                                messagebox.showinfo("Success", "Thank for banking")
                                reset()

                            else:
                                messagebox.showinfo("Error", "Invalid amount")
                                reset()
            except:
                messagebox.showinfo("ERROR", "DATA WAS NOT ENTER PROPERLY")

        def reset():
            but4["state"] = NORMAL
            ent1.delete(0, "end")
            ent.delete(0, "end")
            ent.focus()

        def back():
            base2.destroy()
            major()

        lab = Label(base2, text="Enter Account number : ")
        lab.place(x=200, y=70)
        ent = Entry()
        ent.place(x=350, y=75)
        lab1 = Label(base2, text="Enter amount for deposit : ")
        lab1.place(x=195, y=120)
        ent1 = Entry()
        ent1.place(x=350, y=125)
        but4 = Button(base2, text="Submit", command=submit)
        but4.place(x=350, y=170)
        but5 = Button(base2, text="Reset", command=reset)
        but5.place(x=430, y=170)
        but6 = Button(base2, text="<--", command=back)
        but6.place(x=1, y=1)

    but1 = Button(base, text='Balance Check', command=balance)
    but1.pack()
    but2 = Button(text="Withdraw", command=withdraw)
    but2.pack()
    but3 = Button(base, text="Deposit", command=deposit)
    but3.pack()
    base.mainloop()


major()

print("HELLO WORLD")
