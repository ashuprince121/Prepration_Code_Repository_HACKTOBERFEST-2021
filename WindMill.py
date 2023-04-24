from turtle import Screen, Turtle

def rectangle(t):
    t.forward(50)
    t.left(90)
    t.backward(5)
    t.pendown()

    for _ in range(2):
        t.forward(10)
        t.right(90)
        t.forward(120)
        t.right(90)

    t.penup()

def windmill(t):
    for _ in range(4):
        t.penup()
        rectangle(t)
        t.goto(0, 0)

screen = Screen()
screen.tracer(0)

turtle = Turtle()
turtle.setheading(90)

def rotate():
    turtle.clear()
    windmill(turtle)
    screen.update()
    turtle.left(1)

    screen.ontimer(rotate, 40)  # adjust speed via second argument

rotate()

screen.mainloop()
