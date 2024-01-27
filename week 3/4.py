BAD_PASSWORDS = ['hello123', 'letmein', 'sesame', 'maya7654', 'justinbieber']
password1 = input('Enter new password : ')
# check if the password is not the bad password
if password1 not in BAD_PASSWORDS:
    # check if the password length is between 8 and 12 characters
    if 7 < len(password1) < 13:
        password2 = input('Enter new password again : ')
        # to check if the both passwords match or not
        if password1 == password2:
            print('Password set.')
        else:
            print("Password doesn't match.")
    else:
        print('The password must be between 8 to 12 characters long.')
else:
    print('This password cannot be used.')
