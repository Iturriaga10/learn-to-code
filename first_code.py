from turtle import *

Bob = Turtle()
Matt = Turtle()

Bob.color('red')
Bob.speed(2)
Bob.fillcolor('red')

Matt.color('blue')
Matt.speed(2)
Matt.fillcolor('blue')
Matt.left(37)
Matt.forward(320)
Matt.end_fill()


Bob.begin_fill()
Bob.left(45)
Bob.forward(200)
Bob.circle(100, 180)
Bob.left(10)
Bob.forward(50)
Bob.left(30)
Bob.left(195)
Bob.circle(100, 180)

Bob.left(37)
Bob.forward(320)
Bob.end_fill()

exitonclick()