from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

# declare all the required globals
global x_min, y_min, x_max, y_max, clipper
# required clipping limits
# specifying the polygon
global x_clip, y_clip, clip_polygon
x_clip = [-20, 30, 55, 70, 130]
y_clip = [40, 150, 140, 140, 20]
clip_polygon = list(zip(x_clip, y_clip))

# print clip_polygon
global save_vertices
save_vertices = []
# the sutherland hodgeman clip
# edges totally inside : add the 2nd vertex
# edges leaving: add intersection point
# edges entirely outside: add nothing
# edges entering: save intersection and inside points

# the sutherland hodgeman clip returns a set of vertices
def sutherland_hodgeman_clip(clip_polygon, clipper):
    for index, each_point in enumerate(clip_polygon[:-1]):
        x_init, y_init = each_point
        x_final, y_final = clip_polygon[index + 1]
        n = len(clip_polygon)
        
        left_clip(x_init, y_init, x_final, y_final)
        right_clip(x_init, y_init, x_final, y_final)
        top_clip(x_init, y_init, x_final, y_final)
        bottom_clip(x_init, y_init, x_final, y_final)

def left_clip(x_init, y_init, x_final, y_final):
    global x_min, save_vertices
    if x_final - x_init != 0:
        # calculate slope
        m = (y_final - y_init) / float(x_final - x_init)
    else:
        m = 1000
    
    # check for all the four conditions
    # 1. if both edges are inside, add the second vertex
    if x_init >= x_min and x_final >= x_min:
        save_vertices.append([x_final, y_final])
    
    # 2. for edges leaving, add intersection point
    elif x_init >= x_min and x_final < x_min:
        x_int = x_min
        y_int = m * (x_min - x_init) + y_init  
        save_vertices.append([x_int, y_int])
    
    # 3. for edges coming inside, add both inside and intersection
    elif x_init < x_min and x_final >= x_min:
        x_int = x_min
        y_int = m * (x_min - x_init) + y_init
        save_vertices.append([x_int, y_int])
        save_vertices.append([x_final, y_final])

def right_clip(x_init, y_init, x_final, y_final):
    global x_max, save_vertices
    
    if x_final - x_init != 0:
        # get the slope 
        m = (y_final - y_init) / float(x_final - x_init)
    else:
        m = 1000
    
    # both edges are inside, add final
    if x_init <= x_max and x_final <= x_max:
        save_vertices.append([x_final, y_final])
    # for edges leaving, add intersection point
    elif x_init <= x_max and x_final > x_max:
        x_int = x_max
        y_int = m * (x_max - x_init) - y_init
        save_vertices.append([x_int, y_int])
    # for edges coming in, add both intersection and inside point
    elif x_init > x_max and x_final <= x_max:
        x_int = x_max
        y_int = m * (x_max - x_init) - y_init
        save_vertices.append([x_int, y_int])
        save_vertices.append([x_final, y_final])

def top_clip(x_init, y_init, x_final, y_final):
    global y_max, save_vertices
    if x_final - x_init != 0:
        # get the slope 
        m = (y_final - y_init) / float(x_final - x_init)
    else:
        m = 1000
    # both edges are inside, add final
    if y_init <= y_max and y_final <= y_max:
        save_vertices.append([x_final, y_final])
    # for edges leaving, add intersection point
    elif y_init <= y_max and y_final > y_max:
        y_int = y_max
        x_int = x_init + m * (y_max - y_init)
        save_vertices.append([x_int, y_int])
    # for edges coming inside, add both intersection and inside point
    elif y_init >= y_max and y_final < y_max:
        y_int = y_max
        x_int = x_init + m * (y_max - y_init)
        save_vertices.append([x_int, y_int])
        save_vertices.append([x_final, y_final])

def bottom_clip(x_init, y_init, x_final, y_final):
    global y_min, save_vertices
    if x_final - x_init != 0:
        # get the slope 
        m = (y_final - y_init) / float(x_final - x_init)
    else:
        m = 1000
    # both edges are inside, add final
    if y_init >= y_min and y_final >= y_min:
        save_vertices.append([x_final, y_final])
    # for edges leaving, add intersection point
    elif y_init >= y_min and y_final < y_min:
        y_int = y_min
        x_int = x_init + m * (y_min - y_init)
        save_vertices.append([x_int, y_int])
    # for edges coming inside, add both intersection and inside point
    elif y_init <= y_min and y_final > y_min:
        y_int = y_min
        x_int = x_init + m * (y_min - y_init)
        save_vertices.append([x_int, y_int])
        save_vertices.append([x_final, y_final])
    
        
        

def set_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()
    
def dda_line(P_init, P_final):
    x_init, y_init = P_init
    x_final, y_final = P_final
    
    dx = x_final - x_init
    dy = y_final - y_init
    
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    x_inc, y_inc = dx / float(steps) , dy / float(steps)
    x, y = x_init, y_init
    for i in range(int(steps) + 1):
        set_pixel(x, y)
        x += x_inc
        y += y_inc
        
        
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)
    
def plot_points():
    global clipper, clip_polygon, save_vertices
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)

    # plot here
    # bres_line([0, 0], [100, 100])
    for index, point in enumerate(clipper[:-1]):
        dda_line(point, clipper[index + 1])
    dda_line(clipper[0], clipper[-1])
    
    glColor3f(0.0, 0.0, 1.0)
    for index, point in enumerate(clip_polygon[:-1]):
        dda_line(point, clip_polygon[index + 1])
    dda_line(clip_polygon[0], clip_polygon[-1])

    glColor3f(1.0, 1.0, 1.0)
    sutherland_hodgeman_clip(clip_polygon, clipper)
    for index, point in enumerate(save_vertices[:-1]):
        dda_line(point, save_vertices[index + 1])
    dda_line(save_vertices[0], save_vertices[-1])
    
def read_in():
    global x_min, y_min, x_max, y_max, clipper
    print 'Enter clipping coordinates : '
    x_min = int(input('enter min x '))
    y_min = int(input('enter min y '))
    x_max = int(input('enter max x '))
    y_max = int(input('enter max y '))
    clipper = [[x_min, y_min], [x_min, y_max], [x_max, y_max], [x_max, y_min]]
    
    
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'polygon_clipping')
    read_in()
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()

main()