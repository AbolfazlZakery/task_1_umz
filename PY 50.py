print("hi!! \t welcom your account ")
sum = 0
while 1:
    x = input("please specify your desired operaition: ")
    if x == "deposid":
        y = int(input("Enter the desired amount: "))
        sum += y
        print("Your current account balance: ", sum)
    elif x == "withdraw money":
        c = int(input("Enter the desired amount: "))
        sum -= c
        print("Your current account balance: ", sum)
    elif x == "inventory chech":
        print("Your current account balance: ", sum)
    elif x == "money transfer":
        c = input("Enter card number: ")
        d = int(input("how much money for transfer: "))
        b = input("Enter your passport: ")
        sum -= d
        print("compleceted")
        print("Your current account balance: ", sum)
    else:
        continue
