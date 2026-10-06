# 1
# numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
#
# positives = []
# negatives = []
# evens = []
# multiples_three = []
#
# for num in numbers:
#     if num > 0:
#         positives.append(num)
#     if num < 0:
#         negatives.append(num)
#     if num % 2 == 0:
#         evens.append(num)
#     if num % 3 == 0:
#         multiples_three.append(num)
#
# min_val = min(numbers)
# max_val = max(numbers)
# total_sum = sum(numbers)
# average = total_sum / len(numbers)
#
# print(f"Додатні: {positives}")
# print(f"Від’ємні: {negatives}")
# print(f"Парні: {evens}")
# print(f"Кратні 3: {multiples_three}")
# print(f"Min: {min_val}; Max: {max_val}; Sum: {total_sum}; Average: {average}")



# 2
# group1 = {"Anna", "Ivan", "Olha"}
# group2 = {"Ivan", "Maksym", "Olha"}
#
# shared = group1 & group2
# only_group1 = group1 - group2
# only_group2 = group2 - group1
# all = group1 | group2
#
# print(f"Спільні: {', '.join(sorted(shared))}")
# print(f"Тільки group1: {', '.join(sorted(only_group1))}")
# print(f"Тільки group2: {', '.join(sorted(only_group2))}")
# print(f"Усі: {', '.join(sorted(all))}")



# 3
# products = {
#     "milk": 48,
#     "bread": 25,
#     "tea": 75,
#     "coffee": 120,
#     "apple": 35,
#     "cheese": 95
# }
# new_name = input("Новий товар: ")
# new_price = int(input("Його ціна: "))
# products[new_name] = new_price
#
# search_name = input("Що шукаєте? ")
# found_price = products.get(search_name)
#
# if found_price is not None:
#     print(f"Результат пошуку: {search_name} — {found_price} грн")
# else:
#     print(f"Товар '{search_name}' не знайдено")
#
# min_price = int(input("Ведіть початок діапазону: "))
# max_price = int(input("Його кінець: "))
#
# print(f"\nТовари в діапазоні {min_price}..{max_price} грн:")
# for name, price in products.items():
#     if min_price <= price <= max_price:
#         print(f"{name} — {price} грн")





# 4
# group_info = ('10-IT', '2026/2027')
#
# journal = {}
#
# name = "Anna"
# grades = [10, 11, 12, 9, 10]
# if len(grades) == 5 and all(1 <= g <= 12 for g in grades):
#     journal[name] = grades
# else:
#     print(f"Помилка: {name} повинен мати рівно 5 оцінок у діапазоні 1–12.")
#
# name = "Ivan"
# grades = [8, 9, 10, 11, 9]
# if len(grades) == 5 and all(1 <= g <= 12 for g in grades):
#     journal[name] = grades
# else:
#     print(f"Помилка: {name} повинен мати рівно 5 оцінок у діапазоні 1–12.")
#
# name = "Olha"
# grades = [11, 12, 12, 10, 11]
# if len(grades) == 5 and all(1 <= g <= 12 for g in grades):
#     journal[name] = grades
# else:
#     print(f"Помилка: {name} повинен мати рівно 5 оцінок у діапазоні 1–12.")
#
# print(f"\nЖурнал групи {group_info[0]} — {group_info[1]}")
# for name, grades in journal.items():
#     print(f"{name}: {grades}")
#
# print("\nСередній бал кожного учня:")
# for name, grades in journal.items():
#     average = sum(grades) / len(grades)
#     print(f"{name}: {round(average, 2)}")
#
# rating_list = []
# for name, grades in journal.items():
#     average = sum(grades) / len(grades)
#     rating_list.append([name, average])
#
# n = len(rating_list)
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if rating_list[j][1] < rating_list[j + 1][1]:
#             rating_list[j], rating_list[j + 1] = rating_list[j + 1], rating_list[j]
#
# print("\nРейтинг учнів за середнім балом:")
# place = 1
# for name, average in rating_list:
#     print(f"{place}. {name} — {round(average, 2)}")
#     place += 1
#
# best_name = ""
# best_average = 0
# for name, grades in journal.items():
#     average = sum(grades) / len(grades)
#     if average > best_average:
#         best_average = average
#         best_name = name
# print(f"\nНайкращий учень: {best_name} — {round(best_average, 2)}")
