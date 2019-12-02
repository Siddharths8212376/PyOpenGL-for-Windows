from line_algorithm import line_algorithm
# doing the cohen-sutherland line clipping algorithm
# define all the points
inside = 0
left = 1
right = 2
bottom = 4
top = 8
# defining min_max boundaries
x_min, y_min = 4, 4
x_max, y_max = 100, 100
# define compute code funtionality
def computeCode(x, y):
    code = inside
    if x < x_min:
        code |= left
    elif x > x_max:
        code |= right
    elif y < y_min:
        code |= bottom
    elif y > y_max:
        code |= top
    return code
#Program to plot a point

def cohenSutherlandClip(x1, y1, x2, y2): 
  
    # Compute region codes for P1, P2 
    code1 = computeCode(x1, y1) 
    code2 = computeCode(x2, y2) 
    accept = False
  
    while True: 
  
        # If both endpoints lie within rectangle 
        if code1 == 0 and code2 == 0: 
            accept = True
            break
  
        # If both endpoints are outside rectangle 
        elif (code1 & code2) != 0: 
            break
  
        # Some segment lies within the rectangle 
        else: 
  
            # Line Needs clipping 
            # At least one of the points is outside,  
            # select it 
            x = 1.0
            y = 1.0
            if code1 != 0: 
                code_out = code1 
            else: 
                code_out = code2 
  
            # Find intersection point 
            # using formulas y = y1 + slope * (x - x1),  
            # x = x1 + (1 / slope) * (y - y1) 
            if code_out & top: 
                
                # point is above the clip rectangle 
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1) 
                y = y_max 
  
            elif code_out & bottom: 
                  
                # point is below the clip rectangle 
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1) 
                y = y_min 
  
            elif code_out & right: 
                  
                # point is to the right of the clip rectangle 
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1) 
                x = x_max 
  
            elif code_out & left: 
                  
                # point is to the left of the clip rectangle 
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1) 
                x = x_min 
  
            # Now intersection point x,y is found 
            # We replace point outside clipping rectangle 
            # by intersection point 
            if code_out == code1: 
                x1 = x 
                y1 = y 
                code1 = computeCode(x1,y1) 
  
            else: 
                x2 = x 
                y2 = y 
                code2 = computeCode(x2, y2) 
  
    if accept: 
        # print ("Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1,y1,x2,y2)) 
        return [int(x1), int(y1)], [int(x2), int(y2)]
        # Here the user can add code to display the rectangle 
        # along with the accepted (portion of) lines 
  
    else: 
        # print("Line rejected")
        return None

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time
from line_algorithm import line_algorithm

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)


def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)

    min = [x_min, y_min]
    max = [x_max, y_max]
    X = [x_max, y_min]
    Y = [x_min, y_max]
    min_X = line_algorithm(min, X)
    min_Y = line_algorithm(min, Y)
    max_X = line_algorithm(max, X)
    max_Y = line_algorithm(max, Y)
    min_X.dda_line()
    min_Y.dda_line()
    max_X.dda_line()
    max_Y.dda_line()
    r_x = [0, 0]
    r_y = [200, 100]
    line_random = line_algorithm(r_x, r_y)
    # line_random.dda_line()
    final_begin, final_end = cohenSutherlandClip(0, 0, 200, 100)
    final_line = line_algorithm(final_begin, final_end)
    final_line.dda_line()
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'plot_all_points')
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()


main()
