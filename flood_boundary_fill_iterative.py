#Program to plot a point

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time
from Algorithms.line_algorithm import line_algorithm
from Algorithms.circle_algorithms import circle_algorithms
sys.setrecursionlimit(1500)
# defining min_max boundaries
x_min, y_min = 4, 4
x_max, y_max = 100, 100
radius = 50
old_color = [0, 0, 0]  
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

# define the get-pixel and set-pixel functions
def set_pixel(x, y, color_code):
    glBegin(GL_POINTS)
    glColor3fv(color_code)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def get_pixel(x, y, pixels):
    glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_UNSIGNED_BYTE, None)
    

def flood_fill(x, y, fill_color, old_color):
    in_color = [0] * 3
    get_y = y + 250.0
    get_x = x + 250.0
    glReadPixels(get_x, get_y, 1.0, 1.0, GL_RGB, GL_FLOAT, in_color) 
    print (in_color)
    segments = 500
    for rad in range(segments):
        for i in range(radius):
            theta = 2 * 3.14159 * rad / segments
            x_ = i * math.cos(theta)
            y_ = i * math.sin(theta)
            set_pixel(x_, y_, fill_color)
		
        
    # if in_color != old_color:
      #   old_color = in_color
      #   return
    # if x ** 2  + y ** 2 > radius ** 2:
		# return
    # elif in_color != fill_color:
		# set_pixel(x, y, fill_color)
		# flood_fill(x - 1, y, fill_color, old_color)
		# flood_fill(x + 1, y, fill_color, old_color)
		# flood_fill(x, y + 1, fill_color, old_color)
		# flood_fill(x, y - 1, fill_color, old_color)
    # else:
		# return
 

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

    # min_X.dda_line()
    # min_Y.dda_line()
    # max_X.dda_line()
    # max_Y.dda_line()
    param_circle = circle_algorithms(radius, 0, 0)
    param_circle.parameteric_circle()
    glEnd()
    glFlush()
    flood_fill(0 , 0 , [0, 1, 0], old_color)


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
