import turtle             
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("First and Last Initial")
kord = turtle.Turtle()
kord.color("white")


kord.left(180)
kord.penup()
kord.forward(300)
kord.pendown()

kord.right(80)
kord.forward(100)
kord.left(160)
kord.forward(100)
kord.right(160)
kord.forward(100)
kord.left(160)
kord.forward(100)

kord.penup()
kord.left(100)
kord.forward(350)

kord.left(180)

kord.color("red")
kord.pendown()

for i in range(180):
    kord.forward(1)
    kord.right(1)

wn.mainloop()             
