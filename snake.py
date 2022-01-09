from turtle import Turtle, Screen

class Snake:
    direction: int = 0
    snake_parts: list[Turtle] = []
    grow: bool = False
    pauzed: bool = False

    def color_part(self, nt, i):
        if i == 0:
            # make head of snake green
            nt.color('green')
            nt.fillcolor('darkgreen')
        else:
            nt.color('green')
            nt.fillcolor('yellow')

    def create_snake(self):
        for i in range(3):
            nt = Turtle('circle')
            self.color_part(nt, i)
            nt.penup()
            nt.setposition(i * -20, 0)
            self.snake_parts.append(nt)

    def snake_head_pos(self) -> Turtle.position:
        return self.snake_parts[0].pos()

    def turn_left(self):
        self.snake_parts[0].left(90)

    def turn_right(self):
        self.snake_parts[0].right(90)

    def go_right(self):
        self.snake_parts[0].setheading(0)

    def go_up(self):
        self.snake_parts[0].setheading(90)

    def go_left(self):
        self.snake_parts[0].setheading(180)

    def go_down(self):
        self.snake_parts[0].setheading(270)

    def pauze(self):
        self.pauzed = not self.pauzed
        if self.pauzed:
            print(f"pauzing at {self.snake_head_pos()}")

    def move_snake(self):
        if self.pauzed:
            return
        def new_pos(pos):
            move_matrix = [(20, 0), (0, 20), (-20, 0), (0, -20)]
            return (
                pos[0] + move_matrix[self.direction][0],
                pos[1] + move_matrix[self.direction][1]
            )

        if self.grow:
            nt = self.snake_parts[0].clone()
            nt.forward(20)
            # demote old head
            self.color_part(self.snake_parts[0], 1)
            # add new head
            self.snake_parts.insert(0, nt)
            self.grow = False
        else:
            for i in range(len(self.snake_parts) - 1, 0, -1):
                self.snake_parts[i].goto(self.snake_parts[i - 1].pos())
            self.snake_parts[0].forward(20)

    def snake_bites_tail(self) -> bool:
        for tail_part in self.snake_parts[1::]:
            if tail_part.pos() == self.snake_parts[0].pos():
                tail_part.color("red")
                return True
        return False

    def snake_off_screen(self) -> bool:
        outer_size = (300, 300)

        tp = self.snake_parts[0].pos()
        if abs(tp[0]) >= outer_size[0] or abs(tp[1]) >= outer_size[1]:
            return True
        else:
            return False

    def die(self):
        for part in self.snake_parts:
            part.color("gray")

    def snake_status(self) -> str:
        return f"off screen:{self.snake_off_screen()} bites tail:{self.snake_bites_tail()}"

    def __str__(self):
        result = f"snake at {self.snake_head_pos()} len{len(self.snake_parts)}"
        return result
