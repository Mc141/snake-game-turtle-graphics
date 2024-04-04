from turtle import Turtle, Screen, time

screen = Screen()


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.square_x_posistions = [0, -20, -40]
        self.foward_distance = 20
        self.create_snake()
    

    def create_snake(self):
        for posisiton in self.square_x_posistions:
            square = Turtle()
            square.color("white")
            square.shape("square")
            square.penup()      
            square.goto(posisiton, 0)
            self.squares.append(square)
            
            
    def move(self):
        time.sleep(0.1)
        screen.update()
        for square_index in range(len(self.squares) - 1, 0, -1):
            old_x_posistion = self.squares[square_index - 1].xcor()
            old_y_posistion = self.squares[square_index - 1].ycor()
            self.squares[square_index].goto(old_x_posistion, old_y_posistion)

        self.squares[0].forward(self.foward_distance)
        
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