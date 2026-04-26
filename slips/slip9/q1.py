import pandas as pd

data = {
    "Subject_Name": ["Maths", "Science", "English", "History", "Geography", "Hindi", "Physics", "Chemistry", "Biology", "Computer"],
    "Marks": [85, 90, 78, 65, 70, 88, 92, 75, 80, 95]
}

df = pd.DataFrame(data)
print("First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
