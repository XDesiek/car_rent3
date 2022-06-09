

def login_check(Session,Employee,username_entry,password_entry,root):                           
    import tkinter as tk
    session = Session()
    username_checkbox=username_entry.get()
    password_checkbox=password_entry.get()
    user = session.query(Employee).filter(Employee.username == username_checkbox).first()
    if username_checkbox ==(""):
        tk.messagebox.showerror(root,message="you didn't enter your username").pack()
    else:
        if password_checkbox ==(""):
            tk.messagebox.showerror(root,message="you didn't enter your password").pack()
        else:    
            if user is not None:
                if user.password == password_checkbox:
                    tk.messagebox.showinfo(root,message='everything is correct')
                    root.destroy()     
                else:
                        tk.messagebox.showerror(root,message="your password isn't correct").pack()
            else:
                tk.messagebox.showerror(root,message="your username isn't correct").pack()

def all_cars(Session,Car):
    sessioncar = Session()
    cars = sessioncar.query(Car).all()
    for car in cars:
       print('')
       print (car)
    print('')
    sessioncar.close()
#user ma jakas dziwna classe i nie jest stringiem  //  potem odpalic nowe window z dodawaniem cars i ogarnianiem



def add_user(Session,Employee,window,name_entry,surname_entry,username_entry,password_entry):
    import tkinter as tk
    session = Session()
    name=name_entry.get()
    surname=surname_entry.get()
    username=username_entry.get()
    password=password_entry.get()

    double_user_check = session.query(Employee).filter(Employee.username == username).first()
    if double_user_check is None:
        ziomek = Employee(name,surname,username,password)
        session.add(ziomek)
        session.commit()
        session.close()
        window.destroy()
    else:
        tk.messagebox.showerror(title="login box",message="your username has been already taken").pack()

