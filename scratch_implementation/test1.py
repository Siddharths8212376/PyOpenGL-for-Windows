from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys
import numpy as np 

global x1,y1,x2,y2,x3,y3
def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-250,250,-250,250)
    
def input():
    #input
    global x1,y1,x2,y2,x3,y3
    print("Enter the coordinates")
    x1=int(input("x1"))
    y1=int(input("y1"))
    x2=int(input("x2")) 
    y2=int(input("y2"))
    x3=int(input("x3"))
    y3=int(input("y3"))
    
    plot_points(x1,y1,x2,y2)
    plot_points(x2,y2,x3,y3)
    plot_points(x3,y3,x1,y1)
    

def plot_points(xi,yi,xf,yf):
    #to plot points
    glClear(COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(xi,yi)
    glVertex2f(xf,yf)
    glEnd()
    glFLush()    
    #def trans():
    #to do translation calc

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(500,500)
glutInitWindowPosition(540,540)
glutCreateWindow(b"test1")
glutDisplayFunc(input)
init()
glutMainLoop()
    
    