from turtle import*

def estrella(longitud):
       for i in range(5):
             forward(longitud)
             right(180 - 36)
             
def espiral_estrella():
       for i in range(72):
             estrella(300)
             right(5)
             
speed(0)
espiral_estrella()
input()