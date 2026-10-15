#import os

#1

# filename = "text.txt"
# with open(filename, 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#
#
# total_lines = len(lines)
# total_words = 0
# total_chars = 0
#
# longest_line_text = ""
# longest_line_len = -1
# longest_line_num = -1
#
# for index, line in enumerate(lines, start=1):
#     clean_line = line.rstrip('\r\n')
#
#     total_chars += len(clean_line)
#     total_words += len(clean_line.split())
#
#     if len(clean_line) > longest_line_len:
#         longest_line_len = len(clean_line)
#         longest_line_text = clean_line
#         longest_line_num = index
#
# print(f"Кількість рядків: {total_lines}")
# print(f"Кількість слів: {total_words}")
# print(f"Кількість символів: {total_chars}")
# print(f"Номер найдовшого рядка: {longest_line_num}")
# print(f"Довжина найдовшого рядка: {longest_line_len}")
# print(f"Текст найдовшого рядка: {longest_line_text}")


#2

#
# filename = "text.txt"
#
# if not os.path.exists(filename):
#     print(f"Помилка: Файл {filename} не знайдено.")
# else:
#     search_query = input("Введіть фрагмент тексту для пошуку: ").lower()
#
#     with open(filename, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#
#     found = False
#     index = 1
#
#     for line in lines:
#         clean_line = line.rstrip('\r\n')
#         if search_query in clean_line.lower():
#             print(f"Рядок {index}: {clean_line}")
#             found = True
#         index += 1
#
#     if not found:
#         print("Збігів не знайдено.")


#3

# input_filename = "students.txt"
# output_filename = "result.txt"
#
# if not os.path.exists(input_filename):
#     print(f"Помилка: Файл {input_filename} не знайдено.")
# else:
#     with open(input_filename, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#
#     good_students = []
#
#     for line in lines:
#         clean_line = line.rstrip('\r\n')
#         if not clean_line:
#             continue
#
#         parts = clean_line.split(';')
#         if len(parts) == 2:
#             name, score_str = parts
#             score = float(score_str)
#             if score > 80:
#                 good_students.append((name, score))
#
#     good_students.sort(key=lambda student: student[1], reverse=True)
#
#     with open(output_filename, 'w', encoding='utf-8') as file:
#         for name, score in good_students:
#             if score.is_integer():
#                 file.write(f"{name};{int(score)}\n")
#             else:
#                 file.write(f"{name};{score}\n")


#4

# def read_grades(filename="grades.csv"):
#     students_data = {}
#
#     if not os.path.exists(filename):
#         print(f"Помилка: Файл {filename} не знайдено.")
#         return None
#
#     with open(filename, 'r', encoding='utf-8') as file:
#         header = file.readline()
#
#         for line in file:
#             clean_line = line.rstrip('\r\n')
#             if not clean_line:
#                 continue
#
#             parts = clean_line.split(';')
#             if len(parts) == 3:
#                 name, subject, grade_str = parts
#                 grade = float(grade_str)
#
#                 if name not in students_data:
#                     students_data[name] = []
#                 students_data[name].append(grade)
#
#     return students_data
#
#
# def analyze_students(students_data):
#     report_list = []
#
#     for name, grades in students_data.items():
#         count = len(grades)
#         avg_grade = sum(grades) / count
#         report_list.append((name, count, avg_grade))
#
#     report_list.sort(key=lambda x: x[2], reverse=True)
#     return report_list
#
#
# def write_report(report_list, output_filename="report.txt"):
#     if not report_list:
#         return
#
#     best_student = report_list[0]
#
#     with open(output_filename, 'w', encoding='utf-8') as file:
#         for name, count, avg in report_list:
#             file.write(f"Учень: {name}, Кількість оцінок: {count}, Середній бал: {avg:.2f}\n")
#
#         file.write(f"\nНайкращий учень: {best_student[0]} із середнім балом {best_student[2]:.2f}\n")
#
#
# data = read_grades()
# if data:
#     analysis = analyze_students(data)
#     write_report(analysis)
