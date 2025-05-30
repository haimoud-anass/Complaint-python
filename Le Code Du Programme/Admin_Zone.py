from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sqlite3
import time
class DataBase:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        
        
    def insert(self,name,passw,description,status,resolution):
        mytime = time.localtime()
        result = time.strftime("%d/%m/%y, %H:%M:%S",mytime)
        self.cur.execute("insert into sign values (NULL,?,?,?,?,?,?,?)",
                         (name,passw,description,status,resolution,result,'False'))
        self.con.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM sign")
        rows = self.cur.fetchall()
        return rows
    def remove(self,id):
        self.cur.execute("delete from sign where id=?",(id,))
        self.con.commit()
    def update(self,id,name,passw,status,description,resolution):
        
        self.cur.execute("update sign set name=?,pass=?,description=?,status=?,resolution=?  , updated = ? where id=?",
                         (name,passw,description,status,resolution,'True',id))
        self.con.commit()
    def check(self,us,ps):
        self.cur.execute("SELECT name FROM sign WHERE name=? AND pass=?",(us,ps))
        b = self.cur.fetchall()
        return b
class ComplaintsManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Complaints Management")
        self.root.geometry('365x480+100+100')
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')

        self.db = DataBase("Complaints.db")
        self.name = tk.StringVar()
        self.passw = tk.StringVar()
        self.Gender = tk.StringVar()
        self.Description = tk.StringVar()
        self.Status = tk.StringVar()
        self.Resolution = tk.StringVar()
        self.create_widgets()
        self.create_table()

    def hide(self):
        self.root.geometry('365x480')

    def show(self):
        self.root.geometry('1615x615')

    def get_data(self, event):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        global row
        row = data['values']
        self.name.set(row[1])
        self.passw.set(row[2])
        self.Status.set(row[3])
        self.Description.set(row[4])
        
        self.Resolution.set(row[5])

    def clear(self):
        self.name.set("")
        self.Gender.set("")
        self.passw.set("")
        self.Status.set("")
        self.Resolution.set("")
        self.Description.set("")

    def display_all(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.db.fetch():
            self.tv.insert("", tk.END, values=row)

    def add_complaints(self):
        b = self.db.check(self.name.get(),self.passw.get())
        if self.name.get() == "" or self.passw.get() == ""  or self.Status.get() == "" or self.Description.get() == "" or self.Resolution.get() == "":
            messagebox.showerror("Error", "Please Fill all Entry")
        
        elif not(bool(b)) and self.name.get()!="admin" and self.passw.get() != 'admin' :
            self.db.insert(self.name.get(), self.passw.get(), self.Status.get(),
                        self.Description.get(), self.Resolution.get())
            self.clear()
            self.display_all()
            messagebox.showinfo("Success", "Added new Complaint")
        else:
            messagebox.showerror("Error", "The account already exists")
        

    def delete(self):
        self.db.remove(row[0])
        self.clear()
        self.display_all()

    def update(self):
        if self.name.get() == "" or self.passw.get() == ""  or self.Status.get() == "" or self.Description.get() == "" or self.Resolution.get() == "":
            messagebox.showerror("Error", "Please Fill all Entry")
            return
        self.db.update(row[0], self.name.get(), self.passw.get(), self.Description.get(),self.Status.get(),
                        self.Resolution.get())
        self.clear()
        self.display_all()
        messagebox.showinfo("Success", "The Complaint data is updated")

    def create_widgets(self):
        enties_frame = tk.Frame(self.root, bg='#2c3e50')
        enties_frame.place(x=1, y=1, width=360, height=510)

        title = tk.Label(enties_frame, text="Complaints Management", font=('Calibri', 18, 'bold'),
                         bg='#2c3e50', fg='white')
        title.place(x=10, y=1)

        name_label = tk.Label(enties_frame, text="Name:", font=('Calibri', 16), bg='#2c3e50', fg='white')
        name_label.place(x=10, y=50)
        name_entry = tk.Entry(enties_frame, width=20, textvariable=self.name, font=('Calibri', 16))
        name_entry.place(x=130, y=52)

        lbl_pass = tk.Label(enties_frame, text="pass:", font=('Calibri', 16), bg='#2c3e50', fg='white')
        lbl_pass.place(x=10, y=100)
        ent_pass = tk.Entry(enties_frame, width=20, textvariable=self.passw, font=('Calibri', 16))
        ent_pass.place(x=130, y=102)



        lbl_description = tk.Label(enties_frame, text="Status:", font=('Calibri', 16), bg='#2c3e50', fg='white')
        lbl_description.place(x=10, y=200)
        ent_description = tk.Entry(enties_frame, width=20, textvariable=self.Description, font=('Calibri', 16))
        ent_description.place(x=130, y=202)

        lbl_status = tk.Label(enties_frame, text="Description:", font=('Calibri', 16), bg='#2c3e50', fg='white')
        lbl_status.place(x=10, y=250)
        ent_status = tk.Entry(enties_frame, width=20, textvariable=self.Status, font=('Calibri', 16))
        ent_status.place(x=130, y=252)

        lbl_resolution = tk.Label(enties_frame, text="Resolution:", font=('Calibri', 16), bg='#2c3e50', fg='white')
        lbl_resolution.place(x=10, y=300)
        ent_resolution = tk.Entry(enties_frame, width=20, textvariable=self.Resolution, font=('Calibri', 16))
        ent_resolution.place(x=130, y=302)

        btn_hide = tk.Button(enties_frame, text='Hide', bd=1, bg='white', relief=tk.SOLID, cursor="hand2", command=self.hide)
        btn_hide.place(x=280, y=10)

        btn_show = tk.Button(enties_frame, text='Show', cursor="hand2", command=self.show, bd=1, bg='white',
                             relief=tk.SOLID)
        btn_show.place(x=320, y=10)

        btn_frame = tk.Frame(enties_frame, bg='#2c3e50', bd=1, relief=tk.SOLID)
        btn_frame.place(x=10, y=350, width=346, height=98)

        btn_add = tk.Button(btn_frame, text='Add Details', width=15, height=1, font=('Calibri', 16), fg='white',
                            bg="#16a085", bd=0, command=self.add_complaints, cursor="hand2")
        btn_add.place(x=2, y=5)

        btn_update = tk.Button(btn_frame, text='Update Details', width=15, height=1, command=self.update,
                               font=('Calibri', 16), fg='white', bg="#2980b9", bd=0, cursor="hand2")
        btn_update.place(x=2, y=50)

        btn_delete = tk.Button(btn_frame, text='Delete Details', width=15, height=1, command=self.delete,
                               font=('Calibri', 16), fg='white', bg="#c0392b", bd=0, cursor="hand2")
        btn_delete.place(x=171, y=5)

        btn_clear = tk.Button(btn_frame, text='Clear Details', width=15, height=1, font=('Calibri', 16), fg='white',
                              bg="#f39c12", bd=0, command=self.clear, cursor="hand2")
        btn_clear.place(x=171, y=50)

    def create_table(self):
        tree_frame = tk.Frame(self.root, bg='white')
        tree_frame.place(x=365, y=1, width=1250, height=610)
        style = ttk.Style(self.root)
        style.configure("mystyle.Treeview", font=('Calibri', 13), rowheight=50)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 20, 'bold'))
        self.tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6,7,8), style="mystyle.Treeview")
        self.tv.heading('1', text="ID")
        self.tv.column('1', width="40")
        self.tv.heading('2', text="username")
        self.tv.column('2', width="117")
        self.tv.heading('3', text="Password")
        self.tv.column('3', width="118")
        self.tv.heading('4', text="Description")
        self.tv.column('4', width="185")
        self.tv.heading('5', text="status")
        self.tv.column('5', width="185")
        self.tv.heading('6', text="Resolution")
        self.tv.column('6', width="270")
        self.tv.heading('7', text="Execution time")
        self.tv.column('7', width="200")
        self.tv.heading('8', text="Updated")
        self.tv.column('8', width="100")
        self.tv.bind("<ButtonRelease-1>", self.get_data)
        self.tv['show'] = 'headings'
        self.tv.place(x=1, y=1, height=610, width=1250)

        self.display_all()

    def run(self):
        self.root.mainloop()
        

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ComplaintsManagerApp(root)
#     app.run()