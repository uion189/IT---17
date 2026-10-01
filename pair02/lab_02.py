#1

# n = int(input("Число: "))
#
# suma = 0
# count = 0
#
# for i in range(1, n + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         count += 1
#         suma += i
#
# print("Кількість", count)
# print("Сума", suma)
# print("Середнє", suma / count)
#

#2

# n = int(input("Число: "))
#
# if n == 0:
#     count = 1
#     suma = 0
#     max_digit = 0
#     min_digit = 0
# else:
#     count = 1
#     max_digit = n % 10
#     min_digit = n % 10
#     suma = n % 10
#
#     while n > 9:
#         n = n // 10
#         count += 1
#         if n % 10 > max_digit:
#             max_digit = n % 10
#         if n % 10 < min_digit:
#             min_digit = n % 10
#         suma += n % 10
#
# print("Кількість чисел", count)
# print("Максимальне число", max_digit)
# print("Мінімальне число", min_digit)
# print("Сума чисел", suma)
#

#3

# n = int(input())
#
# result = []
#
# for i in range(1, n):
#     temp = i
#     is_valid = True
#
#     while temp > 0:
#         digit = temp % 10
#
#         if digit != 0 and i % digit != 0:
#             is_valid = False
#             break
#
#         temp //= 10
#
#     if is_valid:
#         result.append(i)
#
# for i in result:
#     print(i, end=" ")
#


#4

# width = int(input("Ширина прямокутника (мінімум 3): "))
# height = int(input("Висота прямокутника (мінімум 3): "))
# border = input("Символ контуру: ")
# fill = input("Символ внутрішньої частини: ")
#
# if width < 3 or height < 3:
#     print("Розміри більше за 3")
# else:
#     for i in range(height):
#         for j in range(width):
#             if i == 0 or i == height - 1 or j == 0 or j == width - 1:
#                 print(border, end="")
#             else:
#                 print(fill, end="")
#
#         print()
