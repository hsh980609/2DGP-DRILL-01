import turtle

while True:
    shape=input("Enter Shape: ")
    if shape == "circle":
        turtle.circle(50)
    elif shape == "triangle":
        # 문장과 문장을 구분하기 위한 세미콜론
        # 독립적인 문장이란걸 알려주기위해 넣는 것임.
        turtle.forward(50); turtle.left(120)
        turtle.forward(50); turtle.left(120)
        turtle.forward(50)
    elif shape == "quit":
        break
    else:
        print("Wrong Shape")

turtle.bye()
