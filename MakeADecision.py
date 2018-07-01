#leimportation
import time
from turtle import *
from random import randint
#randomshitpile1
print("How many options would you like to choose from?");
Decision = "";
Decision0 = "";
Decision1 = "";
Decision2 = "";
Decision3 = "";
Decision4 = "";
Decision5 = "";
options = int(input(""));
list1 = []
def optionish(i):
    end
def optionetc(i):
    end
#actualshitpile1
optionish = options
optionetc = options
while (options >= 1):
    print("Enter your option");
    Decision = input("");
    print("Option recorded..\n")
    list1.append(Decision)
    options = options - 1;
while (optionish >= 1):
    penup()
    goto(-210, 140-optionish*70)
    pendown()
    for steps in range(6):
        write(steps)
        forward(73.5)
    optionish = optionish - 1
    hideturtle()
penup()

#Decisions n shit
Decision0 = list1[0]
if optionetc > 1:
    Decision1 = list1[1]
if optionetc > 2:
    Decision2 = list1[2]
if optionetc > 3:
    Decision3 = list1[3]
if optionetc > 4:
    Decision4 = list1[4]
if optionetc > 5:
    Decision5 = list1[5]

#TURTLES

#fake turtles
finish = Turtle()
finish.up()
finish.speed(15)
finish.hideturtle()
finish.goto(230, 210)
finish.down()
finish.right(90)
finish.width(5)
for i in range(40+optionetc*5):
	finish.color("white")
	finish.forward(5)
	finish.color("black")
	finish.forward(5)

Nick = Turtle()
Nick.color('red')
Nick.shape("turtle")
Nick.penup()
Nick.goto(-210, 140-70)
Nick.pendown()


if (optionetc > 1):
    Nicki = Turtle()
    Nicki.color('orange')
    Nicki.shape("turtle")
    Nicki.penup()
    Nicki.goto(-210, 140-140)
    Nicki.pendown()
if (optionetc > 2):
    Nickic = Turtle()
    Nickic.color('yellow')
    Nickic.shape("turtle")
    Nickic.penup()
    Nickic.goto(-210, 140-210)
    Nickic.pendown()
if (optionetc > 3):
    Nickick = Turtle()
    Nickick.color('green')
    Nickick.shape("turtle")
    Nickick.penup()
    Nickick.goto(-210, 140-280)
    Nickick.pendown()
if (optionetc > 4):
    Nickickc = Turtle()
    Nickickc.color('blue')
    Nickickc.shape("turtle")
    Nickickc.penup()
    Nickickc.goto(-210, 140-350)
    Nickickc.pendown()
if (optionetc > 5):
    Nickickck = Turtle()
    Nickickck.color('purple')
    Nickickck.shape("turtle")
    Nickickck.penup()
    Nickickck.goto(-210, 140-420)
    Nickickck.pendown()
for turn in range(150):
    if (optionetc > 0):
        Nick.forward(randint(1, 5));
        if Nick.xcor() >= 230:
            Nick.back(250)
            Nick.write(Decision0 + " is yo answer", font=("Times New Roman", 15, "normal"))
            break
    if (optionetc > 1):
        Nicki.forward(randint(1, 5));
        if Nicki.xcor() >= 235:
            Nicki.back(250)
            Nicki.write(Decision1 + " is yo answer", font=("Times New Roman", 15, "normal"))
            break
    if (optionetc > 2):
        Nickic.forward(randint(1, 5));
        if Nickic.xcor() >= 235:
            Nickic.back(250)
            Nickic.write(Decision2 + " is yo answer", font=("Times New Roman", 15, "normal"))
            break
    if (optionetc > 3):
        Nickick.forward(randint(1, 5));
        if Nickick.xcor() >= 235:
            Nickick.back(250)
            Nickick.write(Decision3 + " is yo answer", font=("Times New Roman", 15, "normal"))
            break
    if (optionetc > 4):
        Nickickc.forward(randint(1, 5));
        if Nickickc.xcor() >= 235:
            Nickickc.write(Decision4 + " is yo answer", font=("Times New Roman", 15, "normal"))
            break
    if (optionetc > 5):
        Nickickck.forward(randint(1, 5));
        if Nickickck.xcor() >= 235:
            Nickickck.back(250)
            Nickickck.write(Decision5 + " is yo answer", font=("Times New Roman", 15, "normal"))
            break


    #lullaby
time.sleep(10)