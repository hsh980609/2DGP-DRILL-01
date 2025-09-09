import turtle

count=12
# c와의 차이는 괄호없이 "들여쓰기"로만 블럭을 구분하며,
# 조건에 대해서 괄호없이 사용.
while count>0:
    turtle.forward(100)
    turtle.left(30)
    count -= 1
else:
    print("count is zero")

turtle.exitonclick()