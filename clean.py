import re

with open("dictionary.txt", "r", encoding="utf-8") as file:
    content = file.read()

cleaned_content = re.sub(r'[a-zA-Z0-9.,!?\'"()-_,]+', '', content)

with open("cleaned_dictionary.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_content)

print("File cleaned successfully.")