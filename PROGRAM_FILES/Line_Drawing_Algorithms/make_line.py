
from line_plotting import get_line
global lis_lines
lis_lines = []
def draw_line(x_i, y_i, x_f, y_f):
    P_init = [x_i, y_i]
    P_final = [x_f, y_f]
    lis_lines.append([P_init, P_final])


# A = [
#         [10, -50],
#         [30, -100],
#         [50, 50],
#         [70, -200],
#     ]
# get_line(A, B)
# gets lines ab, bc
def show_line():
    # for each_line in lis_lines:
    get_line(lis_lines)

# it should be much more like an import of an import, adding various layers of abstraction
