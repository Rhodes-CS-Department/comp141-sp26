from cs1.graphics import *
from math import sqrt

def draw_dotted_line(x1, y1, x2, y2):
    distance_x = x2 - x1
    distance_y = y2 - y1
    distance = sqrt(distance_x ** 2 + distance_y ** 2)
    
    gaps = int(distance // 10)
    x_step = int(distance_x // gaps)
    y_step = int(distance_y // gaps)
    current_x = x1
    current_y = y1
    for i in range(gaps + 1):
        draw_filled_circle(current_x, current_y, 2)
        current_x += x_step
        current_y += y_step

def main():
    fileName = input("Filename: ")
    file = open(fileName, 'r')
    
    for line in file:
        line = line.rstrip()
        command, first, second = line.split(sep=' ')
        x, y = int(first), int(second)
        
        if command == "canvas":
            open_canvas(x, y)
            set_line_thickness(2)

        elif command == "jumpto":
            current_x, current_y = x, y
            
        elif command == "lineto":
            draw_line(current_x, current_y, x, y)
            current_x, current_y = x, y
            
        elif command == "dlineto":
            draw_dotted_line(current_x, current_y, x, y)
            current_x, current_y = x, y
        
main()


