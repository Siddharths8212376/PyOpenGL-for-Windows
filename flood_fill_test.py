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


def fill_it(x,y,fillColor,prevColor):
    color=glReadPixels(x,y,1.0,1.0,GL_RGB,GL_FLOAT)
    if((color!=prevColor).any()):
        return
    glColor3f(fillColor[0],fillColor[1],fillColor[2])
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()
    glFlush()
    
    fill_it(x+1,y,fillColor,prevColor)
    fill_it(x-1,y,fillColor,prevColor)
    fill_it(x,y+1,fillColor,prevColor)
    fill_it(x,y-1,fillColor,prevColor)


def mouse(btn,state,x,y):
    y = 480-y
    if(btn==GLUT_LEFT_BUTTON):
        if(state==GLUT_DOWN):
              prevColor= [0,0,0]
              fillColor= [1,0,1]
              fill_it(x,y,fillColor,prevColor)

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

