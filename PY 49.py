x = (input("Enter your str: "))
try:
    float(x)
    if "." in x:
        print("float")
    else:
        print("int")
except:
    if x[0]=='[' and x[-1]==']' in x:
        print("list")
    elif x[0]=='(' and x[-1]==')' in x:
        print("tuple")
    elif x[0]=='{' and x[-1]=='}' in x:
        if ':' in x:
            print("dic")
        else:
            print("set")
    else:
        print("string")
