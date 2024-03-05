while 1:
    x = int(input("Enter frist number: "))
    y = int(input("Enter frist number: "))
    t = (input("Enter your action: "))
    if t == "divide":
        print(x / y)
    elif t == "multipe":
        print(x * y)
    elif t == "difference":
        print(x - y)
    elif t == "sum":
        print(x + y)
    else :
        continue