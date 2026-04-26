import re

s = input("Enter a string: ")

capital_words = re.findall(r'\b[A-Z][a-z]*\b', s)
print("Words starting with capital letter:", capital_words)

modified = re.sub(r'[^a-zA-Z0-9\s]', '', s)
print("String after removing special characters:", modified)
