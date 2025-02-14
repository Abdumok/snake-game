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

    def game_over(self):
        self.clear()
        self.screen.bgcolor('medium violet red')
        self.goto(0, 50)
        self.write("*---------Game Over-----------*", font=("arial", 18, "bold"), align="center")
        self.goto(0, 0)
        self.write(f"Your Score: {self.score}", font=("arial", 18, "bold"), align="center")


    def increase(self):
        self.score += 1
        self.clear()
        self.write_score()