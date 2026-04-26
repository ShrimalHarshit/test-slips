s = input("Enter a string: ")

vowels = 0
consonants = 0
special = 0

for ch in s:
    if ch.lower() in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Special Symbols:", special)
