from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
GAME_ON = True
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.move = []
        self.create_snake()
        # self.up()

    def reset(self):
        for sn in self.move:
            sn.goto(1000, 1000)
        self.move.clear()
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            self.add(position)

    def add(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.move.append(snake)

    def extend(self):
        self.add(self.move[-1].position())

    def move_snake(self):

        for snake in range(len(self.move)-1, 0, -1):
            new_x = self.move[snake-1].xcor()
            new_y = self.move[snake-1].ycor()
            self.move[snake].goto(new_x, new_y)
        self.move[0].forward(MOVE_DIST)

    def up(self):
        if self.move[0].heading() != DOWN:
            self.move[0].setheading(UP)
        # self.move[0].left(90)

    def Down(self):
        if self.move[0].heading() != UP:
            self.move[0].setheading(DOWN)

    def left(self):
        if self.move[0].heading() != RIGHT:
            self.move[0].setheading(LEFT)

    def right(self):
        if self.move[0].heading() != LEFT:
            self.move[0].setheading(RIGHT)
