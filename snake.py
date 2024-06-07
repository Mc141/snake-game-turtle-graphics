from turtle import Turtle, Screen
import time

screen = Screen()
screen.tracer(0)

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.squares = []
        self.square_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.forward_distance = 20
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in self.square_positions:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle()
        square.color("white")
        square.shape("square")
        square.penup()
        square.goto(position)
        self.squares.append(square)

    def extend(self):
        old_position = self.squares[-1].position()
        self.add_segment(old_position)

    def move(self):
        for square_index in range(len(self.squares) - 1, 0, -1):
            new_position = self.squares[square_index - 1].position()
            self.squares[square_index].goto(new_position)

        self.squares[0].forward(self.forward_distance)

    def up(self):
        if self.squares[0].heading() != DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].setheading(DOWN)

    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].setheading(RIGHT)