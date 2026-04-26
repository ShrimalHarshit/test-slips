import pandas as pd

data = {
    "Company": ["Apsara", "Natraj", "Cello", "Parkar", "Apsara"],
    "Count": [15, 20, 25, 35, 20],
    "Price": [250, 200, 600, 900, 300]
}
index = ["Pencil", "Pencil", "Pen", "Pen", "Eraser"]

df = pd.DataFrame(data, index=index)

print("a) All rows with label Pencil:")
print(df.loc["Pencil"])

df.loc["Eraser", "Count"] = 25
print("\nb) After changing Eraser count to 25:")
print(df)

print("\nc) Only Company and Price columns:")
print(df[["Company", "Price"]])

print("\nd) Rows with labels Pencil and Pen:")
print(df.loc[["Pencil", "Pen"]])

df.rename(columns={"Count": "Quantity"}, inplace=True)
print("\ne) After renaming Count to Quantity:")
print(df)
