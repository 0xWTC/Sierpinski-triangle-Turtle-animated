''' Draw an animated Sierpinski triangle using Turtle graphics. 
    The triangle is drawn using recursion.
    You can choose the number of iterations.
    The number of iterations is the depth of the recursion.
    https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle '''

import turtle

def draw_triangle(points, color, my_turtle):
    ''' Draw a triangle with the given points.'''
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    ''' Return the midpoint between the two points. '''
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, my_turtle, depth):
    ''' Draw a Sierpinski triangle with the given points using the given turtle
        at the given depth.
        The triangle is drawn using recursion. '''
    draw_triangle(points, "white", my_turtle)
    if depth > 0:
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   my_turtle, depth-1)
        sierpinski([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                   my_turtle, depth-1)
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                   my_turtle, depth-1)

def main(n):
    ''' Draw a Sierpinski triangle using turtle graphics'''
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-300, -100], [0, 300], [300, -100]]
    sierpinski(my_points, my_turtle, n)
    my_win.exitonclick()

if __name__ == '__main__':
    print("Enter the depth of the Sierpinski triangle(more than 5 is very slow): ")
    n = int(input())
    main(n)