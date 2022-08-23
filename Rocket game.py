import turtle,math,random


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
        self.fuel = 50
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
            
    



        

class Game:
    '''
    Purpose: an object of this class represents the game we are making
    Instance variables:
    player: the spacecraft that we are controlling
    obstacleList: a list of all the obstacle objects in the game

    Methods:
    __init__: constructor method that creates the initial player and sets the game environment
    gameloop: the loop that represents the frames and input time during the operation of the game
    
    
    '''
    def __init__(self):
        turtle.setworldcoordinates(0,0,1000,1000)
        turtle.delay(0)
        self.player = SpaceCraft(random.uniform(100,900),random.uniform(500,900),random.uniform(-5,5),random.uniform(-5,0))
        self.obstacleList = []
        for i in range(10):
            self.obstacle = Obstacles(random.uniform(50,950), random.uniform(50,950), 0)
            self.obstacleList.append(self.obstacle)
        self.gameloop()

        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.leftThrust, 'Left')
        turtle.onkeypress(self.player.rightThrust, 'Right')
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        gameOver = False
        self.player.move()
        for obstacle in self.obstacleList:
            obstacle.move()
            if(math.sqrt((self.player.xcor() - obstacle.xcor())**2 + (self.player.ycor() - obstacle.ycor())**2) <= 15):
                gameOver = True
        if(self.player.ycor() > 10 and gameOver == False):
            
            turtle.ontimer(self.gameloop, 30)
        elif((abs(self.player.vx) <= 4 and abs(self.player.vy) <= 4) and gameOver == False):
            turtle.write('Successful landing!')
        elif((abs(self.player.vx) > 4 and abs(self.player.vy) > 4) or gameOver == True): 
            turtle.write('You crashed!')
    






def main():
    Game()
    input('Press any key to exit... ')

main()
