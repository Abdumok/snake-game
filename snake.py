from turtle import Turtle

POSITION= [(0, 0), (20, 0), (40, 0)]

class Snake:
    def __init__(self):
        self.all_part= []
        self.create_snake()

    def create_snake(self):
        for pos in POSITION:
            part= Turtle()
            part.shape("square")
            part.color("white")
            part.penup()
            part.goto(pos)
            self.all_part.append(part)

    def move(self):
        # let any part of snake follow the part in front of it
        for i in range(len(self.all_part) - 1 ):
            self.all_part[i].goto(self.all_part[i+1].pos())
        # moving head of the snake
        self.all_part[-1].forward(20)
