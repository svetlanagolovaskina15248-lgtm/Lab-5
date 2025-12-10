import re

with open('task2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

pattern = r'<\w+'  # ищем символ '<', за которым следуют буквы/цифры
matches = re.findall(pattern, html_content)

unique_tags = set(matches)

print(unique_tags)
