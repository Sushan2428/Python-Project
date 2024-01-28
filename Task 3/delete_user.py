from password_manager import del_user

filename = 'password.txt'

username = input("Enter Username:- ")

del_user(username, filename)