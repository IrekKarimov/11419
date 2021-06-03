# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int( input("Введите координаты первой точки x1 = ") )
y1 = int( input("Введите координаты первой точки y1 = ") )
x2 = int( input("Введите координаты второй точки x2 = ") )
y2 = int( input("Введите координаты второй точки y2 = ") )

# Вычисляем k, b
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

print(f'k = {k}, b = {b}')
print(f'Формула прямой: y = {k}x + {b}')
