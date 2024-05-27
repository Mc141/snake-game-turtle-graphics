from turtle import Screen, time
from snake import Snake
from food import Food

screen = Screen()

screen.screensize(600, 600)
screen.setup(602, 602)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen._root.resizable(False, False)


snake = Snake()
food = Food()


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
    

    if snake.head.distance(food) <  15:
        food.refresh()


    screen.listen()
    
    


screen.mainloop()