import tkinter as tk
from tkinter import ttk
from employees import Employee
from base_car_rent3 import Session
from gui_functions import login_check
from tkinter.messagebox import showinfo



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
login_button = ttk.Button(root, text="Login",command=lambda:login_check(Session,Employee,username_entry,password_entry,root,tk))
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()
