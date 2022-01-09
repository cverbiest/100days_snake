import time
from turtle import Screen
from snake import Snake
from food import Food


screen = Screen()
screen.colormode(255)
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake")


snake = Snake()
snake.create_snake()
food = Food()
running = True

def quit():
    global running
    running = False


def info():
    print(snake)
    print(food)
    print(food.food_at_position(snake, False))

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

while running:
    screen.update()
    snake.move_snake()
    if snake.snake_off_screen():
        print("You went off screen")
        snake.die()
        break
    if snake.snake_bites_tail():
        print("You bit your own tail")
        snake.die()
        break
    if not snake.pauzed:
        if food.food_at_position(snake):
            print("found food")
            snake.grow = True

        food.food_scatter(snake)

    screen.update()
    time.sleep(0.15)
    # break

screen.update()
print("Game over")
info()
print(snake.snake_status())

screen.exitonclick()
