from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import numpy as np

global xc,yc,r,tx,ty,dx,dy,u,g,theta
g=-9.8
u=50
dx=0
dy=0

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-250,250,-250,250)

def idle():
    if anim==1:
        glutPostRedisplay()
def change_state():
    if anim==0:
        anim=1
    else: 
        anim=0
def mouse(bttn,state,x,y):
    if bttn==GLUT_LEFT_BUTTON:
        if state==GLUT_DOWN:
            change_state()

def plot_points():
    #to find the points to be plotted
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,1.0)
    dx=dx+3
    dy=dx*math.tan(theta)-0.5*g*dx**2*(1/float(u**2*math.cos(theta)))
    glPushMatrix()
    drawfig(dx,dy)
    glPopMatrix()
            
def set_pixel(x,y):
    #to set the pixels
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()
def drawfig(x_,y_):
    #to draw the circle
    segments=500
    for rad in range(segments):
        theta=2*3.14*rad/segments
        x_=radius*math.cos(theta)
        y_=radius*math.sin(theta)
        setp_pixel(x_+xc,y_+yc)    
def input1():
    #user input
    print("Enter the radius for the circle")
    r=int(input("Radius "))
    print("Enter the position/centre point for the object")
    xc=int(input("Enter the x coordinate"))
    yc=int(input("Enter the y coordinate"))    
        
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWIndowPostion(540,540)
    glutInitWindowSize(500,500)
    glutCreateWindow(b,"Projectile")
    input1()
    glutDisplayFunc(plot_points)
    glutIdleFunc(idle)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()
    
main()