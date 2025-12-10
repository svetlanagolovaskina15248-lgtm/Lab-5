import re
import csv

# Рег. выраж. для поиска данных
email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?'
date = r'\d{4}-\d{2}-\d{2}'
name = r'^[A-Z][a-z]+$|^[A-Z][a-z]+-[A-Z][a-z]+$'

with open('task3.txt', 'r') as file:
    content = file.read()

#Разбиваем на слова
words = content.split()

email_res = []
url_res = []
date_res = []
name_res = []
id_res = []

#Распределяем слова
for word in words:
    if re.fullmatch(email, word):
        email_res.append(word)
    elif re.fullmatch(url, word):
        url_res.append(word)
    elif re.fullmatch(date, word):
        date_res.append(word)
    elif re.fullmatch(name, word):
        name_res.append(word)
    elif word.isdigit():        #Число
        id_res.append(word)

#Проверка, одинаковы ли все списки по длине
print(f"ID={len(id_res)}, Фамилий={len(name_res)}, Email={len(email_res)}, Дата={len(date_res)}, URL={len(url_res)}")

#CSV файл
with open('res.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    #Заголовок
    writer.writerow(['ID', 'Last Name', 'Email', 'Registration Date', 'Website'])
    
    #Данные
    for i in range(min(len(id_res), len(name_res), len(email_res), len(date_res), len(url_res))):
        writer.writerow([id_res[i], name_res[i], email_res[i], date_res[i], url_res[i]])
