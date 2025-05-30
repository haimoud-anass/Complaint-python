import sqlite3 as sql
import time 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
# from self_code import SelfCode
from Admin_Zone import ComplaintsManagerApp

log = Tk()

con = sql.connect("Complaints.db")
cur = con.cursor()


  



erorr=StringVar()
us= StringVar()
ps= StringVar()

def sign_up():
    if not(entuser.get()=="" or entpass.get()==""):
        cur.execute("SELECT name FROM sign WHERE name=? AND pass=?",(entuser.get(),entpass.get()))
        b = cur.fetchall()
        
        if not(bool(b)) and  entuser.get().lower() != "admin" and entpass.get().lower() != 'admin':
            erorr.set("")
            Updated = 'False'
            cur.execute("INSERT INTO sign(name,pass) VALUES(?,?)",(entuser.get(),entpass.get()))
            con.commit()
            
            global us , ps
            uss , pss = entuser.get(),entpass.get()
            us.set("")
            ps.set("")
           
            
            a=Toplevel(log)
            
                
            a.geometry("450x400+100+100")
            a.config(bg="#2c3e50")
            
            Entry1=Entry(a,
            bg="#f0f0f0",
            fg="black",
            font=("arial",13),
                bd=0,
                highlightcolor=None,
                highlightbackground=None,
                highlightthickness=1,
                show="",
                )
            Label3=Label(a,
                    text='Description:',
                    bg="#2c3e50",
                    fg="white",
                    font=("arial",13),
                    bd=0,
                    )
            Entry2=Entry(a,
                    bg="#f0f0f0",
                    fg="black",
                    font=("arial",13),
                    bd=0, 
                    highlightcolor=None,
                    highlightbackground=None,
                    highlightthickness=1,
                    show="",
                    )
            Label4=Label(a,text='Statu:',
                    bg="#2c3e50",
                    fg="white",
                    font=("arial",13),
                    bd=0,
                    )
            Label5=Label(a,text='Resolution:',
                    bg="#2c3e50",
                    fg="white",
                    font=("arial",13),
                    bd=0,
                    )
            Entry3=Entry(a,
                    bg="#f0f0f0",
                    fg="black",
                    font=("arial",13),
                    bd=0,
                    highlightcolor=None,
                    highlightbackground=None,
                    highlightthickness=1,
                    show="",
                    )
            Entry1.place(x=217,y=76,width=184,height=23)
            Label3.place(x=30,y=77,width=185,height=23)
            Entry2.place(x=217,y=119,width=184,height=23)
            Label4.place(x=30,y=121,width=184,height=23)
            Label5.place(x=31,y=161,width=184,height=23)
            Entry3.place(x=218,y=159,width=184,height=23)
            def save():
                if not( Entry1.get()=="" or Entry2.get()=="" or Entry3.get()==''):
                    mytime = time.localtime()
                    result = time.strftime("%d/%m/%y, %H:%M:%S",mytime)
                    cur.execute("UPDATE sign SET description=? , status=? ,resolution =? , time =?  , updated=? WHERE name = ? AND pass = ? ",(Entry1.get(),Entry2.get(),Entry3.get(),result,'False',uss,pss))
                    a.destroy()
                    messagebox.showinfo("complete","save completed")
                    con.commit()
                    
                
                else:
                    messagebox.showerror("Error","please fill all entrys")
            btn2 = Button(a,text="save",command=save)
            btn2.place(x=31,y=200)
            a.mainloop()
        else:
            erorr.set("you have account")
    
    else:
        messagebox.showerror("Error","please fill all entrys")
def sign_in():
    if entuser.get().lower() == "admin" and entpass.get().lower() == 'admin':
        
        log.destroy()
        root = Tk()
        app = ComplaintsManagerApp(root)
        app.run()

    elif not(entuser.get()=="" or entpass.get()==""):
        cur.execute("SELECT * FROM sign WHERE name=? AND pass=?",(entuser.get(),entpass.get()))
        b = cur.fetchone()
        erorr.set("")
        
        
        
        if bool(b) :
            global us , ps
            uss , pss = entuser.get(),entpass.get()
            us.set("")
            ps.set("")
            a=Toplevel(log)
            
            a.title("tk")
            
            a.geometry("450x400+100+100")
            a.config(bg="#2c3e50")
            a.attributes("-topmost",0)
            a.overrideredirect(0)
            en1,en2,en3 = StringVar(),StringVar(),StringVar()
                
            Entry1=Entry(a,state='readonly',
                    textvariable=en1,
                    bg="#f0f0f0",
                    fg="black",
                    font=("arial",13),
                    bd=0,
                    highlightcolor=None,
                    highlightbackground=None,
                    highlightthickness=1,
                    show="",
                    )
            Label3=Label(a,
                    text='Description:',
                    bg="#2c3e50",
                    fg="white",
                    font=("arial",13),
                    bd=0,
                    )
            Entry2=Entry(a,state='readonly',textvariable=en2,
                    bg="#f0f0f0",
                    fg="black",
                    font=("arial",13),
                    bd=0, 
                    highlightcolor=None,
                    highlightbackground=None,
                    highlightthickness=1,
                    show="",
                    )
            Label4=Label(a,text='Statu:',
                    bg="#2c3e50",
                    fg="white",
                    font=("arial",13),
                    bd=0,
                    )
            Label5=Label(a,text='Resolution:',
                    bg="#2c3e50",
                    fg="white",
                    font=("arial",13),
                    bd=0,
                    )
            Entry3=Entry(a,state='readonly',textvariable=en3,
                    bg="#f0f0f0",
                    fg="black",
                    font=("arial",13),
                    bd=0,
                    highlightcolor=None,
                    highlightbackground=None,
                    highlightthickness=1,
                    show="",
                    )
            Entry1.place(x=217,y=76,width=184,height=23)
            Label3.place(x=30,y=77,width=185,height=23)
            Entry2.place(x=217,y=119,width=184,height=23)
            Label4.place(x=30,y=121,width=184,height=23)
            Label5.place(x=31,y=161,width=184,height=23)
            Entry3.place(x=218,y=159,width=184,height=23)
            en1.set(b[3])
            en2.set(b[4])
            en3.set(b[5])
            
            

            
            def save():
         
                if not( Entry1.get()=="" or Entry2.get()=="" or Entry3.get()==''):
                    Updated ='True'
                    btnup.place(x=31,y=200)
                    btnsv.place(x=31,y=2000)
                    
                    cur.execute("UPDATE sign SET description=? , status=? ,resolution =? , updated =? WHERE name = ? AND pass = ?",(Entry1.get(),Entry2.get(),Entry3.get(),'True',uss,pss))
                    con.commit()
                    Entry1.config(state='readonly',fg="black")
                    Entry2.config(state='readonly',fg="black")
                    Entry3.config(state='readonly',fg="black")
                    a.destroy()
                    messagebox.showinfo("complete","save completed")
                else:
                    messagebox.showerror("Error","Please fill all entrys")
            def up_date():

                btnup.place(x=31,y=2000)
                btnsv.place(x=31,y=200)
                Entry1.config(state='normal')
                Entry2.config(state='normal')
                Entry3.config(state='normal')
            btnsv = Button(a,text="save",command=save)
            btnup = Button(a,text="update",command=up_date)
            Entry1.config(state='readonly',border=1,fg="black")
            Entry2.config(state='readonly',border=1,fg="black")
            Entry3.config(state='readonly',border=1,fg="black")
            btnup.place(x=31,y=200)
            
            a.mainloop()
        else:
            erorr.set("You dont have account")
    else:
        messagebox.showerror("Error","please fill all entrys")





cur.execute("CREATE TABLE IF NOT EXISTS sign(id integer primary key autoincrement,name text ,pass text,description TEXT , status TEXT, resolution TEXT,time TEXT,Updated   TEXT)")
con.commit()
log.resizable(False, False)
log.geometry("390x400+100+100")
log.title("Complaints Management")
log.config(background="#2c3e50")
lbl = Label(log,text="log-in", font=('Calibri', 16), bg='#2c3e50', fg='white')
lbl.pack(pady=40)
lbluser = Label(log,text="Username:", font=('Calibri', 16), bg='#2c3e50', fg='white')
lbluser.place(x=30,y=146)
entuser = Entry(log, width=20,textvariable=us , font=('Calibri', 16))
entuser.place(x=129,y=150)
lblpass = Label(log,text="Password:", font=('Calibri', 16), bg='#2c3e50', fg='white')
lblpass.place(x=30,y=196)
entpass = Entry(log, width=20,show="*",textvariable=ps, font=('Calibri', 16))
entpass.place(x=129,y=200)
btn = Button(log, border=0 , width=10,relief=SOLID, text="sign-in",command=sign_in)
btn.place(x=230,y=270)
btn1 = Button(log,border=0 ,width=10,relief=SOLID, text="sign-up",command=sign_up)
btn1.place(x=85,y=270)

aa = Label(log,textvariable=erorr, font=('Calibri', 10), bg='#2c3e50', fg='red')
aa.place(x=80,y=245)

log.mainloop()
