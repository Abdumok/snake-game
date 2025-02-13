from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-300, 330)
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self.score}', font=('arial', 12, 'bold'), align='center' )