import turtle             
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("White Square and Red Triangle")
kord = turtle.Turtle()
kord.color("white")


kord.left(180)
kord.penup()
kord.forward(300)
kord.pendown()

for i in [0,1,2,3]:
    kord.forward(50)
    kord.left(90)

kord.left(180)
kord.penup()
kord.forward(600)
kord.color("red")
kord.pendown()

for i in [0,1,2]:
    kord.forward(50)
    kord.right(120)

wn.mainloop()             
