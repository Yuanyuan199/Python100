
import turtle

def draw_rectangle(x, y, width, height):
    "Draw Rectangle"
    turtle.goto(x, y)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width/4)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

    turtle.goto(x+405 , y)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width/4)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_maple_leaf(x, y, scale):
    "Draw Maple leaf"
    def goto(x_offset, y_offset):
        turtle.goto(x + scale*x_offset, y + scale*y_offset)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.penup()
    goto(0,7)
    goto(-1.2,4.4)
    turtle.pendown()
    goto(-3,5)
    goto(-2,1)
    goto(-4, 3)
    goto(-4.3,1.5)
    goto(-7,2.5)
    goto(-5.5,0)
    goto(-7,-1)
    goto(-3.3,-3.4)
    goto(-4,-5)
    goto(-.2,-4.2)
    goto(-.2,-8)
    goto(0.2,-8,)
    goto(0.2,-4.2)
    goto(4,-5)
    goto(3.3,-3.4,)
    goto(7,-1,)
    goto(5.5,0)
    goto(7,2.5)
    goto(4.3,1.5)
    goto(4,3)
    goto(2,1)
    goto(3,5)
    goto(1.2,4.4,)
    goto(0,7)
    turtle.end_fill()

def main():
    turtle.speed(12)
    turtle.penup()
    x, y = -270, -180
    width, height = 540, 360
    draw_rectangle(x, y, width, height)
    
    draw_maple_leaf(0 ,0, 15)
    # Hide turtle
    turtle.ht()
    # Draw
    turtle.mainloop()


if __name__ == '__main__':
    main()