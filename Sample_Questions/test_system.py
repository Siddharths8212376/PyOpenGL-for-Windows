# pybounce.py
# a - animate s - stop
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
from Algorithms.line_algorithm import line_algorithm
# globals for animation, ball position
global anim, x, y, dx, dy

# initial position of the ball
x = -0.67
y = 0.34

# direction sign of the ball's motion
dx = 2
dy = 1

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
        
def draw_figure():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(0.2, 0.2)
    
    glVertex2f(0.2, 0.2)
    glVertex2f(0.5, 0)
    
    glVertex2f(0, 0)
    glVertex2f(0.5, 0)
    
    # a.dda_line()
    # b.dda_line()
    # c.dda_line()
    glEnd()
    glFlush()
# define the bounce algorithm
def bounce():
    # refer to the globals
    global x, y, dx, dy
    # clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT)
    
    # changes in x and y
    x += 0.00001 * dx
    y += (-0.0001 * dx * dx  ) * dy
    
    # keep the motion mathematics
    # safe from harm
    # so that's why we need to use Push and Pop Matrix
    glPushMatrix()
    glTranslate(x, y, 0)
    glutSolidSphere(0.1, 10, 10)
    # glColor3f(0, 0, 1)
    # glTranslate(x + 10, y, 0)
    # glutSolidSphere(0.1, 12, 12)
    # draw_figure()
    # glutSolidCube(0.1)
    glPopMatrix()
    
    glPushMatrix()
    # glTranslate(x, y, 0)
    # glutSolidSphere(0.1, 10, 10)
    glColor3f(0, 0, 1)
    glTranslate(x + 0.3, y - 0.2, 0)
    glutSolidSphere(0.1, 12, 12)
    # draw_figure()
    # glutSolidCube(0.1)
    glPopMatrix()
    
    
    # detection of collision
    if x >= ax_range or x <= -ax_range:
        dx = -1 * dx
    if y >= ax_range:
        dy = -1 * dy
    if y <= -ax_range:
        y = ax_range
        
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
    
    