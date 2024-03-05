x = (input("Enter your str: "))
try:
    float(x)
    if "." in x:
        print("float")
    else:
        print("int")
except:
    if '[' in x:
        print("list")
    elif '('in x:
        print("tuple")
    elif '{' in x:
        if ':' in x:
            print("dic")
        else:
            print("set")
    else:
        print("string")