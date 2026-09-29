num = int(input("Введіть ціле число: "))
if num % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")

age = int(input("Введіть свій вік: "))
if age >= 18:
    print("Ви повнолітні!")
else:
    print("Ви неповнолітній!")

import math

r = float(input("Введіть радіус кола: "))
a = math.pi * (r ** 2)
l = 2 * math.pi * r
print(f"Площа кола:", a)
print(f"Довжина кола: ", l)

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
if a > b:
    print(f"Більше число: {a}")
elif b > a:
    print(f"Більше число: {b}")
else:
    print("Числа рівні")
