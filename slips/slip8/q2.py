filename = input("Enter filename: ")
position = int(input("Enter byte position: "))

try:
    with open(filename, "r") as f:
        f.seek(position)
        print("Content from position", position, ":")
        print(f.read())
except FileNotFoundError:
    print("File not found.")
