x, y = map(float, input("Введіть координати точки (x y) через пробіл: ").split())

if x > 0 and y > 0:
    print("1 чверть")
elif x < 0 and y > 0:
    print("2 чверть")
elif x < 0 and y < 0:
    print("3 чверть")
elif x > 0 and y < 0:
    print("4 чверть")
elif x == 0 and y == 0:
    print("Точка знаходиться на початку координат")
else:
    print("Точка лежить на одній з осей координат")
