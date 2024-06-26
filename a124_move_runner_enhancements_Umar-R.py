# Rayan Umar, Block 7

# Program Name: a124_move_runner_enhancements_Umar-R.py

# Purpose: The purpose of this program is to create a maze. 
# I will use iteration and sequencing to randomly place barriers and doors in different parts of the maze.
# I will also make a turtle object so that it can move around through the paths of the maze.
# In addition, I have 2 enhancements that add depth to my program. 
# The 1st enhancement causes the runner to stop when it hits a wall. 
# In addition, the runner will move automatically so that the user won't have to spam the move key.
# The 2nd enhancement creates a 2nd runner that so that 2 people can run through the maze.
# The 2nd runner, however, will function as a hunter who will try to catch the 1st runner in the maze.

# Import trtl as turtle
# Import random as rand
import turtle as trtl
import random as rand

# Create turtle called maze_creator
maze_creator = trtl.Turtle()

# Create maze runner turtle
# The shape of the maze runner will be a triangle,
# with the size being 0.45 and the color being red.
# The maze runner then goes to (40,-20), which is roughly
# the center of the maze and avoids colliding with the walls.
maze_runner = trtl.Turtle()
maze_runner.shape("triangle")
maze_runner.shapesize(0.45)
maze_runner.color("red")
maze_runner.penup()
maze_runner.goto(-40, 20)

# ENHANCEMENT 2: Maze Hunter turtle
# The shape of the maze hunter will be a triangle,
# with the size being 0.45 and the color being purple.
# The maze hunter then goes to (340,20), which will put
# the hunter right outside of the maze.

maze_hunter = trtl.Turtle()
maze_hunter.shape("triangle")
maze_hunter.shapesize(0.45)
maze_hunter.color("purple")
maze_hunter.penup()
maze_hunter.goto(340, 20)
maze_hunter.setheading(180)



# Set the turtle to speed to the max (Which is 0).
maze_creator.speed(0)

# Set the color of the maze to blue.
maze_creator.color("Blue")

# This variable will be used to increase the size of the wall.
wall_increaser = 160

# This variable will be used to make the width of the door later on in the program.
half_of_door_width = 20

# The up, down, left, and right functions give
# the maze runner a specific heading so that it can
# navigate the different turns of the maze.

def up():
    maze_runner.setheading(90)

def down():
    maze_runner.setheading(270)

def left():
    maze_runner.setheading(180)

def right():
    maze_runner.setheading(360)

# The move_runner function helps the maze runner
# move forward by 10 pixels.

def move_runner():
    maze_runner.pendown()
    maze_runner.forward(10)


    # ENHANCEMENT 1: Wall Collisions + Automatic Runner
    # determine if runner hits a wall
    wn_canvas = wn.getcanvas()
    x,y = maze_runner.position()
    margin = 5
    items = wn_canvas.find_overlapping(x+margin, -y+margin, x-margin, -y-margin)

    if (len(items) > 0):

    # get a property of the base object - the canvas
        canvas_color = wn_canvas.itemcget(items[0], "fill")

        if (canvas_color == "Blue"):
        # stop the game
            maze_runner.fillcolor("gray")
            wn.onkeypress(move_runner, 'g')
            maze_runner.forward(-10)
            return
# automatically move the runner
    wn.ontimer(move_runner, 300) # fires every 300 msec

# The up, down, left, and right functions give
# the maze hunter a specific heading so that it can
# navigate the different turns of the maze.

def hunter_up():
    maze_hunter.setheading(90)

def hunter_down():
    maze_hunter.setheading(270)

def hunter_left():
    maze_hunter.setheading(180)

def hunter_right():
    maze_hunter.setheading(360)

# The move_hunter function helps the maze hunter
# move forward by 10 pixels.

def move_hunter():
    maze_hunter.pendown()
    maze_hunter.forward(10)

    # Wall Collisions + Automatic Hunter
    # determine if hunter hits a wall

    wn_canvas = wn.getcanvas()
    x,y = maze_hunter.position()
    margin = 5
    items = wn_canvas.find_overlapping(x+margin, -y+margin, x-margin, -y-margin)

    if (len(items) > 0):

    # get a property of the base object - the canvas
        canvas_color = wn_canvas.itemcget(items[0], "fill")

        if (canvas_color == "Blue"):
        # stop the game
            maze_hunter.fillcolor("gray")
            wn.onkeypress(move_hunter, ';')
            maze_hunter.forward(-10)
            return
# automatically move the hunter
    wn.ontimer(move_hunter, 300) # fires every 300 msec


# The build_door function takes in the door
# as a parameter, where it will construct
# the door depending on what the random value of "door" is.

def build_door(door):
    maze_creator.forward(door)
    maze_creator.penup()
    maze_creator.forward(half_of_door_width*2)
    maze_creator.pendown()

# The build_barrier function takes in the barrier
# as a parameter, where it will construct
# the barrier depending on what the random value of "barrier" is

def build_barrier(barrier):
    maze_creator.forward(barrier)
    maze_creator.left(90)
    maze_creator.forward(half_of_door_width*2)
    maze_creator.forward(-half_of_door_width*2)
    maze_creator.right(90)

# The for loop below includes a nested while loop that helps
# build the maze with the use of the rand library so that
# the locations of the doors and barriers are randomized.

for i in range(25):

    maze_creator.left(90)
    

# randomize location of doors and barriers in wall
    door = rand.randint(half_of_door_width*2, (wall_increaser - half_of_door_width*2))
    barrier = rand.randint(half_of_door_width*2, (wall_increaser - half_of_door_width*2))

    while(abs(door - barrier) < half_of_door_width * 2):

        door = rand.randint(half_of_door_width*2, (wall_increaser - half_of_door_width*2))


     # Draw the barrier
     # Draw the door, subtracting what you drew for the barrier.
     # Finish drawing what is left of the wall

    if (door > barrier):
        build_barrier(barrier)
        build_door(door - barrier)
        maze_creator.forward(wall_increaser - door - half_of_door_width * 2)

    # Draw the door.
    # Draw the barrier, subtracting what you drew for the door as well as the width of the door.
    # Finish drawing what is left of the wall

    else:
        build_door(door)
        build_barrier(barrier - door - half_of_door_width * 2)
        maze_creator.forward(wall_increaser - barrier)


    wall_increaser = wall_increaser + half_of_door_width



# Persist the screen
wn = trtl.Screen()


# The keyboard will listen for these letters that correspond to the movement.
# When the user clicks one of the letters below,
# The runner will change its heading to face up (north), down (south), left (west), or right (east)
# The runner will move a certain amount when the user presses "g".

wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")
wn.onkeypress(move_runner, "g")

# The keyboard will listen for these letters that correspond to the movement.
# When the user clicks one of the letters below,
# The hunter will change its heading to face up (north), down (south), left (west), or right (east)
# The hunter will move a certain amount when the user presses ";".

wn.onkeypress(hunter_up, "i")
wn.onkeypress(hunter_down, "k")
wn.onkeypress(hunter_left, "j")
wn.onkeypress(hunter_right, "l")
wn.onkeypress(move_hunter, ";")

wn.listen()

# The last statement in a graphics program because it handles the events above.
wn.mainloop()

""" 
ENHANCEMENT 1 Documentation:

Issues Encountered:

Margin Calibration: Initially, the margin was set to zero, 
causing false negatives (not detecting wall collisions). Increasing the margin resolved this.

False Positives: At first, I did not check the color of the canvas items, leading to incorrect wall detection. 
Adding a condition to check if the overlapping item was blue solved this issue.

Solutions and Improvements:

- Adjusted the margin size to account for the turtle's size and avoid false negatives.
- Implemented a color check on the overlapping canvas items to prevent false positives.
- Used turtle.fillcolor("gray") to indicate that the runner stopped due to a wall collision.
- Disabled automatic movement after collision to prevent further unintended movements into walls.

Automatic Runner Movement:
To implement automatic movement for the maze runner, 
I used the ontimer method to call the move_runner() function at regular intervals. 
This eliminated the need to repeatedly press the move key to advance.

Timer Interval: Initially, the interval was set at 100 milliseconds, which was too fast, 
leading to collision detection issues. 
Increasing it to 300 milliseconds provided smoother movement and better collision handling.

Collision Handling: The automatic movement was stopped if a wall collision was detected, 
preventing the turtle from moving through walls.

Enhancement 1 achieved its goals of wall collision detection and automatic runner movement. 
By implementing these features, the maze runner program became more interactive 
and added a new level of challenge, as the runner stopped when it hit a wall, 
requiring careful navigation through the maze."""