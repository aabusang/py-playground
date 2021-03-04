choice_num = input("Enter 1 for sign or 2 for sign up: ")

if (choice_num == 1):
    name = input("username: ")
    password = input("password: ")
elif(choice_num == 2):
    username = input("Chose a username: ")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
else:
    print("Invalid choice")
