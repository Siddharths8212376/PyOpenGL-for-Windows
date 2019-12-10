from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys
# a - animate s - stop
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250, 250, -250, 250)

def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    # set of points
    Points = [[0,0], [0, 100], [100, 100], [100, 0], [50, -100]]
    # then no. of control points = len(Points) + 1 = 6
    n = 6
    # initialize matrix of Derivatives
    D = [0] * 6
    # define the y matrix
    y_matrix = []
    y_top = [Points[1] - Points[0]]
    y_bottom = [Points[n-2] - Points[n - 3]]
    y_mid = [Point[x] - Point[x - 2] for Point in Points[2:]]
    y_mid.append(y_bottom)
    y_mid.insert(0, y_top)
    
    y_matrix = y_mid
    # define the matrix
    # matrix will be of dimensions 6 * 6 
    spline_matrix = []
    mat_top = [2, 1]
    mat_bottom = []
    for i in range(n - 2):
        mat_top.append(0)
        mat_bottom.append(0)
    mat_bottom.append(2)
    mat_bottom.append(1)
    mat_mid = []
    k = 0
    mat_in = []
    for j in range(n - 2):
        mat_in.append(1)
        mat_in.append(4)
        mat_in.append(1)
        for i in range(n - 3):
            mat_in.append(0)
            k += 1
        mat_mid.append(mat_in)
        mat_in = [0] * k 
        
    mat_mid.append(mat_bottom)
    mat_mid.insert(0, mat_top)
    
    spline_matrix = mat_mid
    inverse_test = np.linalg.inv(spline_matrix)
    D_solutions = np.matmul(inverse_test, y_matrix)
    for i in range(len(D_solutions)):
        for l in range(100):
            t = 0.01 * l
            x = l
            y = y_matrix[i] + D_solutions[i] * t + (3 * (y_matrix[i + 1] - y_matrix[i]) - 2 * D_solutions[i] - D_solutions[i + 1]) * t ** 2 + ( 2 * (y_matrix[i] - y_matrix[i + 1]) + D_solutions[i] + D_solutions[i + 1]) * t ** 3
            glVertex2f(x, y)
            
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'cubic spline')
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()
    
main()