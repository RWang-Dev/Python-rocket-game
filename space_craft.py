import turtle,math

class SpaceCraft(turtle.Turtle):
    '''
    Purpose: an object of this class represents a play controlled space craft
    Instance variables: 
    vx: initial x velocity
    vy: initial y velocity
    fuel: the amount of fuel the spacecraft has
    x: the initial x pos
    y: the initial y pos
    Methods:
    __init__: constructor method that sets up the initial variables
    move: simulates gravity by constantly subtracting the y velocity
    thrust: Moves the rocket up with each press of the up key and reduces the fuel
    leftthrust: turns the rocket left when the left arrow is pressed
    righthrust: turns the rocket right when the right arrow is pressed 
    '''

    def __init__(self, x, y, vx, vy):
        turtle.Turtle.__init__(self)
        self.vx = vx
        self.vy = vy
        self.fuel = 500
        self.left(90)
        self.penup()
        self.speed(0)
        self.setpos(x,y)

    def move(self):
        self.vy = self.vy - 0.0486
        xPos = self.xcor() + self.vx
        yPos = self.ycor() + self.vy
        self.setpos(xPos,yPos)

    def thrust(self):
        if(self.fuel > 0):
            self.fuel -= 1
            angle = math.radians(self.heading())
            self.vx += math.cos(angle)
            self.vy += math.sin(angle)
            print(self.fuel)
        else: print('Out of fuel')

    def leftThrust(self):
        if(self.fuel > 0):
            self.fuel -= 1
            self.left(15)
            print(self.fuel)
        else: print('Out of fuel')

    def rightThrust(self):
        if(self.fuel > 0):
            self.fuel -= 1
            self.right(15)
            print(self.fuel)
        else: print('Out of fuel')