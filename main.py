from turtle import Screen, time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.screensize(600, 600)
screen.setup(602, 602)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen._root.resizable(False, False)


snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')


game_is_running = True
snake_range = 280


while game_is_running:
    time.sleep(0.1)
    screen.update()
    
    snake.move()
    


    if snake.head.distance(food) <  15:
        food.refresh()
        score_board.current_score += 1   
        score_board.update(score_board.current_score)

    if snake.head.xcor() > snake_range or snake.head.xcor() < -snake_range - 20 or snake.head.ycor() > snake_range + 20 or snake.head.ycor() < -snake_range:
        game_is_running = False
        score_board.game_over()
    



    screen.listen()
    
    


screen.mainloop()