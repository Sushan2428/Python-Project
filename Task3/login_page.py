from password_manager import login

filename = 'password.txt'

username = input("Username:- ")
password = input("Password:- ")

login(username, password, filename)