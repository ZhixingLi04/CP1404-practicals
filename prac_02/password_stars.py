password = input("Please enter your password:")
while password == "":
    print("Invalid input!")
    password = input("Please enter your password:")
print(len(password)*"*")