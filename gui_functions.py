
def login_check(Session,Employee,username_entry,password_entry,root,tk):
    
    session = Session()
    username_checkbox=username_entry.get()
    password_checkbox=password_entry.get()
    user = session.query(Employee).filter(Employee.username == username_checkbox).all()
    password = session.query(Employee).filter(Employee.password ==password_checkbox).all()
    if user == password:# bedzie sie wieszac przy wielu takich samych paswordach
        tk.messagebox.showinfo(root,message='everything is correct').pack()
    session.close()

#user ma jakas dziwna classe i nie jest stringiem  //  potem odpalic nowe window z dodawaniem cars i ogarnianiem