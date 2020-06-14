# Pre-import
# The turtle module is used to do basic graphics with Python 3. 
import turtle
import os

# Pong Logistics:
# Pong requires 3 main sprites: 2 paddles and a ball. The paddles only need to move up and down, and the ball must be able to
# bounce off when touch either the paddles or the horizontal walls. When the ball hits vertical walls, it will be returned at (0,0) and
# when it hits horizontal walls, it will bounce.

# A game window is created with the command [object] = turtle.Screen(), which holds the frame of this game.
# [object].title() write a title on top of the graphic frame.
# [object].bgcolor() allows the change in background color.
# [object].setup(width="", height="") allows the change in the frame dimensions. Note that (0,0) is in the middle and the
# dimension value is splitted 50% for each direction.
# [object].tracer() let the user to manually refresh the frame.
gamewindow = turtle.Screen()
gamewindow.title("Pong Game by Alan K. Nguyen")
gamewindow.bgcolor("white")
gamewindow.setup(width = 800, height = 600)
gamewindow.tracer(0)

# Here, we declare the existence of the three main objects: the two paddles and the ball.
# Declare First Paddle
# [object] = turtle.Turtle() declares the existence of the object as a Turtle object (Turtle is class name)
# [object].speed(0) allows the customization of the speed of animation (0 is maximum)
# [object].shape() determines the shape of the object.
# [object].color() determines the color of the object.
# [object].shapesize(stretch_wid= , stretch_len= ) allow the stretching of the shape in 2D.
# [object].penup() means that the object won't leave marks as it is moving.
firstpaddle = turtle.Turtle() 
firstpaddle.speed(0)
firstpaddle.shape("square")
firstpaddle.shapesize(stretch_wid=8, stretch_len=1) 
firstpaddle.color("blue")
firstpaddle.penup()
firstpaddle.goto(-350, 0)

# Declare Second Paddle
secondpaddle = turtle.Turtle()
secondpaddle.speed(0)
secondpaddle.shape("square")
secondpaddle.shapesize(stretch_wid=8, stretch_len=1) 
secondpaddle.color("red")
secondpaddle.penup()
secondpaddle.goto(350, 0)

# Declare Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)

# Declare Ball's Behavior
# The ball's behavior can be dissect into two main parts:
# 1. The part that has to do with the ball itself, like its move speed... This we configure in object declaration.
# 2. The part that has to do with the ball and the paddles, which we must configure in the Main Game Loop.
# [object].dx tells you the pixel change in the x axis of an object if it moves
# [object].dy tells you the pixel change in the y axis of an object if it moves
ball.dx = 0.20
ball.dy = 0.20

# Declare Scoring System
# [object].write("string", align="", font=("font_name", "font_size", "font_format")) allows us to print out an object that have
# letters on it.
# [object].hideturtle() allows the user to hide the object on the screen, only showing the writings on it.
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, -250)
scoring.write("Blue: 0  Red: 0", align ="center", font = ("Courier", 20, "normal"))

# Score variable declaration
score_a = 0
score_b = 0
    
# Here, we declare the functions for each of the object, basically telling them how to behave.    
# Declare Functions
# [object].ycor() returns the value of y coordinate of the object.
# [object].xcor() returns the value of x coordinate of the object.
# [object].sety(variable) Move the object to the y coordinate that have the value carried by the variable.
# [object].setx(variable) Move the object to the x coordniate that have the value carried by the variable.

def firstpaddle_up():
    y = firstpaddle.ycor()
    y += 15
    firstpaddle.sety(y)
    
def firstpaddle_down():
    y = firstpaddle.ycor()
    y -= 15
    firstpaddle.sety(y)
    
def secondpaddle_up():
    y = secondpaddle.ycor()
    y += 15
    secondpaddle.sety(y)
    
def secondpaddle_down():
    y = secondpaddle.ycor()
    y -= 15
    secondpaddle.sety(y)
    
# Keyboard Binding
# This part is used to bind the keyboard key-pressing with the functions that was defined to move the paddles.
# [object].listen() is used to tell the game window to listen to keyboard input and response.
# [object].onkeypress(function, key) is used to tell Turtle to link a certain keyboard input with a predefined function
gamewindow.listen()
gamewindow.onkeypress(firstpaddle_up, "w")
gamewindow.onkeypress(firstpaddle_down, "s")
gamewindow.listen()
gamewindow.onkeypress(secondpaddle_up, "Up")
gamewindow.onkeypress(secondpaddle_down, "Down")

    
# Main Game Loop (Always placed at the end for the program)
# [object].update() tells the main loop that every time it runs, the screen must be updated.
# [object].
while True:
    gamewindow.update()
    
    # Ball's Behavior
    # Ball's Movement
    # This basically means that everytime the frame gets updated, the ball x and y positions will be updated by adding its
    # initial position with each component of its speed (ball.dx and ball.dy) (s = 0.5(v + u)t))
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Ball's Behaviors with Walls
    # [object].dy *= -1 will reverse the direction of the ball vertically
    # [object].dx *= -1 will reverse the direction of the ball horizontally
    # [object].sety(y-coordinate) is used to place the object at the y coordinate specified.
    # [object].setx(x-coordinate) is used to place the object at the x coordinate specified.
    # [object].goto(x-coordinate, y-coordinate) is used to set the object at a certain coordinate.

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        scoring.clear()
        scoring.write("Blue: {}  Red: {}".format(score_a, score_b), align ="center", font = ("Courier", 20, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        scoring.clear()
        scoring.write("Blue: {}  Red: {}".format(score_a, score_b), align ="center", font = ("Courier", 20, "normal"))
         
    # Ball's Behaviors with Paddles
    # Explaination: When the ball's horizontal coordinate when past the 340 pixel point (which is pass the middle x coordinate of the
    # paddle), and the ball's vertical coordinate is "between" the middle of the paddle and 50 pixel up or down, the ball will change
    # direction. When the ball is detected to be in between 340 and 350 (or -340 and -350), it was setted back at 340 (and -340) and
    # change direction, as well as color.
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < secondpaddle.ycor() + 80) and (ball.ycor() > secondpaddle.ycor() - 80):
        ball.setx(340)
        ball.dx *= -1
        ball.color("red")
        
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < firstpaddle.ycor() + 80) and (ball.ycor() > firstpaddle.ycor() - 80):
        ball.setx(-340)
        ball.dx *= -1
        ball.color("blue")
        
        
        
        
    
    
    
    
    

