#1
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         return f"Ім'я: {self.name}"
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#
#     def info(self):
#         return f"Студент: {self.name}, Група: {self.group}"
#
# student1 = Student("Іваненко Іван Іванович", "КН-21")
# student2 = Student("Петренко Ольга Петрівна", "ІПЗ-12")
#
# print(student1.info())
# print(student2.info())

#2
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         return f"Ім'я: {self.name}"
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#
#     def info(self):
#         return f"Студент: {self.name}, Група: {self.group}"
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     def info(self):
#         return f"Викладач: {self.name}, Предмет: {self.subject}"
#
# person1 = Person("Коваленко Андрій")
# student1 = Student("Іваненко Іван Іванович", "КН-21")
# teacher1 = Teacher("Сидоренко Олег Петрович", "Програмування")
#
# people = [person1, student1, teacher1]
#
# for person in people:
#     print(person.info())


#3
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         return f"Ім'я: {self.name}"
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#
#     def info(self):
#         return f"Студент: {self.name}, Група: {self.group}"
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     def info(self):
#         return f"Викладач: {self.name}, Предмет: {self.subject}"
#
# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []
#
#     def add_student(self, student):
#         for s in self.students:
#             if s.name == student.name:
#                 print(f"Помилка: Студент {student.name} вже записаний на курс!")
#                 return
#         self.students.append(student)
#
#     def remove_student(self, name):
#         for s in self.students:
#             if s.name == name:
#                 self.students.remove(s)
#                 return
#         print(f"Помилка: Студента з ПІБ {name} не знайдено на курсі.")
#
#     def show_students(self):
#         print(f"\nАктуальний список курсу '{self.title}' (Викладач: {self.teacher.name}):")
#         if not self.students:
#             print("На курсі немає студентів.")
#             return
#         for s in self.students:
#             print(f"- {s.info()}")
#
#
# teacher = Teacher("Сидоренко Олег Петрович", "Програмування")
# course = Course("Основи Python", teacher)
#
# st1 = Student("Іваненко Іван Іванович", "КН-21")
# st2 = Student("Петренко Ольга Петрівна", "ІПЗ-12")
# st3 = Student("Коваленко Сергій Васильович", "КН-21")
# st4 = Student("Мельник Анна Андріївна", "ІПЗ-12")
#
# course.add_student(st1)
# course.add_student(st2)
# course.add_student(st3)
# course.add_student(st4)
#
# course.add_student(st1)
#
# course.show_students()
#
# print()
# course.remove_student("Петренко Ольга Петрівна")
#
# course.show_students()


#4
# import os
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         return f"Ім'я: {self.name}"
#
#
# class Student(Person):
#     def __init__(self, name, group, grades=None):
#         super().__init__(name)
#         self.group = group
#         self.grades = grades if grades is not None else []
#
#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)
#             return True
#         print("Помилка: Оцінка повинна бути в діапазоні від 1 до 12.")
#         return False
#
#     def average(self):
#         if not self.grades:
#             return 0.0
#         return round(sum(self.grades) / len(self.grades), 2)
#
#     def info(self):
#         return f"Студент: {self.name}, Група: {self.group}, Оцінки: {self.grades}, Середній бал: {self.average()}"
#
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     def info(self):
#         return f"Викладач: {self.name}, Предмет: {self.subject}"
#
#
# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []
#
#     def add_student(self, student):
#         for s in self.students:
#             if s.name == student.name:
#                 print(f"Помилка: Студент з ПІБ '{student.name}' вже записаний на курс!")
#                 return False
#         self.students.append(student)
#         return True
#
#     def remove_student(self, name):
#         for s in self.students:
#             if s.name == name:
#                 self.students.remove(s)
#                 print(f"Студента '{name}' успішно видалено з курсу.")
#                 return True
#         print(f"Помилка: Студента з ПІБ '{name}' не знайдено на курсі.")
#         return False
#
#     def find_student(self, name):
#         for s in self.students:
#             if s.name == name:
#                 return s
#         return None
#
#     def add_grade_to_student(self, name, grade):
#         student = self.find_student(name)
#         if student:
#             return student.add_grade(grade)
#         print(f"Помилка: Студента з ПІБ '{name}' не знайдено.")
#         return False
#
#     def show_students(self):
#         print(f"\n--- Список курсу '{self.title}' (Викладач: {self.teacher.name}) ---")
#         if not self.students:
#             print("На курсі немає студентів.")
#             return
#         for s in self.students:
#             print(f"- {s.info()}")
#
#     def show_rating(self):
#         print(f"\n--- Рейтинг студентів курсу '{self.title}' ---")
#         if not self.students:
#             print("На курсі немає студентів для формування рейтингу.")
#             return
#         sorted_students = sorted(self.students, key=lambda s: s.average(), reverse=True)
#         for i, s in enumerate(sorted_students, 1):
#             print(f"{i}. {s.name} ({s.group}) — Середній бал: {s.average()}")
#
#     def save_to_file(self, filename="course_data.txt"):
#         try:
#             with open(filename, "w", encoding="utf-8") as f:
#                 for s in self.students:
#                     grades_str = ",".join(map(str, s.grades))
#                     f.write(f"{s.name};{s.group};{grades_str}\n")
#             print(f"Дані успішно збережено у файл '{filename}'.")
#         except IOError as e:
#             print(f"Помилка при збереженні файлу: {e}")
#
#     def load_from_file(self, filename="course_data.txt"):
#         if not os.path.exists(filename):
#             print(f"Файл '{filename}' не знайдено. Початок роботи з порожнім списком.")
#             return
#         try:
#             with open(filename, "r", encoding="utf-8") as f:
#                 for line_num, line in enumerate(f, 1):
#                     line = line.strip()
#                     if not line:
#                         continue
#                     parts = line.split(";")
#                     if len(parts) != 3:
#                         print(f"Помилка в рядку {line_num}: Неправильний формат даних. Рядок пропущено.")
#                         continue
#                     name, group, grades_str = parts
#                     try:
#                         grades = [int(g) for g in grades_str.split(",")] if grades_str else []
#                         for g in grades:
#                             if not (1 <= g <= 12):
#                                 raise ValueError(f"Некоректна оцінка {g}")
#                     except ValueError as e:
#                         print(f"Помилка в рядку {line_num} (пошкоджені оцінки): {e}. Рядок пропущено.")
#                         continue
#
#                     student = Student(name, group, grades)
#                     self.students.append(student)
#             print(f"Дані успішно завантажено з файлу '{filename}'. Відновлено {len(self.students)} студентів.")
#         except IOError as e:
#             print(f"Помилка при читанні файлу: {e}")
#
#
# def main():
#     teacher = Teacher("Сидоренко Олег Петрович", "Програмування")
#     course = Course("Основи Python", teacher)
#
#     course.load_from_file()
#
#     while True:
#         print("\n\tМЕНЮ ПРОГРАМИ")
#         print("1 — Показати курс")
#         print("2 — Додати студента")
#         print("3 — Видалити студента")
#         print("4 — Знайти студента")
#         print("5 — Виставити оцінку")
#         print("6 — Показати рейтинг")
#         print("7 — Зберегти дані")
#         print("0 — Вихід")
#         print()
#
#         choice = input("Оберіть пункт меню: ").strip()
#
#         if choice == "1":
#             course.show_students()
#
#         elif choice == "2":
#             name = input("Введіть ПІБ студента: ").strip()
#             group = input("Введіть групу студента: ").strip()
#             if name and group:
#                 new_student = Student(name, group)
#                 if course.add_student(new_student):
#                     print(f"Студента '{name}' успішно додано.")
#             else:
#                 print("Помилка: ПІБ та група не можуть бути порожніми.")
#
#         elif choice == "3":
#             name = input("Введіть ПІБ студента для видалення: ").strip()
#             course.remove_student(name)
#
#         elif choice == "4":
#             name = input("Введіть ПІБ студента для пошуку: ").strip()
#             student = course.find_student(name)
#             if student:
#                 print(f"Знайдено: {student.info()}")
#             else:
#                 print(f"Студента з ПІБ '{name}' не знайдено.")
#
#         elif choice == "5":
#             name = input("Введіть ПІБ студента: ").strip()
#             try:
#                 grade = int(input("Введіть оцінку (1-12): ").strip())
#                 if course.add_grade_to_student(name, grade):
#                     print(f"Оцінку {grade} успішно виставлено студенту {name}.")
#             except ValueError:
#                 print("Помилка: Введене значення має бути цілим числом.")
#
#         elif choice == "6":
#             course.show_rating()
#
#         elif choice == "7":
#             course.save_to_file()
#
#         elif choice == "0":
#             print("Роботу завершено.")
#             break
#
#         else:
#             print("Помилка: Неправильний пункт меню.")
#
#
# if __name__ == "__main__":
#     main()

