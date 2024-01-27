password1 = input('Enter new password : ')
if 7 < len(password1) < 13:
    password2 = input('Enter new password again : ')
    if password1 == password2:
        print('Password set')
    else:
        print("Password doesn't match")
else:
    print('Password must be between 8 to 12 characters long')