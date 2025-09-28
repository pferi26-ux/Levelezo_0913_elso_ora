# r-re rajzol, q-ra kilép
import turtle

def rajzol():
    #fal
    turtle.clear()
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-75,-75)
    turtle.pendown()
    turtle.pencolor("black")
    for _ in range(4):
        turtle.forward(150)
        turtle.left(90)

    #ajto
    turtle.penup()
    turtle.goto(-50, -75)
    turtle.pendown()
    turtle.pencolor("brown")
    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)

    #kilincs
    turtle.penup()
    turtle.goto(-10, -25)
    turtle.pendown()
    turtle.dot(10, "black")

    # ablak
    turtle.penup()
    turtle.goto(10, 0)
    turtle.pendown()
    turtle.pencolor("black")

    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    #fal
    turtle.penup()
    turtle.goto(75,75)
    turtle.pendown()
    turtle.pencolor("red")

    for _ in range(2):
        turtle.left(120)
        turtle.forward(150)

# app
ablak = turtle.Screen()
turtle.hideturtle()
#turtle.speed(0)
turtle.listen()
turtle.onkey(rajzol, "r")
turtle.onkey(turtle.bye, "q")
turtle.mainloop()