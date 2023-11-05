import turtle as t
import random

t.speed(0)
t.bgcolor("black")
colores = ["red", "orange", "yellow", "green", "blue", "purple"]

def dibujar_espiral_multicolor():
	     for i in range(360):
	     	    t.pencolor(colores[i % 6])
	     	    t.forward(i)
	     	    t.right(59)
	     	    
dibujar_espiral_multicolor()

t.hideturtle()

t.exitonclick()