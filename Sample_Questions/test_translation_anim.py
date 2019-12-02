# pybounce.py

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

# globals for animation, ball position
global anim, x, y, dx, dy

# initial position of the ball
x = -0.67
y = 0.34

# direction sign of the ball's motion
dx = dy = 1

# window dimensions
width = height = 500
ax_range = 1.0

# no animation to begin with
is_anim = 0

# init function
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    # sets unsigned bytes
    glColor3ub(255, 0, 0)
    
    # dimensions of the screen
    gluOrtho2D(-ax_range, ax_range, -ax_range, ax_range)

# define the idle function
def idle():
    # animate only if is_anim is set
    if is_anim == 1:
        glutPostRedisplay()
        
# define the bounce algorithm
def bounce():
    # refer to the globals
    global x, y, dx, dy
    # clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT)
    
    # changes in x and y
    x += 0.001 * dx
    y += 0.001 * x * x * dy
    
    # keep the motion mathematics
    # safe from harm
    # so that's why we need to use Push and Pop Matrix
    glPushMatrix()
    glTranslate(x, y, 0)
    glutSolidSphere(0.1, 50, 50)
    # glutSolidCube(0.1)
    glPopMatrix()
    
    # detection of collision
    if x >= ax_range or x <= -ax_range:
        dx = -1 * dx
    if y >= ax_range or y <= -ax_range:
        dy = -1 * dy
    # glFlush()
    glutSwapBuffers()
    
# keyboard function
def keyboard(key, x, y):
    # allow quit by using 'esc' or 'q'
    # we can animate by using 'a' or stop by using 's'
    # refer to the global anim object
    global is_anim
    
    if key == chr(27):
        sys.exit()
    if key == 'a':
        # enable animation
        is_anim = 1
    if key == 's':
        # stop the animation
        is_anim = 0
    if key == 'q':
        sys.exit()

# main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(width, height)
    glutCreateWindow(b'animate_ball')
    glutDisplayFunc(bounce)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)
    
    init()
    glutMainLoop()

main()

# end of program
    
    