import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Maze Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Player setup
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.goto(-250, 250)

# Goal setup
goal = turtle.Turtle()
goal.shape("circle")
goal.color("green")
goal.penup()
goal.goto(200, -200)

# Wall setup
wall = turtle.Turtle()
wall.shape("square")
wall.color("black")
wall.penup()
walls = [(-200, 200), (-180, 200), (-160, 200), (-160, 180), (-160, 160),
         (-180, 160), (-200, 160), (-220, 160), (-240, 160)]
for pos in walls:
    wall.goto(pos)
    wall.stamp()

# Movement
def go_up():
    y = player.ycor()
    player.sety(y + 20)

def go_down():
    y = player.ycor()
    player.sety(y - 20)

def go_left():
    x = player.xcor()
    player.setx(x - 20)

def go_right():
    x = player.xcor()
    player.setx(x + 20)

# Keybinds
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Check Win
def check_win():
    if player.distance(goal) < 20:
        print("🎉 You Win!")

# Game loop
while True:
    screen.update()
    check_win()
