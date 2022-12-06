password = "test"
try:
    user_pas =input("enter your password: ")
    if user_pas == password:
        print("Password correct, you're logging in now")
except:
    print("incorrect password, please try again, you have two more tries")
    for i in range(2):
        user_pas =input("enter your password: ")
        if input ==password:
            print("Password correct, you're logging in now")
        else:
            print("Incorrect")
else:
    print("Congratulations, you know your password.")
finally:
    print("You suck, you've been locked out.")