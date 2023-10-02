import turtle

wn = turtle.Screen()
wn.setup(800,600)
wn.bgcolor('red')

pic = turtle.Turtle()
pic.speed(0)
pic.penup()
pic.goto(180,180)
pic.pendown()
def arun(value):
    for i in range(52):
        pic.forward(value)
        pic.left(90)
        value = value + 2
new_pic = turtle.Turtle()
new_pic.penup()
new_pic.goto(180,-180)
new_pic.pendown()
new_pic.speed(0)
def moni(val):
        for i in range(50):
            new_pic.forward(val)
            new_pic.left(90)
            val = val + 2
arun(1)
arun(1)
moni(1)
moni(1)
turtle.done()
wn.mainloop()