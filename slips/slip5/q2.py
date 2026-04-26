import random

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = "HelloWorld"
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print("Random elements from list:", random.sample(lst, 3))
print("Random elements from string:", random.sample(s, 3))
print("Random elements from tuple:", random.sample(t, 3))
