from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xc):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.penup()
        self.speed("fastest")
        self.goto(x=xc,y=0)
        self.setheading(90)
        
    def up_left(self):
        if self.ycor()<275:
            self.fd(20)
        
    def up_right(self):
        if self.ycor()<275:
            self.fd(20)
        
    def down_left(self):
        if self.ycor()>-275:
            self.backward(20)
        
    def down_right(self):
        if self.ycor()>-275:
            self.backward(20)