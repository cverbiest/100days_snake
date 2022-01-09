import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import  Scoreboard

screen = Screen()
screen.colormode(255)
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake")

snake = Snake()
snake.create_snake()
food = Food()

scoreboard = Scoreboard()

running = True

def quit():
    global running
    running = False


def info():
    print(snake)
    print(food)
    print(food.food_at_position(snake, False))
    print(snake.snake_status())

screen.listen()
screen.onkey(snake.pauze, "space")
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.onkey(quit, "q")
screen.onkey(info, "i")

screen.tracer(0)

#food.plant_food_at_position((120, 0))
#food.plant_food_at_position((140, 0))
food.food_add(snake)
snake.grow = 20
while running:
    scoreboard.update(snake, food)
    screen.update()
    snake.move_snake()
    if snake.snake_off_screen():
        print("You went off screen")
        snake.die()
        break
    if snake.snake_bites_tail:
        print("You bit your own tail")
        snake.die()
        break
    if not snake.pauzed:
        if food.food_at_position(snake):
            print("found food")
            snake.grow += 1

        food.food_scatter(snake)

    screen.update()
    time.sleep(0.15)
    # break

screen.update()
scoreboard.game_over()
screen.update()
print("Game over")
info()


screen.exitonclick()
