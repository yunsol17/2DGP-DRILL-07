import turtle
import random
import math

def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_maccoding(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)
    x1,y1 = p1[0],p1[1]
    x2,y2=p2[0],p2[1]

    a=(y2-y1)/(x2-x1)
    b= y1-x1*a
    for x in range(x1,x2+1,10):
        y=a*x+b
        draw_point((x,y))

    draw_point(p2)

def draw_line(a,b):
    for t in range(0,100000):
        t = math.radians(t)
        x = (a - b) * math.cos(t) + b * math.cos((a / b - 1) * t)
        y = (a - b) * math.sin(t) - b * math.sin((a / b - 1) * t)

        draw_point((x*10,y*10))



prepare_turtle_canvas()


draw_line(20,1)


turtle.done()