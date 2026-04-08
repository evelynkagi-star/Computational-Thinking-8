# Section 1 - Your code
from utils import *
set_background("antarctica")

s1 = create_sprite("dog", 100, 100)
s2 = create_sprite("fish", -200, 200)
s2 = create_sprite("turtle", -100, -100)
s2 = create_sprite("sea lion", 200, -200)

message1 = create_sprite("alien",-200,200)
message1.color("pink")
message1.write("Hola mi amigos",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()
