from turtle import *

tur = Turtle()
tur.speed(2)

def eyes(color, radius):
    tur.color(color)
    tur.circle(radius)


tur.pos(20, 20)
eyes("red", 30)

tur.pos(20, 50)
eyes("blue", 30)
