age = int(input("Введіть вік (від 0 до 120): "))

last_digit = age % 10
last_two_digits = age % 100

if age < 0:
    word = "ти ше замаленький"
elif age > 120:
    word = "добре зберігся молодець"
elif 11 <= last_two_digits <= 14:
    word = "років"
elif last_digit == 1:
    word = "рік"
elif 2 <= last_digit <= 4:
    word = "роки"
else:
    word = "років"

print(age, word)
