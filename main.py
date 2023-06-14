from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def goUp(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def goDown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xMove = 10
        self.yMove = 10
        self.moveSpeed = 0.1

    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)

    def ybounce(self):
        self.yMove *= -1
        self.moveSpeed *= 0.8

    def xbounce(self):
        self.xMove *= -1
        self.moveSpeed *= 0.75

    def resetPos(self):
        self.hideturtle()
        self.goto(0, 0)
        self.moveSpeed = 0.1
        self.showturtle()
        screen.delay(3)
        self.xbounce()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreL = 0
        self.scoreR = 0
        self.updateScore()

    def updateScore(self):
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(-100, 225)
        self.write(self.scoreL, align="center", font=("Courier", 40, "bold"))
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.goto(100, 225)
        self.write(self.scoreR, align="center", font=("Courier", 40, "bold"))

    def pointL(self):
        self.scoreL += 1
        self.clear()
        self.updateScore()

    def pointR(self):
        self.scoreR += 1
        self.clear()
        self.updateScore()

    def checkWin(self):
        finish = False
        if self.scoreL == 3:
            self.clear()
            self.goto(0, 0)
            self.color("red")
            self.write("Red Wins", align="center", font=("Courier", 40, "bold"))
            finish = True
            return finish
        elif self.scoreR == 3:
            self.clear()
            self.goto(0, 0)
            self.color("blue")
            self.write("Blue Wins", align="center", font=("Courier", 40, "bold"))
            finish = True
            return finish
        return finish


paddleLeft = Paddle((-350, 0), "red")
paddleRight = Paddle((350, 0), "blue")
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddleRight.goUp, "Up")
screen.onkey(paddleRight.goDown, "Down")

screen.onkey(paddleLeft.goUp, "w")
screen.onkey(paddleLeft.goDown, "s")

game = True
while game:
    time.sleep(ball.moveSpeed)
    ball.move()

    # detect if ball hits wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ybounce()

    # detect if ball hit paddleRight
    if ball.distance(paddleRight) < 50 and ball.xcor() > 320:
        ball.xbounce()

    # detect if ball hit paddleLeft
    if ball.distance(paddleLeft) < 50 and ball.xcor() < -320:
        ball.xbounce()

    # detect when paddleRight or paddleLeft miss
    if ball.xcor() > 380:
        ball.resetPos()
        scoreboard.pointL()
        win = scoreboard.checkWin()
        if win:
            break
    if ball.xcor() < -380:
        ball.resetPos()
        scoreboard.pointR()
        win = scoreboard.checkWin()
        if win:
            break

screen.exitonclick()