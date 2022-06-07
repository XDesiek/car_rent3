

def login_check(Session,Employee,username_entry,password_entry,root):
    import tkinter as tk
    session = Session()
    username_checkbox=username_entry.get()
    password_checkbox=password_entry.get()
    user = session.query(Employee).filter(Employee.username == username_checkbox).all()
    password = session.query(Employee).filter(Employee.password ==password_checkbox).all()
    
    
    # print (f"\n\n\n\n\n {user.type()} \n\n\n\n\n")


    if user == password:# bedzie sie wieszac przy wielu takich samych paswordach
        root.destroy()
        tk.messagebox.showinfo(title="login box",message='everything is correct')
    elif user != password:
        tk.messagebox.showerror(title="login box",message='login is not correct').pack()    
    session.close()

def all_cars(Session,Car):
    sessioncar = Session()
    cars = sessioncar.query(Car).all()
    for car in cars:
       print('')
       print (car)
    print('')
    sessioncar.close()
#user ma jakas dziwna classe i nie jest stringiem  //  potem odpalic nowe window z dodawaniem cars i ogarnianiem











# def add_user(root,):
#     import tkinter as tk
#     from tkinter import ttk
#     root.destroy()
    
#     window = tk.Tk()
#     window.columnconfigure(0, weight=1)
#     window.columnconfigure(1, weight=3)

#     # name
#     name_label = ttk.Label(window, text="name:")
#     name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

#     name_entry = ttk.Entry(window)
#     name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
#     # surname
#     surname_label = ttk.Label(window, text="surname:")
#     surname_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

#     surname_entry = ttk.Entry(window)
#     surname_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
#     # username
#     username_label = ttk.Label(window, text="Username:")
#     username_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

#     username_entry = ttk.Entry(window)
#     username_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
#     # password
#     password_label = ttk.Label(window, text="password:")
#     password_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

#     password_entry = ttk.Entry(window)
#     password_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

#     # login button
#     login_button = ttk.Button(window, text="Login",command=lambda:submit())
#     login_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
    
#     window.columnconfigure(0, weight=1)
#     window.columnconfigure(1, weight=3)


#     window.mainloop()

