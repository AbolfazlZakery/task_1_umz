#نوشتن لاترجی با ترتل
import turtle as t

flash = t.Turtle()


def make_g():
    flash.pendown()
    flash.lt(130)
    flash.fd(40)
    flash.rt(90)
    flash.fd(40)
    flash.rt(90)
    flash.fd(80)
    for _ in range(10):
        flash.lt(15)
        flash.fd(6)
    for _ in range(10):
        flash.rt(13)
        flash.fd(10)
    for _ in range(10):
        flash.rt(10)
        flash.fd(11)

def make_u():
    flash.pendown()
    flash.rt(90)
    flash.fd(100)
    for _ in range(25):
        flash.lt(7.2)
        flash.fd(3)
    flash.fd(100)
def location(x, y):
    flash.penup()
    return flash.goto(x, y)

def make_cirle(x):
    flash.pendown()
    flash.circle(x)

board = t.Screen()
board.setup(600, 600)
board.title('strongbox')
board.bgcolor('white')

def make_tar():
    flash.pendown()
    flash.rt(180)
    flash.fd(30)
    flash.rt(90)
    flash.fd(45)
    flash.lt(50)
    flash.fd(80)

location(40, 40)
make_cirle(10)
location(20, 40)
make_cirle(10)
location(80, 80)
make_u()
location(30,20)
make_tar()
location(-95, 50)
make_g()
location(-75, -30)
make_cirle(10)



while 1:
    board.update()
board.mainloop()
