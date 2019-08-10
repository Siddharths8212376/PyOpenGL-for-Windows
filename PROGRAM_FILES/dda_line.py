#DDA for positive slope
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def ROUND(a):
    return int(a + 0.5)
def myInit():

    glClearColor(0.0,1.0,1.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)

def readInput():
    global x0,y0,xEnd,yEnd
    x0,y0,xEnd,yEnd = input('cordinates: ')

def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()


def lineDDA(x0,y0,xEnd,yEnd):

    dx = abs(xEnd-x0)
    dy = abs(yEnd-y0)
    x,y=x0,y0
    steps = dx if dx > dy else dy
    
        xIncrement = dx/float(steps)
        yIncrement = dy/float(steps)
        setPixel(ROUND(x),ROUND(y))

        for k in range(steps):
       
            x+= xIncrement
            y+= yIncrement
            setPixel(ROUND(x),ROUND(y))  
def Display():
    
        glClear(GL_COLOR_BUFFER_BIT)
        lineDDA(x0,y0,xEnd,yEnd)


def main():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)
    glutCreateWindow("DDA Line Algorithum")
    readInput()
    glutDisplayFunc(Display)
    myInit()
    glutMainLoop()
main()
