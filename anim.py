from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy
import math
import sys
# from dda_import import ddadisplay
from Algorithms.line_algorithm import line_algorithm
import time

x1=0
y1=0
def init():
	glClearColor(1.0,.0,1.0,0.0)
	glMatrixMode(GL_PROJECTION)
	gluOrtho2D(0,640,0,480)




def square(x,y):
    line = line_algorithm([x - 20, y - 20], [x + 20, y + 20])
    line.dda_line()
	# ddadisplay(x-20,y-20,x+20,y+20)


def mouse(btn,state,x,y):
	y = 480-y
	if(btn==GLUT_LEFT_BUTTON):
		if(state==GLUT_DOWN):
			world(x,y)
		
             # square(x,y)


def world(x,y):
	glLineWidth(3)
	glPointSize(7.0)
	#glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glBegin(GL_LINES)
	glVertex2i(600,300)
	glVertex2i(50,300)
	glEnd()
	glFlush()
   	glBegin(GL_LINE_LOOP)
	glVertex2i(x-5,y-5)
	glVertex2i(x+5,y-5)
	glVertex2i(x+5,y+5)
	glVertex2i(x-5,y+5)
	glVertex2i(x-5,y-5)
	#glVertex2i(300,300)
	#glVertex2i(450,100)
	glEnd()
	glFlush()
	while (y>300):
		translate(x,y)
		y-=10
		time.sleep(0.5)

	translate(x,305)
	global x1,y1
	x1=x
	y1=y+10
		
def translate(x,y):
    glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_LINES)
	glVertex2i(600,300)
	glVertex2i(50,300)
	glEnd()
	glFlush()
	glBegin(GL_QUADS)
	glVertex2i(x-5,y-5)
	glVertex2i(x+5,y-5)
	glVertex2i(x+5,y+5)
	glVertex2i(x-5,y+5)
	glVertex2i(x-5,y-5)
	glEnd()
	glFlush()

def translate_horizontal(x,y,val):
	if val=="left":
		global x1,y1
		glClear(GL_COLOR_BUFFER_BIT)
		glBegin(GL_LINES)
		glVertex2i(600,300)
		glVertex2i(50,300)
		glEnd()
		glFlush()
		glBegin(GL_QUADS)
		glVertex2i(x1-5,y1-5)
		glVertex2i(x1+5,y1-5)
		glVertex2i(x1+5,y1+5)
		glVertex2i(x1-5,y1+5)
		glVertex2i(x1-5,y1-5)
		glEnd()
		glFlush()
	if val=="right":
		global x1,y1
		glClear(GL_COLOR_BUFFER_BIT)
		glBegin(GL_LINES)
		glVertex2i(600,300)
		glVertex2i(50,300)
		glEnd()
		glFlush()
		glBegin(GL_QUADS)
		glVertex2i(x1-5,y1-5)
		glVertex2i(x1+5,y1-5)
		glVertex2i(x1+5,y1+5)
		glVertex2i(x1-5,y1+5)
		glVertex2i(x1-5,y1-5)
		glEnd()
		glFlush()

def key_pressed(key,x,y):
	global x1,y1
	if (key == GLUT_KEY_LEFT):
		x1-=5
		translate_horizontal(x1,y1,"left")
	elif (key == GLUT_KEY_RIGHT):
		x1+=5
		translate_horizontal(x1,y1,"right")
	


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(640,480)
	glutInitWindowPosition(200,200)
	glutCreateWindow("Animation")
	#glutDisplayFunc(world)
	glutMouseFunc(mouse)
	glutSpecialFunc(key_pressed)
	#glutSpecialFunc(special)
	init()
	glutMainLoop()
   
main()
	
		
	
