from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math
import numpy as np 

global rec
rec=[]
def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-250,250,-250,250)
    
def plot_points():
    global rec
    #setting up points to be plotted
    glClear(GL_COLOR_BUFFER_BIT)
    n=3
    for i in range (n):
        x1,y1=rec[i]
        x2,y2=rec[i+1]
        set_pixel(x1,y1,x2,y2)
    x1,y1=rec[0]
    x2,y2=rec[3]
    set_pixel(x1,y1,x2,y2)
    
def set_pixel(xi,yi,xf,yf):
    #printing the point
    glColor3f(0.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(xi,yi)
    glVertex2f(xf,yf)
    glEnd()
    glFlush()
def input1():
    #user input
    global rec
    print("Enter the coordinates for the sqaure")
    xmin=int(input("xmin "))
    ymin=int(input("ymin "))
    xmax=int(input("xmax "))
    ymax=int(input("ymax "))
    rec=[[xmin,ymin],[xmax,ymin],[xmax,ymax],[xmin,ymax]]
    
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowPosition(540,540)
    glutInitWindowSize(500,500)
    glutCreateWindow(b"squaretrans")
    input1()
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop() 
    
main()