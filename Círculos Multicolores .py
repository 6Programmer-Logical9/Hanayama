import turtle as t
from random import randint

t.bgcolor("black")
t.speed("fastest")
t.pensize(2)
t.colormode(255)

for i in range(70):
	    color = (randint(0, 255), randint(0, 255), randint(0, 255))
	    t.color(color)
	    t.circle(i*2)
	    t.left(90)
	    
t.exitonclick()