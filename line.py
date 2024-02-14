from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(x=0,y=300)
        self.pendown()
        self.setheading(270)
        for _ in range(30):
            self.fd(10)
            self.penup()
            self.fd(10)
            self.pendown()