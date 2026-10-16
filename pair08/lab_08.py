# 1
#
# try:
#     num1 = float(input("Введіть перше число: "))
#     num2 = float(input("Введіть друге число: "))
#     operation = input("Введіть операцію (+, -, *, /): ").strip()
#
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         if num2 == 0:
#             print("Помилка: ділення на нуль неможливе.")
#         else:
#             result = num1 / num2
#     else:
#         print("Помилка: невідома операція. Дозволені тільки +, -, *, /.")
#         result = None
#
#     if result:
#         print(f"Результат: {result}")
#
# except ValueError:
#     print("Помилка: введено нечислове значення.")


#2

# def input_grade():
#     while True:
#         try:
#             user_input = input("Введіть оцінку (1 -> 12): ").strip()
#             grade = int(user_input)
#
#             if not (1 <= grade <= 12):
#                 raise ValueError("Число поза діапазоном 1-12.")
#
#             return grade
#
#         except ValueError:
#             print("Помилка: потрібно ввести саме ціле число від 1 до 12.\n")
#
# valid_grade = input_grade()
# print(f"Оцінку успішно прийнято: {valid_grade}")

#3

# students = ["Комаров Іван", "Петров Олег", "Сидоров Максим", "Антонова Ірина"]
# grades = {
#     "Математика": 11,
#     "Фізика": 10,
#     "Інформатика": 12,
#     "Історія": 9,
#     "Хімія": 8
# }
#
# print("1 — Пошук учня за індексом")
# print("2 — Пошук оцінки за назвою предмета")
#
# choice = input("Оберіть тип пошуку (1 -> 2): ").strip()
#
# if choice == "1":
#     try:
#         index_input = input("Введіть індекс учня: ").strip()
#         index = int(index_input)
#         student_name = students[index]
#         print(f"Учень за індексом {index}: {student_name}")
#     except ValueError:
#         print(f"Помилка введення! Ви ввели '{index_input}', а потрібно ввести ціле число.")
#     except IndexError:
#         print(f"Помилка індексу! Індекс {index} виходить за межі списку. Дозволені значення: від 0 до {len(students) - 1}.")
#
# elif choice == "2":
#     try:
#         subject = input("Введіть назву предмета: ").strip()
#         grade = grades[subject]
#         print(f"Оцінка з предмета '{subject}': {grade}")
#     except KeyError:
#         print(f"Помилка ключа! Предмета з назвою '{subject}' немає у словнику.")
#
# else:
#     print(f"Помилка меню! Пункту '{choice}' не існує. Оберіть 1 або 2.")


#4

# try:
#     with open("students.txt", "r", encoding="utf-8") as infile:
#         lines = infile.readlines()
#
#     valid_records = []
#     skipped_count = 0
#
#     for line_num, line in enumerate(lines, start=1):
#         line = line.strip()
#         if not line:
#             skipped_count += 1
#             print(f"Рядок {line_num}: Пропущено порожній рядок.")
#             continue
#
#         if ";" not in line:
#             skipped_count += 1
#             print(f"Рядок {line_num}: Помилка структури. Відсутній роздільник ';'.")
#             continue
#
#         parts = line.split(";")
#         if len(parts) != 2:
#             skipped_count += 1
#             print(
#                 f"Рядок {line_num}: Помилка структури. Неправильна кількість полів (очікується 2, отримано {len(parts)}).")
#             continue
#
#         name, score_str = parts[0].strip(), parts[1].strip()
#
#         try:
#             score = int(score_str)
#             if not (0 <= score <= 100):
#                 raise ValueError(f"Бал {score} знаходиться поза діапазоном 0..100.")
#
#             valid_records.append((name, score))
#
#         except ValueError as e:
#             skipped_count += 1
#             if "invalid literal for int()" in str(e):
#                 print(f"Рядок {line_num}: Помилка значення. Бал '{score_str}' не є цілим числом.")
#             else:
#                 print(f"Рядок {line_num}: Помилка значення. {e}")
#
#     valid_records.sort(key=lambda x: x[1], reverse=True)
#
#     with open("report.txt", "w", encoding="utf-8") as outfile:
#         for name, score in valid_records:
#             outfile.write(f"{name};{score}\n")
#
#     print(f"Кількість правильних записів: {len(valid_records)}")
#     print(f"Кількість пропущених записів: {skipped_count}")
#
# except FileNotFoundError:
#     print("Помилка: Файл 'students.txt' не знайдено. Перевірте його наявність.")
