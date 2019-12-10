from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math
import time
import numpy as np 
global x1,y1,x,y,x2,y2,N,tx,ty
def Init():
    glClearColor(0.0,0.0,1.0,0.0)
    gluOrtho2D(-350,350,-350,350)

def plotpoints(x,y,xend,yend):

    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(xend,yend)
    glEnd()
    glFlush()

def inp():
    global x1,y1,x,y,x2,y2,tx,ty
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    x=int(input("Enter x cordinate "))
    y=int(input("Enter y cordinate "))
    x1=int(input("Enter x1 cordinate "))
    y1=int(input("Enter y1 cordinate "))
    x2=int(input("Enter x2 cordinate "))
    y2=int(input("Enter y2 cordinate "))
    plotpoints(x,y,x1,y1)
    plotpoints(x1,y1,x2,y2)
    plotpoints(x,y,x2,y2)
    tx=int(input("translatin x"))
    ty=int(input("translatin y"))
    transf(x,y,tx,ty)
    xnew=N[0][0]
    ynew=N[1][0]
    transf(x1,y1,tx,ty)
    xnew=N[0][0]
    ynew=N[1][0]
    transf(x2,y2,tx,ty)
    xnew=N[0][0]
    ynew=N[1][0]
    plotpoints(x,y,x1,y1)
    plotpoints(x1,y1,x2,y2)
    plotpoints(x,y,x2,y2)
    


def transf(x,y,tx,ty):
    global N
    print("x ",x)
    print("y ",y)
    T=[[1,0,tx],[0,1,ty],[0,0,1]]
    C=[[x],[y],[1]]
    N=np.matmul(T,C)
    print("xnew", N[0][0])
    print("ynew", N[1][0])
     

def main():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("New")
    glutDisplayFunc(inp)
    Init()
    glutMainLoop()
    
main()