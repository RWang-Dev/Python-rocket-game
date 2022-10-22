import turtle, math, random
from space_craft import *
from obstacles import *

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