from tkinter import *


root = Tk()
root.title('Outfield')
root.geometry('576x360')

login_frame = Frame(root, width=576, height=360)
login_frame.pack()

register_frame = Frame(root, width=576, height=360)
welcome_frame = Frame(root, width=576, height=360)


class loginPage():
    def __init__(self):
        self.outfield_label = Label(login_frame, text='Welcome to the Outfield System!', font=30)
        self.outfield_label.pack(fill='both', expand=1)

        self.space_label = Label(login_frame)
        self.space_label.pack()

        self.username_label = Label(login_frame, text='Username')
        self.username_label.pack()

        self.username_entry = Entry(login_frame, width=35)
        self.username_entry.pack()

        self.password_label = Label(login_frame, text='Password')
        self.password_label.pack()

        self.password_entry = Entry(login_frame, width=35, show='*')
        self.password_entry.pack()
        
        self.login_error_label = Label(login_frame, text='')
        self.login_error_label.pack()
        

        def clearAllEntries():
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)


        def logMeIn():
            self.read_txt = open('users.txt', 'r')
            self.users = self.read_txt.read()
            self.users = self.users.split()
            if self.username_entry.get() in self.users:
                self.user_index = self.users.index(self.username_entry.get())
                if self.password_entry.get() == self.users[self.user_index+1]:
                    clearAllEntries()
                    welcome_frame.pack()
                    login_frame.pack_forget()
                else:
                    self.login_error_label.config(text='Password is incorrect.')
            else:
                self.login_error_label.config(text="Username doesn't exist.")


        def SignMeUp():
            login_frame.pack_forget()
            register_frame.pack(fill='both', expand=1)
        

        self.login_button = Button(login_frame, text='Log In', command=logMeIn)
        self.login_button.pack()

        self.sign_up_button = Button(login_frame, text='Sign Up', command=SignMeUp)
        self.sign_up_button.pack()


class signUpPage():
    def __init__(self):
        self.sign_up_label = Label(register_frame, text='Be an Outfield Member!', font=30)
        self.sign_up_label.pack(fill='both', expand=1)

        self.new_user_label = Label(register_frame, text='Username')
        self.new_user_label.pack()

        self.new_user_entry = Entry(register_frame, width=35)
        self.new_user_entry.pack()

        self.new_pass_label = Label(register_frame, text='Password')
        self.new_pass_label.pack()

        self.new_pass_entry = Entry(register_frame, width=35, show='*')
        self.new_pass_entry.pack()

        self.confirm_pass_label = Label(register_frame, text='Confirm Password')
        self.confirm_pass_label.pack()

        self.confirm_pass_entry = Entry(register_frame, width=35, show='*')
        self.confirm_pass_entry.pack()

        self.register_error_label = Label(register_frame, text='')
        self.register_error_label.pack()


        def clearAllEntries():
            self.new_user_entry.delete(0, END)
            self.new_pass_entry.delete(0, END)
            self.confirm_pass_entry.delete(0, END)


        def RegisterMe():
            if ' ' not in self.new_user_entry.get():
                if self.new_pass_entry.get() == self.confirm_pass_entry.get():
                    check_txt = open('users.txt', 'r')
                    old_users = check_txt.read()
                    old_users = old_users.split()
                    if self.new_user_entry.get() in old_users:
                        self.register_error_label.config(text='Username already exists.')
                    else:
                        write_on_txt = open('users.txt', 'a')
                        write_on_txt.writelines(f'{self.new_user_entry.get()} {self.new_pass_entry.get()} {self.confirm_pass_entry.get()}\n')
                        write_on_txt.close()
                        clearAllEntries()
                        self.register_error_label.config(text="Account created!")
                else:
                    self.register_error_label.config(text="Passwords don't match.")
            else:
                self.register_error_label.config(text="Spaces are not permitted.")


        def returnToLogin():
                    register_frame.pack_forget()
                    login_frame.pack()


        self.register_button = Button(register_frame, text='Register', command=RegisterMe)
        self.register_button.pack()

        self.return_to_login_button = Button(register_frame, text='Return', command=returnToLogin)
        self.return_to_login_button.pack()


class welcomePage():
    def __init__(self):
        self.sign_up_label = Label(welcome_frame, text='Welcome, Outfield Member!', font=30)
        self.sign_up_label.pack(fill='both', expand=1)


        def LogOut():  
            welcome_frame.pack_forget()
            login_frame.pack()


        self.log_out_button = Button(welcome_frame, text='Log out', command=LogOut)
        self.log_out_button.pack()


login_page = loginPage()
sign_up_page = signUpPage()
welcome_page = welcomePage()

root.mainloop()
