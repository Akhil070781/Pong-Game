import turtle
from paddle import Paddle
from ball import Ball
from score import Score
from line import Line
import time

screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)

left=Paddle(-390)
right=Paddle(380)

line=Line()    
ball=Ball()
screen.listen()

screen.onkeypress(fun=left.up_left,key="w")
screen.onkeypress(fun=right.up_right,key="Up")
screen.onkeypress(fun=left.down_left,key="s")
screen.onkeypress(fun=right.down_right,key="Down")

left_score=Score(-30,0)
right_score=Score(13,0)

game_is_on=True

while game_is_on:
    time.sleep(0.06)   
    screen.update()
    ball.move()
    
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
        
    if right.distance(ball)<50 and ball.xcor()>350:
        ball.bounce_x()
        
    elif left.distance(ball)<50 and ball.xcor()<-350:
        ball.bounce_x()
        
    if ball.xcor()<-380:
        ball.bounce_x()
        ball.home()
        right_score.score+=1
        right_score.update()
        
    if ball.xcor()>380:
        ball.bounce_x()
        ball.home()
        left_score.score+=1
        left_score.update()
        


screen.exitonclick()

