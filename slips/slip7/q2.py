import os

os.makedirs("finance_tools", exist_ok=True)

with open("finance_tools/__init__.py", "w") as f:
    f.write("")

with open("finance_tools/interest.py", "w") as f:
    f.write("def cal_interest(amount, year):\n    rate = 5\n    return (amount * rate * year) / 100\n")

with open("finance_tools/currency.py", "w") as f:
    f.write("def convert(amount):\n    return amount * 0.012\n")

from finance_tools import interest, currency

amount = float(input("Enter amount: "))
year = int(input("Enter years: "))

print("Simple Interest:", interest.cal_interest(amount, year))
print("Amount in USD:", currency.convert(amount))
