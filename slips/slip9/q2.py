filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        content = f.read()

    print(content)

    chars = len(content)
    words = len(content.split())
    lines = len(content.splitlines())

    print("Total characters:", chars)
    print("Total words:", words)
    print("Total lines:", lines)

except FileNotFoundError:
    print("File does not exist.")
