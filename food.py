from turtle import Turtle
import random
from snake import Snake


class Food:
    
    food_collection = {}
    nt = Turtle('circle', visible=False)
    nt.color('red')
    nt.fillcolor('red')
    nt.penup()

    food_colors = [ "red", "orange", "pink", "purple" ]

    def food_scatter(self, snake: Snake):
        """add food if there is not enough left"""
        if len(self.food_colors) > 0 and random.randint(0, 10) == 5:
            self.food_add(snake)

    def food_add(self, snake: Snake):
        """add void avoiding snape_parts"""

        occupied = []
        for part in snake.snake_parts:
            occupied.append(part.pos())
        for part in self.food_collection:
            occupied.append(part)
        if len(occupied) >= 841:
            # Screen full 841=29*29
            return False

        while True:
            x = random.randint(-14, 14) * 20
            y = random.randint(-14, 14) * 20
            food_pos = (x, y)

            if food_pos in occupied:
                print(f"Already occupied {food_pos}")
            else:
                self.plant_food_at_position(food_pos)
                return True

    def plant_food_at_position(self, food_pos: Turtle.position):
        """Intervene to add food at specific location for test purposes"""
        food_color = self.food_colors.pop()
        self.nt.color(food_color)
        self.nt.setposition(food_pos)
        food = (self.nt.stamp(), food_color)
        self.food_collection[food_pos] = food
        print(f"drop {food[1]},{food[0]} at {food_pos}")

    def food_at_position(self, snake: Snake, eat=True):
        #if testpos in self.food_collection:
        #    self.nt.clearstamp(self.food_collection.pop(testpos))
        #    return True
        #return False
        testpos = snake.snake_head_pos()
        testpos = (int(round(testpos[0])), int(round(testpos[1])))
        print(f"test {testpos} for food")

        for part in self.food_collection:
            # print(f"test {testpos} against {part} {self.food_collection[part]} {part == testpos}")
            if part == testpos:
                food = self.food_collection.pop(part)
                if eat:
                    print(f"eat {food[1]},{food[0]} at {part}")
                    self.food_colors.append(food[1])
                    self.nt.clearstamp(food[0])
                return True
        return False

    def __str__(self):
        result = f"{self.food_collection}\n"
        result += f"{self.food_colors}"
        return result
