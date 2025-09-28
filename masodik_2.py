#masodik alkalom szünet után
import turtle


'''
def teglalap(x,y):
    #a = 5
    #b = 4
    ker = x * 2 + y * 2
    ter = x * x
    #print(ker)
    return ker, ter

a = 2
b = 3
eredmeny = teglalap(a,b)
print("A kerülete: ",eredmeny[0])
print("A területe: ",eredmeny[1])
'''
def negyszog(x, y):
    ker = x * 2 + y * 2
    ter = x * x
    if x==y:
        alagzat = "négyzet"
    else:
        alagzat = "téglalap"
    return ker, ter, alagzat


def negyzet():
    turtle.penup()
    turtle.goto(-50,50)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.pensize(5)

    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def pont(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(10,"black")

def dobas():
    import random
    turtle.hideturtle()
    turtle.clear()
    negyzet()
    szam = random.randint(1,6)
    if szam == 1:
        pont(0,0)
    elif szam == 2:
        pont(-30,30)
        pont(30, -30)
    elif szam == 3:
        pont(0,0)
        pont(-30, 30)
        pont(30, -30)
    elif szam == 4:
        pont(30, 30)
        pont(-30, -30)
        pont(-30, 30)
        pont(30, -30)
    elif szam == 5:
        pont(0,0)
        pont(30, 30)
        pont(-30, -30)
        pont(-30, 30)
        pont(30, -30)
    elif szam == 6:
        pont(30,0)
        pont(-30,0)
        pont(30, 30)
        pont(-30, -30)
        pont(-30, 30)
        pont(30, -30)



# app
ablak = turtle.Screen()
turtle.speed(0)
turtle.listen()
turtle.onkey(dobas, "d")
turtle.onkey(turtle.bye, "Escape")
turtle.mainloop()

#turtle.done()





'''
if __name__ == "__main__":
    a = 4
    b = 4
    eredmeny = negyszog(a, b)
    print(f"A {eredmeny[2]} kerülete: ",eredmeny[0])
    print(f"A {eredmeny[2]} kerülete: ",eredmeny[1])
    print("Saját hívás")
'''

