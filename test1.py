from tkinter import *

# Positions
user_label_x = 1
user_label_y = 0

root = Tk()
root.title('Outfield')
root.geometry('576x360')

login_frame = Frame(root, width=576, height=360)
login_frame.pack()

register_frame = Frame(root, width=576, height=360)
welcome_frame = Frame(root, width=576, height=360)

#Log In Frame
outfield_label = Label(login_frame, text='Welcome to the Outfield System!', font=30)
outfield_label.pack(fill='both', expand=1)

space_label = Label(login_frame)
space_label.pack()

username_label = Label(login_frame, text='Username')
username_label.pack()

username_entry = Entry(login_frame, width=35)
username_entry.pack()

password_label = Label(login_frame, text='Password')
password_label.pack()

password_entry = Entry(login_frame, width=35)
password_entry.pack()


def clearAllEntries():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    new_user_entry.delete(0, END)
    new_pass_entry.delete(0, END)
    confirm_pass_entry.delete(0, END)


login_error_label = Label(login_frame, text='')
login_error_label.pack()

def logMeIn():
    read_txt = open('users.txt', 'r')
    users = read_txt.read()
    users = users.split()
    if username_entry.get() in users:
        user_index = users.index(username_entry.get())
        print(user_index)
        if password_entry.get() == users[user_index+1]:
            print(users.index(password_entry.get()))
            print('You are logged in!')
            clearAllEntries()
            welcome_frame.pack()
            login_frame.pack_forget()

        else:
            print('Password is incorrect.')
            login_error_label.config(text='Password is incorrect.')
    else:
        print("Username doesn't exist.")
        login_error_label.config(text="Username doesn't exist.")


login_button = Button(login_frame, text='Log In', command=logMeIn)
login_button.pack()


def SignMeUp():
    login_frame.pack_forget()
    register_frame.pack(fill='both', expand=1)


sign_up_button = Button(login_frame, text='Sign Up', command=SignMeUp)
sign_up_button.pack()

#Sign up Frame
sign_up_label = Label(register_frame, text='Be an Outfield Member!', font=30)
sign_up_label.pack(fill='both', expand=1)

new_user_label = Label(register_frame, text='Username')
new_user_label.pack()

new_user_entry = Entry(register_frame, width=35)
new_user_entry.pack()

new_pass_label = Label(register_frame, text='Password')
new_pass_label.pack()

new_pass_entry = Entry(register_frame, width=35)
new_pass_entry.pack()

confirm_pass_label = Label(register_frame, text='Confirm Password')
confirm_pass_label.pack()

confirm_pass_entry = Entry(register_frame, width=35)
confirm_pass_entry.pack()

register_error_label = Label(register_frame, text='')
register_error_label.pack()


def RegisterMe():
    if ' ' not in new_user_entry.get():
        if new_pass_entry.get() == confirm_pass_entry.get():
            check_txt = open('users.txt', 'r')
            old_users = check_txt.read()
            old_users = old_users.split()
            if new_user_entry.get() in old_users:
                register_error_label.config(text='Username already exists.')
            else:
                print(f'New username: {new_user_entry.get()}')
                print(f'New password: {new_pass_entry.get()}')
                print(f'Confirm Password: {confirm_pass_entry.get()}')
                write_on_txt = open('users.txt', 'a')
                write_on_txt.writelines(f'{new_user_entry.get()} {new_pass_entry.get()} {confirm_pass_entry.get()}\n')
                write_on_txt.close()
                clearAllEntries()
        else:
            print("Passwords don't match")
            register_error_label.config(text="Passwords don't match.")
    else:
        print('Spaces are not permitted')
        register_error_label.config(text="Spaces are not permitted.")

register_button = Button(register_frame, text='Register', command=RegisterMe)
register_button.pack()


def returnToLogin():
    register_frame.pack_forget()
    login_frame.pack()


return_to_login_button = Button(register_frame, text='Return', command=returnToLogin)
return_to_login_button.pack()

#Welcome Frame
sign_up_label = Label(welcome_frame, text='Welcome, Outfield Member!', font=30)
sign_up_label.pack(fill='both', expand=1)


def LogOut():  
    welcome_frame.pack_forget()
    login_frame.pack()

log_out_button = Button(welcome_frame, text='Log out', command=LogOut)
log_out_button.pack()




root.mainloop()
"""giovanazario@gmail.com@edu.com.br"""