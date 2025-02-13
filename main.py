from turtle import Screen
from snake import Snake
from food import Food
import time
window = Screen()
window.title("Snake Game v1.00")
window.setup(width=700, height=700)
window.bgcolor("black")
window.tracer(0)
window.listen()


# initial snake:
snaky= Snake()
# control snake movement
window.onkey(fun=snaky.up, key="Up")
window.onkey(fun=snaky.down, key="Down")
window.onkey(fun=snaky.left, key="Left")
window.onkey(fun=snaky.right, key="Right")


#initial Food:
food= Food()

game_on=True
while game_on:
    snaky.move()

    #Detect collision with food
    if snaky.head.distance(food) < 15:
        food.relocate()

    # Detect collision with The wall:
    if ((snaky.head.xcor() > 330) or (snaky.head.xcor() < -330) or
        (snaky.head.ycor() > 330) or (snaky.head.ycor() < -330)):
        game_on =False

    # Detect collision with snake body:
    for part in snaky.all_part[0:-1]:
        if snaky.head.distance(part) < 5:
            game_on = False

    window.update()
    time.sleep(0.1)



window.exitonclick()