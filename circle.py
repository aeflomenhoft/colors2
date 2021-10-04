#Initialization
import turtle
import random
ally=turtle.Turtle()
turtle.colormode(255)

#Functions
def randomDot():
    ally.color(255,0,0)
    ally.begin_fill()
    ally.circle(150)
    ally.end_fill()

#Main
randomDot()
