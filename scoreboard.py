from turtle import Turtle
from snake import Snake
from food import  Food

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(-280, 280)

    def update(self, snake: Snake, food: Food):
        if snake.pauzed:
            return
        self.clear()
        self.goto(-50, 280)
        self.write(f"length={len(snake.snake_parts)}", font=('Hack', 12, 'normal'))

    def game_over(self):
        self.goto(-100, 10)
        self.write("GAME OVER", font=('Hack', 30, 'bold'))
