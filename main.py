from turtle import Screen
from snake import Snake
import time
window = Screen()
window.title("Snake Game v1.00")
window.setup(width=700, height=700)
window.bgcolor("black")
window.tracer(0)


# initial snake:
snaky= Snake()

game_on=True
while game_on:
    snaky.move()


    window.update()
    time.sleep(0.1)



window.exitonclick()