password = None
while password != "myPassword1234":
    password = input("Enter the password: ")
    if password != "myPassword1234":
        print("Your password is incorrect.")
print("Correct password. Welcome.")
