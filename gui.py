import tkinter as tk
from tkinter import ttk
from employees import Employee
from cars import Car
from base_car_rent3 import Session
from gui_functions import login_check, all_cars,add_user
from tkinter.messagebox import showinfo,showerror


def add_user_gui(root):
    root.destroy()
    
    window = tk.Tk()
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    # name
    name_label = ttk.Label(window, text="name:")
    name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

    name_entry = ttk.Entry(window)
    name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
    # surname
    surname_label = ttk.Label(window, text="surname:")
    surname_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

    surname_entry = ttk.Entry(window)
    surname_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
    # username
    username_label = ttk.Label(window, text="Username:")
    username_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

    username_entry = ttk.Entry(window)
    username_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
    # password
    password_label = ttk.Label(window, text="password:")
    password_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

    password_entry = ttk.Entry(window)
    password_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

    # Submit button
    submit_button = ttk.Button(window, text="Submit",command=lambda:add_user(Session,Employee,window,name_entry,surname_entry,username_entry,password_entry))
    submit_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
    



    window.mainloop()



# root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,) # show="*"
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login",command=lambda:login_check(Session,Employee,username_entry,password_entry,root))
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


add_user_button = ttk.Button(root, text="add user",command=lambda:add_user_gui(root))
add_user_button.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()

all_cars(Session,Car)