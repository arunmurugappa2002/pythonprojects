from turtle import *
speed(11)
color('blue')
bgcolor('red')
right(45)
for n in range(150):
    if 0< n < 84:
        left(5)
        circle(10)
        backward(10)
    if 84< n < 150:
        right(5)
        circle(10)
        backward(10)