# 1
# def calculate_circle_area(radius):
#     pi = 3.14159
#     return pi * (radius ** 2)
#
#
# def calculate_rectangle_area(width, height):
#     return width * height
#
#
# def calculate_triangle_area(base, height):
#     return 0.5 * base * height
#
#
# def main():
#     print('1 = круг')
#     print('2 = прямокутник')
#     print('3 = трикутник')
#     choice = input("Оберіть фігуру: ").strip()
#
#     if choice == '1' or choice.lower() == 'круг':
#         radius = float(input("Радіус: "))
#         area = calculate_circle_area(radius)
#         print(f"Площа круга: {area}")
#
#     elif choice == '2' or choice.lower() == 'прямокутник':
#         width = float(input("Ширина: "))
#         height = float(input("Довжина: "))
#         area = calculate_rectangle_area(width, height)
#         print(f"Площа прямокутника: {int(area) if area.is_integer() else area}")
#
#     elif choice == '3' or choice.lower() == 'трикутник':
#         base = float(input("Сторона "))
#         height = float(input("Висота :"))
#         area = calculate_triangle_area(base, height)
#         print(f"Площа трикутника: {area}")
#
#
# if __name__ == "__main__":
#     main()



#2
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def divisors(n):
#     result = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             result.append(i)
#             if i != n // i:
#                 result.append(n // i)
#     return sorted(result)
#
#
# def digit_sum(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total
#
#
# def main():
#     n = int(input("N = "))
#
#     prime_status = "так" if is_prime(n) else "ні"
#     divs = divisors(n)
#     d_sum = digit_sum(n)
#
#     print(f"Просте число: {prime_status}")
#     print(f"Дільники: {divs}")
#     print(f"Сума цифр: {d_sum}")
#
#
# if __name__ == "__main__":
#     main()



#3
# def average(grades):
#     return sum(grades) / len(grades)
#
#
# def minimum(grades):
#     return min(grades)
#
#
# def maximum(grades):
#     return max(grades)
#
#
# def count_above(grades, value):
#     count = 0
#     for grade in grades:
#         if grade > value:
#             count += 1
#     return count
#
#
# def main():
#     grades = list(map(int, input("Оцінки: ").split()))
#     grade = int(input("Вище за?: "))
#
#     avg_grade = average(grades)
#     min_grade = minimum(grades)
#     max_grade = maximum(grades)
#     above_grade = count_above(grades, grade)
#
#     print(f"Середній бал: {avg_grade:.1f}")
#     print(f"Мінімальна: {min_grade}")
#     print(f"Максимальна: {max_grade}")
#     print(f"Вище {grade}: {above_grade}")
#
#
# if __name__ == "__main__":
#     main()



#4
# def check_length(password):
#     return len(password) >= 8
#
#
# def check_digit(password):
#     for char in password:
#         if char.isdigit():
#             return True
#     return False
#
#
# def check_upper(password):
#     for char in password:
#         if char.isupper():
#             return True
#     return False
#
#
# def check_lower(password):
#     for char in password:
#         if char.islower():
#             return True
#     return False
#
#
# def check_special(password):
#     for char in password:
#         if not char.isalnum():
#             return True
#     return False
#
#
# def validate_password(password):
#     errors = []
#
#     if not check_length(password):
#         errors.append("довжина менше 8 символів")
#     if not check_digit(password):
#         errors.append("немає хоча б однієї цифри")
#     if not check_upper(password):
#         errors.append("немає великої літери")
#     if not check_lower(password):
#         errors.append("немає малої літери")
#     if not check_special(password):
#         errors.append("немає спеціального символу")
#
#     is_valid = len(errors) == 0
#     return is_valid, errors
#
#
# def main():
#     password = input("Password: ")
#
#     is_valid, errors = validate_password(password)
#
#     if is_valid:
#         print("Пароль надійний")
#     else:
#         print("Пароль не відповідає вимогам.")
#         print(f"Не виконано: {', '.join(errors)}")
#
#
# if __name__ == "__main__":
#     main()

