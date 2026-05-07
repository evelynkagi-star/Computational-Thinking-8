from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("pond")


# TODO - create at least two variables and set their starting value. ex: cookies = 0
money = 0
cookies = 0
cost=10

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -300,100)
m1.hideturtle()



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def get_money():
    global money    
    money += 1 
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("money",x,y)
window.onkeypress(get_money, "space")
# When you press space a money sprite pops up on a random point on the screen and the money variable goes up +1
def get_cookie():
    global money, cookies, cost
    if money >= cost:
        cost = cost * 2
        cookies += 1
        x = -400 + 120*cookies
        y = -250
        create_sprite("cookie",x,y)
window.onkeypress(get_cookie, "b")
# if your money count is greater than the cost of the cookie pressing b will allow you to buy a cookie

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    m1.clear()
    m1.write(f"Money: {money}\nCost: {cost}\nCookies: {cookies}",font=("Arial",30,"normal"))

    if i % 100 == 0:
        money += 1*cookies 
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # m1.clear()
    # m1.write("Hello")

    time.sleep(0.01)
    window.update()