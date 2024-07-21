from shape_area import calculate_area, is_right_triangle

# Вычисление площади круга с радиусом 5
area_circle = calculate_area('circle', 5)
print(f"Area of the circle: {area_circle}")

# Вычисление площади треугольника со сторонами 3, 4, 5
area_triangle = calculate_area('triangle', 3, 4, 5)
print(f"Area of the triangle: {area_triangle}")

# Проверка, является ли треугольник со сторонами 3, 4, 5 прямоугольным
right_triangle = is_right_triangle(3, 4, 5)
print(f"Is the triangle right-angled? {right_triangle}")