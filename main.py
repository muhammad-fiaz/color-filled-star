import turtle as t #importing turtle
t.speed(0)
t.bgcolor("white") #background color
t.title("Star Animation") #turtle window title
t.hideturtle()
def star():
    c = ["maroon", "red", "purple", "blue", "aqua", "pink", "hot pink", "yellow", "orange"]  # star colors
    a = 700
    for i in range(a//50):
            t.penup()
            t.goto(0, 0)
            t.fd(a/2)
            t.rt(162)
            t.pendown()
            t.begin_fill()
            t.color(c[i%7])
            for j in range(5):
                t.fd(a)
                t.rt(144)
            t.end_fill()
            t.rt(144+60)
def dis():
    i=1
    while (i >0): #infinite loop
        star() #calling function here
        i+=1

dis()#calling function
t.mainloop()