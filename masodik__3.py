# 150 px egyenlő szárú 3 szög piros, h-betűre rajzol, q-ra kilép
import turtle

def haromszog():

    turtle.clear()
    turtle.penup()
    turtle.goto(-75,-75)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.pensize(5)

    for _ in range(3):
        turtle.forward(150)
        turtle.left(120)

# app
ablak = turtle.Screen()
turtle.hideturtle()
turtle.speed(0)
turtle.listen()
turtle.onkey(haromszog, "h")
turtle.onkey(turtle.bye, "q")
turtle.mainloop()