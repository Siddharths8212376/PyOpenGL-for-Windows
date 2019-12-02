def clip(subjectPolygon, clipPolygon):
   def inside(p):
      return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
 
   def computeIntersection():
      dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
      dp = [ s[0] - e[0], s[1] - e[1] ]
      n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
      n2 = s[0] * e[1] - s[1] * e[0] 
      n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
      return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
 
   outputList = subjectPolygon
   cp1 = clipPolygon[-1]
 
   for clipVertex in clipPolygon:
      cp2 = clipVertex
      inputList = outputList
      outputList = []
      s = inputList[-1]
 
      for subjectVertex in inputList:
         e = subjectVertex
         if inside(e):
            if not inside(s):
               outputList.append(computeIntersection())
            outputList.append(e)
         elif inside(s):
            outputList.append(computeIntersection())
         s = e
      cp1 = cp2
   return(outputList)

#Program to plot a point

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time
from Algorithms.line_algorithm import line_algorithm

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)


def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    targPts = [( 50,150), (200, 50), (350,150), (350,300), (250,300), (200,250), (150,350), (100,250), (100,200)] 
    clipPts = [(100,100), (300,100), (300,300), (100,300)]
    # printing target polygon
    glColor3f(0, 1, 0)
    for index, each_coord in enumerate(targPts[:-1]):
       line = line_algorithm(each_coord, targPts[index + 1])
       line.dda_line()
    line = line_algorithm(targPts[-1], targPts[0])
    line.dda_line()
    # printing clipper
    glColor3f(1, 0, 0)
    for index, each_coord in enumerate(clipPts[:-1]):
       line = line_algorithm(each_coord, clipPts[index + 1])
       line.dda_line()
    line = line_algorithm(clipPts[-1], clipPts[0])
    line.dda_line()
    
    
    # doing the clip
    glColor3f(0, 0, 1)
    output_clip = clip(targPts, clipPts)
    for index, coord in enumerate(output_clip[:-1]):
       line = line_algorithm(coord, output_clip[index + 1])
       line.dda_line()
    line = line_algorithm(output_clip[-1], output_clip[0])
    line.dda_line()


    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'plot_all_points')
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()


main()

