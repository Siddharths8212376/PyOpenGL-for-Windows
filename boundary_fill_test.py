from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy 
import math
import sys
sys.setrecursionlimit(16000)
from Algorithms.circle_algorithms import circle_algorithms
def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glMatrixMode
    (GL_PROJECTION)
    gluOrtho2D(0,640,0,480)


def bound_it(x,y,fillColor,bc):
    color=glReadPixels(x,y,1.0,1.0,GL_RGB,GL_FLOAT)
    if((color!=bc).any() and (color!=fillColor).any()):
        glColor3f(fillColor[0],fillColor[1],fillColor[2])
        glBegin(GL_POINTS)
        glVertex2i(x,y)
        glEnd()
        glFlush()
        
        bound_it(x+1,y,fillColor,bc)
        bound_it(x-1,y,fillColor,bc)
        bound_it(x,y+1,fillColor,bc)
        bound_it(x,y-1,fillColor,bc)
    

def mouse(btn,state,x,y):
    y = 480-y
    if(btn==GLUT_LEFT_BUTTON):
        if(state==GLUT_DOWN):
              bCol= [1,0,0]
              color= [1,0,1]
              bound_it(x,y,color,bCol)

def world():
    glLineWidth(2)
    glPointSize(1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glBegin(GL_POINTS)
    circle = circle_algorithms(40.0, 250, 250)
    circle.parameteric_circle()
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(200,200)
    glutCreateWindow(b'flood fill and boundary fill')
    glutDisplayFunc(world)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()
   
main()

