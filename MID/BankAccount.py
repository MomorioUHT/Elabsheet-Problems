amount = float(input("Enter amount: "))

while (True):
    command = str(input("Enter command (w for withdraw, d for deposit, e for exit): "))
    if command == 'w':
        while (True):
            x = float(input("Enter withdraw amount: "))
            if (x <= 0):
                print("Incorrect transactions!")
            elif (x > amount):
                print("You cannot withdraw more than the amount in your account!")
            else:
                amount-=x
                print(f"Current balance = {amount:.2f}$")
                break
    elif command == 'd':
        while (True):
            x = float(input("Enter deposit amount: "))
            if (x <= 0):
                print("Incorrect transactions!")
            else:
                amount+=x
                print(f"Current balance = {amount:.2f}$")
                break
    elif command == 'e':
        break
    else:
        print("Invalid Command!")