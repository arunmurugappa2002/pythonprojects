import  turtle

pen = turtle.Turtle()
pen.penup()
pen.goto(-200,0)
pen.pendown()
pen.pensize(20)
for i in range(5):
    pen.color('yellow')
    pen.begin_fill()
    pen.forward(300)
    pen.right(144)
    pen.end_fill()

turtle.mainloop()