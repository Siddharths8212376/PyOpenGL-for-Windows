from OpenGL.GL import *

from OpenGL.GLUT import *

from OpenGL.GLU import *

import numpy

from math import sin, cos

# from ddap import DDALine

import sys

import time



def init(): 

    glClearColor(1.0,1.0,1.0,1.0)

    glColor3f(1.0,0.0,0.0)

    glPointSize(3)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(0.0,640.0,0.0,500.0)





class Point:

    x=float(0)

    y=float(0)

    def setxy(self,x2,y2):

    

        self.x = (float)(x2)

        self.y = (float)(y2)

    

    def __eq__(self,rPoint):

    

        self.x = rPoint.x

        self.y = rPoint.y

        return self.x, self.y

    







def factorial(n):

    if (n<=1):

        return(1)

    else:

        n=n*factorial(n-1)

    return n





def binomial_coff(n,k):



    ans =(float)(factorial(n) / (factorial(k)*factorial(n-k)))

    return ans







abc=[]

SCREEN_HEIGHT = 500

points = 0

clicks = 4













def drawDot(x,y):

    glColor3f(0.0,1.0,0.0)

    glBegin(GL_POINTS)

    glColor3f(1.0,0.0,0.0)

    glVertex2f(x,y)

    glEnd()





def drawLine(p1,p2):

    glColor3f(0.0,0.0,1.0)

    glBegin(GL_LINES)

    glVertex2f(p1.x, p1.y)

    glVertex2f(p2.x, p2.y)

    glEnd()







def drawBezier(PT,t):

    P=Point()

    P.x = pow((1 - t), 3) * PT[0].x + 3 * t * pow((1 -t), 2) * PT[1].x + 3 * (1-t) * pow(t, 2)* PT[2].x + pow (t, 3)* PT[3].x

    P.y = pow((1 - t), 3) * PT[0].y + 3 * t * pow((1 -t), 2) * PT[1].y + 3 * (1-t) * pow(t, 2)* PT[2].y + pow (t, 3)* PT[3].y



    return P







def drawBezierGeneralized(PT,t):

    P=Point()

    P.x = 0

    P.y = 0

    for i in range(clicks):

    

        P.x = P.x + binomial_coff((float)(clicks-1),(float)(i)) * pow(t,(float)(i)) * pow((1-t),(clicks-i-1)) * PT[i].x

        P.y = P.y + binomial_coff((float)(clicks-1),(float)(i)) * pow(t,(float)(i)) * pow((1-t),(clicks-i-1)) * PT[i].y

    

    return P





def myMouse(button, state, x, y):

    global points

    #glPointSize(3)



    if(button == GLUT_LEFT_BUTTON and state == GLUT_DOWN):

        k=Point()

        k.setxy((float)(x),(float)(SCREEN_HEIGHT - y))

        abc.append(k)

        points=points+1



        drawDot(x, SCREEN_HEIGHT - y)





        if(points == clicks):

        

            

            for k in range(0,clicks-1):

                drawLine(abc[k], abc[k+1])



            p1 = abc[0]

            for t in numpy.arange(0.0,1.1,0.02):

            

                p2 = drawBezierGeneralized(abc,t)

                print(str(p1.x)+"  ,  "+str(p1.y))

                print(str(p2.x)+"  ,  "+str(p2.y))

                drawLine(p1, p2)

                p1 = p2

            

            # time.sleep(0.5)

            points = 0

    glFlush()

        

  







def myDisplay():

  #  glClearColor(1.0,1.0,1.0,1.0)

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0,1.0,0.0)

    glPointSize(5)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    gluOrtho2D(0.0,640.0,0.0,500.0)

    

    #glFlush()





def main():

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)

    glutInitWindowSize(640,500)

    glutInitWindowPosition(100,150)

    glutCreateWindow(b"Bezier Curve")

    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

    glutDisplayFunc(myDisplay)

    glutMouseFunc(myMouse)

    init()

    glutMainLoop()



main()