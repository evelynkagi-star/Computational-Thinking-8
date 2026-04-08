from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-270
y1 =200
x2 =-100
y2 =200
x3 =50
y3 =200
x4 =200
y4 =200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("flowers")
t1 = create_sprite("corgipixel",x1,y1)
t2 = create_sprite("turtle2",x2,y2)
t3 = create_sprite("cool_dog",x3,y3)
t4 = create_sprite("corgi",x4,y4)

#Sprite 1 is the fastest becasue it has the highest amount of speed the sprites can go to  # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(30):
    y1 -= random.randint(4,15)
    y2 -= random.randint(3,12)
    y3 -= random.randint(5,14)
    y4 -= random.randint(2,13)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("alien",-200,-200)
if y1 <= y2 and y1 <= y3 and y1 <= y4:
    s5.write("Player 1 wins!")
elif y2 <= y1 and y2 <= y3 and y2 <= y4:
    s5.write("player 2 wins!")
elif y3 <= y1 and y3 <= y2 and y3 <= y4:
    s5.write("player 3 wins!")
elif y4 <= y1 and y4 <= y2 and y4 <= y3:
    s5.write("player 3 wins!")
turtle.exitonclick()