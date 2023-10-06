import turtle
import random
import time

delay=0.1
score=0

#snake bodies
bodies=[]

#Getting a screen
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("yellow")
s.setup(width=600, height=600)

#Create Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.fillcolor("gray")
head.penup()
head.goto(0,0)
head.direction="stop"

#Snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#Scoreboard
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("blue")
sb.penup()
sb.ht()
sb.goto(-200,-200)
sb.write("score: 0")

def moveup():
    if head.direction!="down":
        head.direction="up"

def movedown():
    if head.direction!="up":
        head.direction="down"
    
def moveleft():
    if head.direction!="right":
        head.direction="left"

def moveright():
    if head.direction!="left":
        head.direction="right"

def movestop():
    head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#Event Handling
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")

#Main Loop
while True:
    s.update()

    if head.xcor()>290:
        head.setx(-290)

    if head.xcor()<-290:
        head.setx(290)

    if head.ycor()>290:
        head.sety(-290)

    if head.ycor()<-290:
        head.sety(290)

    if head.distance(food)<20:
            
        #Move the food to new random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #increase the length of the snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("black")
        body.fillcolor("red")
        bodies.append(body)

        #Increase the score
        score += 10

        #Change delay
        delay -= 0.001
        
        sb.clear()
        sb.write("score: {}".format(score))

    #Move the snake body
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
    
    #Check collision with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction ="stop"

            #Hide body
            for body in bodies:
                body.ht()
            bodies.clear()

            score = 0
            delay = 0.1

            #update score board
            sb.clear()
            sb.write("score: {}".format(score))
    time.sleep(delay)
s.mainloop()