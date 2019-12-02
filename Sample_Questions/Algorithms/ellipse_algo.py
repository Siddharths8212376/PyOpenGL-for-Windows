from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# DDA algorithm
# assumptions: drawn from left to right
# can plot any line with any slope
class ellipse_algo:
    def __init__(self, x_centre, y_centre, radius_x, radius_y):
        self.x_centre = x_centre
        self.y_centre = y_centre
        self.radius_x = radius_x
        self.radius_y = radius_y
        
    def midpoint_ellipse(self):
        x, y = 0, self.radius_y
    
        # initialize decision parameter of the first quadrant // region 1
        # d1 = ry ** 2 - rx ** 3 + 0.25 * rx ** 2
        # dx = 2 * ry ** 2 * x
        # dy = 2 * rx ** 2 * y
        
        decision_param_1 = self.radius_y ** 2 - self.radius_x ** 3 + 0.25 * (self.radius_x ** 2)
        dx = 2 * ( self.radius_y ** 2 ) * x
        dy = 2 * ( self.radius_x ** 2 ) * y
        
        # for the first region
        while dx < dy:
            # print all the points in the four quadrants
            for x_val in [-x, x]:
                for y_val in [-y, y]:
                    glVertex2f(y_val + self.y_centre, x_val + self.x_centre)
        
            # checking and updating the value of decision parameter
            # based on the algorithm
        
            if decision_param_1 < 0:
                x += 1
                dx = dx + 2 * (self.radius_y ** 2)
                dy = decision_param_1 + dx + self.radius_y ** 2
                
            else:
                x += 1
                y -= 1
                dx = dx + 2 * (self.radius_y ** 2)
                dy = decision_param_1 + dx - dy + self.radius_y ** 2
            
        # decision parameter of the second region
        decision_param_2 =  ((self.radius_y ** 2) * ((x + 0.5) ** 2)) + ((self.radius_x ** 2) * ((y - 1) ** 2)) - ((self.radius_x ** 2) * (self.radius_y ** 2))
        # plotting points of the second region
        while y >= 0:
            # print all the points in the four quadrants
            for x_val in [-x, x]:
                for y_val in [-y, y]:
                    glVertex2f(y_val + self.y_centre, x_val + self.x_centre)
                    
            # checking and updating the value of decision parameter
            if decision_param_2 > 0:
                y -= 1
                dy = dy - 2 * (self.radius_x ** 2)
                decision_param_2 += self.radius_x ** 2 - dy
                
            else:
                y -= 1
                x += 1
                dx = dx + 2 * (self.radius_y ** 2)
                dy = dy - 2 * (self.radius_x ** 2)
                decision_param_2 += dx - dy + self.radius_x ** 2
                
        