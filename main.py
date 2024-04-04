from turtle import Turtle, Screen, time

screen = Screen()

screen.screensize(600, 600)
screen.setup(602, 602)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


def left():
    squares[0].left(90)


squares = []
square_x_posistions = [0, -20, -40]

for square_index in range(0, 3):
    square = Turtle()
    square.color("white")
    square.shape("square")
    square.penup()
    square.goto(square_x_posistions[square_index], 0)
    squares.append(square)


game_is_running = True


while game_is_running:
    time.sleep(0.1)
    screen.update()

    for square_index in range(len(squares) - 1, 0, -1):
        old_x_posistion = squares[square_index - 1].xcor()
        old_y_posistion = squares[square_index - 1].ycor()
        squares[square_index].goto(old_x_posistion, old_y_posistion)

    squares[0].forward(20)

    screen.onkey(left, "a")
    screen.listen()

    
    



    





        





screen.mainloop()