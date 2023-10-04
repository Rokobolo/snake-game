# Snake Game
The snake game built during the 20th and 21st day of python programming course.

## What does it do?
- Do I really have to explain how Snake works?
- Alright kids, sit and listen:
  - The snake is moving using directional keys towards a "piece of food".
  - Once the snake reaches the piece of food, it grows an extra segment (note: it starts with 3 segments)
  - If the snake's head touches a wall or a part itself, the game ends.
  - When the game ends, the high score is updated.

![ezgif com-video-cutter](https://github.com/Rokobolo/snake-game/assets/139471568/384908f0-7dcb-4f7e-9127-e3be24234b07)

 ## What is the goal?
- The goal of this project was to use everything I've learnt so far.
- The Snake game was built as an OOP project using 4 different .py files.

![image](https://github.com/Rokobolo/snake-game/assets/139471568/69fec25b-0fd9-4445-9438-63004477cb4b)

- food.py is creating the piece of food for the snake to chase.

- snake.py is managing the whole snake:
  - initializing it
  - adding parts
  - resetting it in case of game over
  - managing the code requires when an input is pressed

- scoreboard.py is managing the score and keeping track of the high score.
  - Everytime you hit game over, the highest score will be updated in a .txt file.
  - With this action, the game will remember your highest score on the next launch.
 
![image](https://github.com/Rokobolo/snake-game/assets/139471568/c580d9fa-0a24-4b55-94e7-ec6e4597bb87)

- main.py consolidate the whole project, uses turtle package to create the screen and manage the screen update.

## How to use?
- The assigned keys are:
  - "Up", "Down", Right" "Left"
- Move around and catch the food, get the highest score!

![image](https://github.com/Rokobolo/snake-game/assets/139471568/26d26e88-f1c8-4504-9c2c-60cfdba2d245)

  
