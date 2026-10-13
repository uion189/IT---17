#1
#
#
#import math
#
# radius = int(input("Радіус: "))
# cathetus1 = int(input("Катет: "))
# cathetus2 = int(input("Катет: "))
# total_items = int(input("Предметів: "))
# items_per_pack = int(input("В упаковці: "))
#
# circle_area = math.pi * (radius ** 2)
# hypotenuse = math.sqrt(cathetus1 ** 2 + cathetus2 ** 2)
# packs_needed = math.ceil(total_items / items_per_pack)
#
# print(f"Площа круга: {round(circle_area, 2)}")
# print(f"Гіпотенуза: {round(hypotenuse, 2)}")
# print(f"Потрібно упаковок: {packs_needed}")

#2

# import random
# import statistics
#
# n = int(input("Введіть кількість оцінок: "))
#
# if n <= 0:
#     print("Помилка: N повинно бути додатним числом!")
# else:
#     grades = [random.randint(1, 12) for _ in range(n)]
#
#     min_grade = min(grades)
#     max_grade = max(grades)
#     mean_val = statistics.mean(grades)
#     median_val = statistics.median(grades)
#     high_grades_count = 0
#     for i in grades:
#         if 10 <= i <= 12:
#             high_grades_count += 1
#
#     print(f"Список оцінок: {grades}")
#     print(f"Мінімальна оцінка: {min_grade}")
#     print(f"Максимальна оцінка: {max_grade}")
#     print(f"Середнє арифметичне: {round(mean_val, 2)}")
#     print(f"Медіана: {median_val}")
#     print(f"Кількість оцінок 10–12: {high_grades_count}")

#3

# import datetime
#
# year = int(input("Введіть рік: "))
# month = int(input("Введіть місяць: "))
# day = int(input("Введіть день: "))
#
# event_date = datetime.date(year, month, day)
# today = datetime.date.today()
#
# if event_date > today:
#     delta = event_date - today
#     print(f"До події залишилося: {delta.days} днів")
# elif event_date < today:
#     delta = today - event_date
#     print(f"Після події минуло: {delta.days} днів")
# else:
#     print("Подія відбувається сьогодні!")