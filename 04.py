import turtle

# define drawing
def drawSquare(t, sz)
    
    for i in range(4):  #same as repeat block
        t.forwad(sz)    
        t.left(90)

#define window
wn = turtle.screen()    # wn= window, don't forget parenthesis
wn.bgcolor("darkblue")  #background color

#define turtle and movements
elea = turtle.Turtle ()
drawSquare(elea, 50)

elea.penup()
elea.goto(100, 100)
elea.pendown()

drawSquare(elea, 75)

wn.exitonclick()  #end the window
