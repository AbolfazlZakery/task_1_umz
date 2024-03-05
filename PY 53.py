import turtle as t
t.Screen()
e = (input("The color of the side of the square: "))
v = int(input("The size of the side of the square: "))

t.setup(700, 500)
t.title("...")
t.bgcolor('pink')
x = t.Turtle()
x.color(e)
x.fd(v)
x.lt(90)
x.fd(v)
x.lt(90)
x.fd(v)
x.lt(90)
x.fd(v)





while 1:
    t.update()
t.mainloop()