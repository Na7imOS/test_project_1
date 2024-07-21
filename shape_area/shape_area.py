from shapes.circle import Circle
from shapes.triangle import Triangle

def calculate_area(shape, *args):
    if shape == 'circle':
        return Circle(*args).area()
    elif shape == 'triangle':
        return Triangle(*args).area()
    else:
        raise ValueError(f"Unknown shape: {shape}")

def is_right_triangle(a, b, c):
    return Triangle(a, b, c).is_right_triangle()
    