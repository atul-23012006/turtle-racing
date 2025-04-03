from turtle import Screen ,Turtle
screen = Screen()
screen.listen()

'''def move():
    tim.forward(10)
screen.onkey(key="space",fun=move)
screen.exitonclick()'''


'''def w():
    tim.forward(10)
def s():
    tim.backward(10)
def a():
    tim.left(10)
def d():
    tim.right(10)
def c():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def sketch():
    screen.onkey(key="w",fun=w)
    screen.onkey(key="s", fun=s)
    screen.onkey(key="a", fun=a)
    screen.onkey(key="d", fun=d)
    screen.onkey(key="c", fun=c)
sketch()
screen.exitonclick()'''


colors=["red","orange","yellow","green","pink","purple"]
import random
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet: ",prompt="Which turtle will win the race? Enter a color: ")
turtle_list=[]
for i in range(3):
    cc = random.choice(colors)
    colors.remove(cc)
    tim=Turtle()
    turtle_list.append(tim)
    tim.speed("fastest")
    tim.shape("turtle")
    tim.penup()
    tim.color(cc)
    tim.goto(x=-230, y=(i+1)*50)
for i in range(3):
    cc = random.choice(colors)
    colors.remove(cc)
    tim = Turtle()
    tim.speed("fastest")
    turtle_list.append(tim)
    tim.shape("turtle")
    tim.penup()
    tim.color(cc)
    tim.goto(x=-230, y=-(i)*50)

is_race_on = False
if user_bet:
    is_race_on=True
while is_race_on:

    for t in turtle_list:
        if t.xcor()>230:
            is_race_on=False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won!! {winning_color} is the winning turtle")
            else:
                print(f"You've lost!! {winning_color} is the winning turtle")

        t.forward(random.randint(0,10))
screen.exitonclick()