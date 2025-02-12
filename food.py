from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.color("red")
        self.shape("circle")
        self.penup()
        self.shapesize(0.7)
        self.relocate()
    
    def relocate(self):
        random_xcor= random.randint(-330, 300)
        random_ycor= random.randint(-330, 300)
        self.goto(random_xcor, random_ycor)
