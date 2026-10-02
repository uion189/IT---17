# 1
# text = input()
#
# chars = "aeiouyаеєиіїоуюя"
#
# total_chars = len(text)
# letters = 0
# digits = 0
# spaces = 0
# chars_count = 0
#
# for char in text:
#     if char.isalpha():
#         letters += 1
#
#         if char.lower() in chars:
#             chars_count += 1
#
#     elif char.isdigit():
#         digits += 1
#
#     elif char.isspace():
#         spaces += 1
#
# words = len(text.split())
#
# print(f"Символів: {total_chars}")
# print(f"Літер: {letters}")
# print(f"Цифр: {digits}")
# print(f"Пробілів: {spaces}")
# print(f"Голосних: {chars_count}")
# print(f"Слів: {words}")

# 2
# parts = input().split()
#
# first = parts[0].capitalize()
# second = parts[1][0].upper()
# third = parts[2][0].upper()
#
# result = f"{first} {second}.{third}."
#
# print(result)

# 3
# str1 = input("Введіть перший рядок: ")
# str2 = input("Введіть другий рядок: ")
#
# clean_str1 = "".join(str1.split()).lower()
# clean_str2 = "".join(str2.split()).lower()
#
# if sorted(clean_str1) == sorted(clean_str2):
#     print("Результат: Рядки є анаграмами")
# else:
#     print("Результат: Рядки НЕ є анаграмами")

# # 4
# words = input().split()
#
# u_words = []
# for word in words:
#     lower_word = word.lower()
#     if lower_word not in u_words:
#         u_words.append(lower_word)
# count_u = len(u_words)
#
# max_len = max(len(word) for word in words)
# min_len = min(len(word) for word in words)
#
# longest_words = []
# for word in words:
#     if len(word) == max_len and word not in longest_words:
#         longest_words.append(word)
#
# shortest_words = []
# for word in words:
#     if len(word) == min_len and word not in shortest_words:
#         shortest_words.append(word)
#
# print(f"Унікальних слів: {count_u}")
# print(f"Найдовші: {', '.join(longest_words)}")
# print(f"Найкоротші: {', '.join(shortest_words)}")
#
# target_word = input("Введіть слово яке потрібно замінити: ")
# new_word = input("Введіть нове слово: ")
#
# replace_words = []
# for word in words:
#     if word == target_word:
#         replace_words.append(new_word)
#     else:
#         replace_words.append(word)
#
# result = " ".join(replace_words)
# print(f"Після заміни: {result}")
