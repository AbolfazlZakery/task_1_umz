c = float(input("Enter your numbers: "))
x = input("Celsius to Fahrenheit or Fahrenheit to Celsius")
if x == "Celsius to Fahrenheit":
    print((c * 1.8) + 32)
elif x == "Fahrenheit to Celsius":
    print((c - 32) * (5/9))


