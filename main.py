from turtle import Turtle, Screen

screen = Screen()

screen.screensize(600, 600)
screen.setup(602, 602)
screen.bgcolor("black")
screen.title("Snake Game")

sqaures = []
square_x_posistions = [-40, -20, 0]

for square_index in range(0, 3):
    square = Turtle()
    square.color("white")
    square.shape("square")
    square.penup()
    square.goto(square_x_posistions[square_index], 0)
    sqaures.append(square)










screen.mainloop()