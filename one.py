import re

with open("task1-ru.txt", 'r', encoding='utf-8') as file:
    text = file.read()

#Слова от 3 до 5 букв
words_3_to_5 = re.findall(r'\b\w{3,5}\b', text)
print(f"Кол-во слов: {len(words_3_to_5)}")

#Числа больше 3 знаков
all_numbers = re.findall(r'\b\d+\b', text)
long_numbers = [num for num in all_numbers if len(num) > 3]
print(f"Кол-во чисел: {len(long_numbers)}")

with open("words_3_to_5.txt", 'w', encoding='utf-8') as f1:
    f1.write('\n'.join(words_3_to_5))

with open("long_numbers.txt", 'w', encoding='utf-8') as f2:
    f2.write('\n'.join(long_numbers))
