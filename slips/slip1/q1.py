import pandas as pd

mobiles = {
    "Mobile": ["Samsung", "iPhone", "OnePlus", "Redmi", "Realme"],
    "Price": [45000, 80000, 35000, 15000, 20000]
}

df = pd.DataFrame(mobiles)
print(df)
