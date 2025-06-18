name:str = input("Name: ")
email:str = input("Email: ")

if len(name) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")
elif email.find("@gmail.com") == -1:
    print("the email is not valid , please provide a valid email .")
else:
    print(f"welcome {name}, you registered with the email {email} !")