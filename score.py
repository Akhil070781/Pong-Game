from turtle import Turtle

class Score(Turtle):
    def __init__(self,xc,sc):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=xc,y=260)
        self.write(arg="0",move=False,font=("Arial",30,"normal"))
        self.score=sc
        
    def update(self):
        self.clear()
        self.write(arg=f"{self.score}",move=False,font=("Arial",30,"normal"))