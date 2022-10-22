import turtle

class Obstacles(turtle.Turtle):
    '''
    Purpose: an object of this class represents the obstacles in the game
    Instance variables:
    x: the x position of the obstacle
    y: the y position of the obstacle
    vy: the initial y velocity of the obstacle
    rad: the radius of the obstacle
    Methods:
    __init__: constructor method that creates the initial obstacle and sets the position and draws the blue dot as the obstacle
    move: moves the obstacle according to gravity laws
    '''

    def __init__(self, x, y, vy):
        turtle.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.vy = vy
        self.rad = 15/2
        self.hideturtle()
        self.penup()
        self.setpos(self.x, self.y)
        self.dot(15, 'Blue')

    def move(self):
        self.vy = self.vy - 0.0486
        yPos = self.ycor() + self.vy
        self.setpos(self.x,yPos)
        if(self.ycor() <= 10):
            self.setpos(self.x,950)
        self.clear()
        self.dot(15, 'Blue')