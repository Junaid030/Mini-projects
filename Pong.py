import turtle

win = turtle.Screen()
win.title("Ping Pong Game")
win.bgcolor("black")
win.setup(width =900, height=700)
win.tracer(0)


#Score
score_1 = 0
score_2 = 0

#adding the bat
paddle_1 =turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-400,0)

#adding the second bat
paddle_2 =turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(400,0)

#adding the ball
ball =turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 0.18
ball.dy = -0.18


#adding the score card using pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("\t Score Card \n Player A : 0  Player B : 0".format(score_1 , score_2), align="center" , font=("courier", 15,"normal") )


#Function for moving both bats
#first bat

def paddle_1_up():
    y= paddle_1.ycor()
    y+=20
    paddle_1.sety(y)

def paddle_1_down():
    y= paddle_1.ycor()
    y-=20
    paddle_1.sety(y)

#second bat

def paddle_2_up():
    y= paddle_2.ycor()
    y+=20
    paddle_2.sety(y)

def paddle_2_down():
    y= paddle_2.ycor()
    y-=20
    paddle_2.sety(y)

#Assigning the control to the first bat or key binding

win.listen()
win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down,"s")

#Assigning the control to the second bat or key binding
win.listen()
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down,"Down")



#game loop
while True:
    win.update()


    #movement of the ball

    ball.setx((ball.xcor()+ball.dx))
    ball.sety((ball.ycor()+ball.dy))

    #border setting

    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy*= -1
    
    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy*= -1

    if ball.xcor() > 440:
        ball.goto(0,0)
        ball.dx *=-1
        score_1 +=1
        pen.clear()
        pen.write("\t Score card \n Player A : {}  Player B : {}".format(score_1 , score_2), align="center" , font=("courier", 15,"normal") )


    if ball.xcor() < -440:
        ball.goto(0,0)
        ball.dx *=-1
        score_2 += 1
        pen.clear()
        pen.write("\t Score card \n Player A : {}  Player B : {}".format(score_1 , score_2), align="center" , font=("courier", 15,"normal") )



    #setting the bat and ball meetup

    if (ball.xcor() > 390 and ball.xcor() <400) and (ball.ycor() < (paddle_2.ycor() + 60)and ball.ycor() > (paddle_2.ycor()-60) ):
        ball.setx(390)
        ball.dx *= -1

    if (ball.xcor() < -390 and ball.xcor() > -400) and (ball.ycor() < (paddle_1.ycor() + 55)and ball.ycor() > (paddle_1.ycor()-55) ):
        ball.setx(-390)
        ball.dx *= -1
