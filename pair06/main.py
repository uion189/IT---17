import tkinter as tk
from tkinter import messagebox
import student_utils

students = ["Anna", "Ivan", "Olha"]


def generate_report():
    input_value = entry_count.get().strip()

    if not input_value.isdecimal():
        messagebox.showerror("Помилка", "Будь ласка, введіть коректне ціле число!")
        return

    count = int(input_value)
    if not (1 <= count <= 20):
        messagebox.showerror("Помилка", "Кількість оцінок повинна бути в діапазоні від 1 до 20!")
        return

    report_lines = []
    for student in students:
        grades = student_utils.generate_grades(count)
        avg = student_utils.average_grade(grades)
        level = student_utils.get_level(avg)
        report_lines.append(f"{student}: {grades} - {avg} - {level}")

    report = "\n".join(report_lines)

    print(report)

    text_report.delete("1.0", tk.END)
    text_report.insert(tk.END, report)


root = tk.Tk()
root.title("Статистика учнів")
root.geometry("450x350")

label_info = tk.Label(root, text="Введіть кількість оцінок для учнів (1–20):")
label_info.pack(pady=5)

entry_count = tk.Entry(root)
entry_count.pack(pady=5)

generate = tk.Button(root, text="Сформувати звіт", command=generate_report)
generate.pack(pady=5)

text_report = tk.Text(root, height=12, width=50)
text_report.pack(pady=10)

root.mainloop()
