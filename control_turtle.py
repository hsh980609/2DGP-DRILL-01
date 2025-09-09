import turtle

def move_D():
    turtle.stamp()
    turtle.seth(0)
    turtle.forward(50)

def move_W():
    turtle.stamp()
    turtle.seth(90)
    turtle.forward(50)

def move_A():
    turtle.stamp()
    turtle.seth(180)
    turtle.forward(50)

def move_S():
    turtle.stamp()
    turtle.seth(270)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape("turtle")

turtle.onkey(restart,"Escape")

turtle.onkey(move_D,"D")
turtle.onkey(move_D,"d")

turtle.onkey(move_W,"W")
turtle.onkey(move_W,"w")

turtle.onkey(move_A,"A")
turtle.onkey(move_A,"a")

turtle.onkey(move_S,"S")
turtle.onkey(move_S,"s")

turtle.listen()
turtle.mainloop()