from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput(title="make a bet",prompt="which one will win? enter a color:")
color=["red","orange","yellow","green","blue","purple"]
game=False
position=[-70,-40,-10,20,50,80]
my_turtle=[]
for turtle_number in range (0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_number])
    new_turtle.goto(x=-230, y=position[turtle_number])
    my_turtle.append(new_turtle)
if user_bet:
    game=True
while game:
    for turtle in my_turtle:
        if turtle.xcor()>230:
            game=False
            wining_color=turtle.pencolor()
            if wining_color==user_bet:
                    print(f"you won the bet : turtle {wining_color}")
            else:
                print(f"you lose the match, the win turtle is {wining_color}")
        lists_of_distance=random.randint(0,10)
        turtle.forward(lists_of_distance)
screen.exitonclick()  