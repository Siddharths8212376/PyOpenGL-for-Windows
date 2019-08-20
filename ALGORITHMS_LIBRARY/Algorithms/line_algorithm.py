from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# DDA algorithm
# assumptions: drawn from left to right
# can plot any line with any slope
class line_algorithm:
    def __init__(self, P_init, P_final):
        self.P_init = P_init
        self.P_final = P_final
        
    def dda_line(self):
        x_init, y_init = self.P_init
        x_final, y_final = self.P_final

        dx = x_final - x_init
        dy = y_final - y_init

        # depending upon the absolute values of dx and dy 
        # choose the number of steps to put pixel as
        steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

        # calculate increment in x and y for each steps
        x_inc = dx / float(steps)
        y_inc = dy / float(steps)
        x, y = x_init, y_init

        # add pixel for each step
        for i in range(steps + 1):
            glVertex2f(x, y)
            x += x_inc
            y += y_inc


    # Bresenham's algorithm
    # assumptions : 
    #   xf > xi , yf > yi
    #   slope should be positive
    def bresenham_line(self):
        x_init, y_init = self.P_init
        x_final, y_final = self.P_final

        m_new = 2 * (y_final - y_init)
        slope_error_new = m_new - (x_final - x_init)
        
        y = y_init
        for x in range(x_init, x_final + 1):
            glVertex2f(x, y)
            # add slope error to the angle formed
            slope_error_new += m_new
            # if slope error has reached the limit
            # increment y to update the slope error
            if slope_error_new >= 0:
                y += 1
                slope_error_new -= 2 * (x_final - x_init)

    # Midpoint Line algorithm
    # assumptions :
    #  xf > xi , yf > yi
    #  slope of line should be positive             
    def midpoint_line(self):

        x_init, y_init = self.P_init
        x_final, y_final = self.P_final
        dy = y_final - y_init
        dx = x_final - x_init

        # decision parameter d
        d = dy - dx / 2
        x = x_init
        y = y_init
        glVertex(x, y)

        # iterate through x
        while x < x_final:
            x += 1
            # if East is chosen
            if d < 0:
                d += dy
            # if North East is chosen
            else:
                d += dy - dx
                y += 1
            glVertex(x, y)
