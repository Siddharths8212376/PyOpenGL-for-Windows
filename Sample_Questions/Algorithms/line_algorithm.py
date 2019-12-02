from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
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
        steps = int(abs(dx) if abs(dx) > abs(dy) else abs(dy))

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

    def test_bres_line(self):
        x_init, y_init = self.P_init
        x_final, y_final = self.P_final
        
        dx = abs(x_final - x_init)
        dy = abs(y_final - y_init)
        P = 2 * dy - dx
        
        if x_init > x_final:
            x = x_final
            y = y_final
            x_end = x_init
        else:
            x = x_init
            y = y_init
            x_end = x_final
        glVertex2f(x, y)
        
        while x < x_end:
            x += 1
            if P < 0:
                P = P + 2 * dy
            else:
                y += 1
                P = P + 2 * (dy - dx)
            glVertex2f(x, y)
        
        
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

    def return_length(self):
        x_init, y_init = self.P_init
        x_final, y_final = self.P_final
        return math.sqrt((y_final - y_init) ** 2 + (x_final - x_init) ** 2)
    
    def return_midpoint(self):
        x_init, y_init = self.P_init
        x_final, y_final = self.P_final
        return [(x_init + x_final) / 2, (y_init + y_final) / 2]
        
    def return_slope(self):
        x_init, y_init = self.P_init
        x_final, y_final = self.P_final
        if y_final - y_init == 0:
            return 0
        elif x_final - x_init == 0:
            return 10000
        else:
            return(y_final - y_init) / (x_final - x_init)