from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

global anim, x, y, hvel, vvel, radius
global x_border, y_border

x = 0.56
y = 0.34
dtime = 0.0005
radius = 0.1
hvel = 0.75
vvel = 2.0

# adding the window dimensions
width = height = 600
x_border = y_border = axrng = 1.0

# no animation to start
anim = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3ub(255, 0, 0)
    
    # dimensions of the screen
    gluOrtho2D(-axrng, axrng, -axrng, axrng)
    
def idle():
    if anim == 1:
        glutPostRedisplay()

def plotfunc():
    global x, y, hvel, vvel, radius
    glClear(GL_COLOR_BUFFER_BIT)
    
    # changes x and y
    x += hvel * dtime
    # adding the effect of gravity
    vvel = vvel - 9.8 * dtime
    
    if y <= -axrng + radius:
        y = -axrng + radius
    # keep the motion mathematics
    # safe from harm
    glPushMatrix()
    
    glTranslate(x, y, 0)
    glutSolidSphere(radius, 50, 50)
    glPopMatrix()
    
    # detect collision
    if x >= x_border - radius or x <= -x_border + radius:
        hvel = -1*hvel
    if y >= y_border - radius or y <= -y_border + radius:
        vvel = -1*vvel
        
    glutSwapBuffers()
    
def reshape(w, h):
    global x_border, y_border, x, y, radius
    # ensure we don't have a zero height
    if h == 0:
        h = 1
    # fill the entire graphics window
    glViewport(0, 0, w, h)
    # set the projection matrix to our view
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # set the aspect ratio to plot
    # so that it always looks good and never distorted
    if w <= h:
        gluOrtho2D(-axrng, axrng, -axrng * h / w, axrng * h / w)
        y_border = axrng * h / w
        x_border = axrng
    else:
        gluOrtho2D(-axrng * w / h, axrng * w / h, -axrng, axrng)
        x_border = axrng * w / h
        y_border = axrng
    
    if x <= -x_border:
        x = -x_border + 2 * radius
    if x >= x_border:
        x = x_border - (2*radius)
    if y <= -y_border:
        y = -y_border + (2*radius)
    if y >= y_border:
        y = y_border - (2*radius)
    
    # set matrix mode for object we are drawing
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
def keyboard(key, x, y):
    global anim
    if key == chr(27):
        sys.exit()
    if key == 'a':
        anim = 1
    if key == 's':
        anim = 0
    if key ==  'q':
        sys.exit()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
    glutInitWindowPosition(100,100)
    glutInitWindowSize(width,height)
    glutCreateWindow("PyBounce")
    glutDisplayFunc(plotfunc)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)
    init()
    glutMainLoop()

main()

# end of program
    