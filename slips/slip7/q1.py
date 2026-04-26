import pandas as pd

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
df = pd.DataFrame(lst, columns=["Values"])

print(df)
print("Sum:", df["Values"].sum())
print("Mean:", df["Values"].mean())
print("Median:", df["Values"].median())
print("Mode:", df["Values"].mode()[0])
print("Standard Deviation:", df["Values"].std())
