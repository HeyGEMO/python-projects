import random
import turtle

colors=["red","green","yellow","blue"]
turtle.speed(10)
turtle.pensize(2)
turtle.bgpic("")
def curve ():
    for i in range (200):
      turtle.right(1)
      turtle.forward(1)

def heart ():
    turtle.color("black","red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(113)
    curve()
    turtle.left(120)
    curve()
    turtle.forward(112)
    turtle.end_fill()

def txt():
    turtle.penup()
    turtle.setpos(-68,95)
    turtle.pendown()
    turtle.pencolor("cyan")
    turtle.write("I LOVE YOU MOM",font=("Times New Roman",15,"bold"))
heart()
txt()

def firework(x,y):
    turtle.hideturtle()
    col=random.choice(colors)
    l=length_select2()
    turtle.pensize(1)
    turtle.color(col)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(50):
        turtle.forward(70)
        turtle.right(180-(360/20))

def stars(x,y):
    turtle.hideturtle()
    col=random.choice(colors)
    l=length_select()
    turtle.pensize(2)
    turtle.color(col)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()

def length_select():
 return random.randint(3,8)
def length_select2():
    return random.randint(15,70)

turtle.onscreenclick(stars,1)
turtle.onscreenclick(firework,3)
def text():
    turtle.pencolor("yellow")
    turtle.penup()
    turtle.setpos(-250,320)
    turtle.pendown()
    turtle.write("HAPPY MOTHER'S DAY",font=("Times New Roman",30,"bold"))

    turtle.penup()
    turtle.setpos(-600,-250)
    turtle.pendown()
    turtle.write("A mother is she who can take the place of all others but whose place no one else can take.", font="Times New Roman")

text()
turtle.done(0)
