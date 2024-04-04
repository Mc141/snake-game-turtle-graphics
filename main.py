from turtle import Turtle, Screen, time
from snake import Snake

screen = Screen()

screen.screensize(600, 600)
screen.setup(602, 602)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    

snake = Snake()


screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')


game_is_running = True


while game_is_running:
    time.sleep(0.1)
    screen.update()
    
    snake.move()
    
    screen.listen()
    
    


screen.mainloop()