#1

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def info(self):
#         print(f"Прямокутник: {self.width}x{self.height} | Площа: {self.area()} | Периметр: {self.perimeter()}")
#
#
# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3.5, 7.2)
#
# print("1 об'єкт:")
# print(f"Ширина: {rect1.width}, Висота: {rect1.height}")
# print(f"Площа: {rect1.area()}")
# print(f"Периметр: {rect1.perimeter()}")
# print("Виклик методу info():")
# rect1.info()
#
# print("\n2 об'єкт:")
# print(f"Ширина: {rect2.width}, Висота: {rect2.height}")
# print(f"Площа: {rect2.area()}")
# print(f"Периметр: {rect2.perimeter()}")
# print("Виклик методу info():")
# rect2.info()


#2


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         if isinstance(grade, (int, float)) and 1 <= grade <= 12:
#             self.grades.append(grade)
#         else:
#             print(f"Помилка: Оцінка {grade} для {self.name} є некоректною і не буде додана.")
#
#     def average(self):
#         if not self.grades:
#             return 0
#         return round(sum(self.grades) / len(self.grades), 2)
#
#     def __str__(self):
#         grades_str = ", ".join(map(str, self.grades)) if self.grades else "немає оцінок"
#         return f"Студент: {self.name} | Оцінки: [{grades_str}] | Середній бал: {self.average()}"
#
#
# student1 = Student("Іван Коваленко")
# student2 = Student("Марія Петренко")
#
# student1.add_grade(10)
# student1.add_grade(12)
# student1.add_grade(8)
# student1.add_grade(15)
# student1.add_grade(0)
#
# student2.add_grade(11)
# student2.add_grade(9)
#
# print()
# print(student1)
# print(student2)
#
# student3 = Student("Олексій Шевченко")
# print(student3)


#3

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         if isinstance(grade, (int, float)) and 1 <= grade <= 12:
#             self.grades.append(grade)
#
#     def average(self):
#         if not self.grades:
#             return 0
#         return round(sum(self.grades) / len(self.grades), 2)
#
#     def __str__(self):
#         grades_str = ", ".join(map(str, self.grades)) if self.grades else "немає оцінок"
#         return f"Студент: {self.name} | Оцінки: [{grades_str}] | Середній бал: {self.average()}"
#
#
# students = [
#     Student("Олександр Ткаченко"),
#     Student("Олена Бойко"),
#     Student("Дмитро Шевчук"),
#     Student("Ірина Мороз"),
#     Student("Василь Лисенко")
# ]
#
# students[0].add_grade(10)
# students[0].add_grade(11)
# students[0].add_grade(12)
#
# students[1].add_grade(12)
# students[1].add_grade(11)
# students[1].add_grade(12)
#
# students[2].add_grade(8)
# students[2].add_grade(9)
# students[2].add_grade(10)
#
# students[3].add_grade(12)
# students[3].add_grade(12)
# students[3].add_grade(11)
#
# students[4].add_grade(7)
# students[4].add_grade(6)
# students[4].add_grade(8)
#
# print("\tСписок усіх учнів")
# for student in students:
#     print(student)
#
# highest_avg = max(student.average() for student in students)
#
# best_students = [student for student in students if student.average() == highest_avg]
#
# print(f"\n\tНайвищий середній бал: {highest_avg}")
# print("Учень (або учні) з найкращим результатом:")
# for student in best_students:
#     print(f"- {student.name}")


#4

# class BankAccount:
#     def __init__(self, owner, balance=0.0):
#         self.owner = owner
#         self.balance = float(balance)
#
#     def deposit(self, amount):
#         if amount <= 0:
#             print(f"Помилка поповнення для {self.owner}: сума {amount} повинна бути більшою за 0.")
#         else:
#             self.balance += amount
#             print(f"Успішно: {self.owner} поповнив рахунок на {amount}. Новий баланс: {self.balance}")
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print(f"Помилка зняття для {self.owner}: сума {amount} повинна бути більшою за 0.")
#         elif amount > self.balance:
#             print(f"Помилка зняття для {self.owner}: недостатньо коштів на рахунку.")
#         else:
#             self.balance -= amount
#             print(f"Успішно: {self.owner} зняв з рахунку {amount}. Новий баланс: {self.balance}")
#
#     def info(self):
#         print(f"Власник рахунку: {self.owner} | Поточний баланс: {self.balance}")
#
#
# account1 = BankAccount("Іван Комаров", 1000.0)
# account2 = BankAccount("Олена Петренко", 250.0)
#
# print("\tПочатковий стан рахунків")
# account1.info()
# account2.info()
#
# print("\n\tОперації для рахунку 1 (Іван Комаров)")
# account1.deposit(500)
# account1.withdraw(300)
# account1.deposit(-50)
# account1.withdraw(2000)
#
# print("\n\tОперації для рахунку 2 (Олена Петренко)")
# account2.withdraw(100)
# account2.deposit(0)
# account2.withdraw(-20)
# account2.deposit(150)
#
# print("\n\tКінцевий стан рахунків")
# account1.info()
# account2.info()
