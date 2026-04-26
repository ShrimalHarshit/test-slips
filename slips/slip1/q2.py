import os

os.makedirs("vehicle/types", exist_ok=True)

with open("vehicle/__init__.py", "w") as f:
    f.write("")

with open("vehicle/types/__init__.py", "w") as f:
    f.write("")

with open("vehicle/types/cars.py", "w") as f:
    f.write("def available_models():\n    return ['Toyota', 'Honda', 'Ford', 'BMW', 'Audi']\n")

with open("vehicle/types/bikes.py", "w") as f:
    f.write("def available_models():\n    return ['Splendor', 'Pulsar', 'Apache', 'Bullet', 'Shine']\n")

from vehicle.types import cars, bikes

print("Available Car Models:", cars.available_models())
print("Available Bike Models:", bikes.available_models())
