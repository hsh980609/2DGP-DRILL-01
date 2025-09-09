import turtle
import random

turtle.shape("turtle")
while(True):
    turtle.setheading(random.randint(0,30))
    turtle.forward(random.randint(100,120))
    turtle.stamp()
