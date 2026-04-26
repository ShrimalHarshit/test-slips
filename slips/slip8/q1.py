import re

string = input("Enter string: ")
substring = input("Enter substring: ")

if re.match(substring, string):
    print("The string starts with the given substring.")
else:
    print("The string does not start with the given substring.")
