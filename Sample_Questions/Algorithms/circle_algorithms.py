from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
class circle_algorithms:
    
    def __init__(self, radius, x_centre, y_centre):
        self.radius = radius
        self.x_centre = x_centre
        self.y_centre = y_centre
    
    def bresenham_circle(self):
        # self.radius = radius
        # self.x_centre = x_centre
        # self.y_centre = y_centre
        x, y = 0, self.radius
        d = 3 - 2 * self.radius
        for x_val in [-x, x]:
            for y_val in [-y, y]:
                glVertex2f(self.x_centre + x_val, self.y_centre + y_val)
                glVertex2f(self.x_centre + y_val, self.y_centre + x_val)

        while y >= x:
            # for each pixel we'll draw eight pixel
            x += 1

            if d > 0:
                y -= 1
                d += 4 * (x - y) + 10
            else:
                d += 4 * x + 6
            for x_val in [-x, x]:
                for y_val in [-y, y]:
                    glVertex2f(self.x_centre + x_val, self.y_centre + y_val)
                    glVertex2f(self.x_centre + y_val, self.y_centre + x_val)
    
    def midpoint_circle(self):
        # self.radius = radius
        # self.x_centre = x_centre
        # self.y_centre = y_centre
        x, y = self.radius, 0
        error = 0
        while x >= y:
            for x_val in [-x, x]:
                for y_val in [-y, y]:
                    glVertex2f(self.x_centre + x_val, self.y_centre + y_val)
                    glVertex2f(self.x_centre + y_val, self.y_centre + x_val)
            if error <= 0:
                y += 1
                error += 2 * y + 1
            if error > 0:
                x -= 1
                error -= 2 * x + 1
                
    def parameteric_circle(self):
        # self.radius = radius
        # self.x_centre = x_centre
        # self.y_centre = y_centre
        segments = 500
    
        for rad in range(segments):
            theta = 2 * 3.14159 * rad / segments
            x = self.radius * math.cos(theta)
            y = self.radius * math.sin(theta)
            glVertex2f(x + self.x_centre, y + self.y_centre)