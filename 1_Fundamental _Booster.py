print("Welcome to the Interactive Personal Data Collector!")
print("Please enter the following details.\n")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
fav_number = int(input("Enter your favourite number: "))

print("\nThank you! Here is the information collected:\n")

birth_year = 2025 - age

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Favourite Number: {fav_number}")

print("\n--- Data Type and Memory Information ---")
print(f"Name -> Value: {name}, Type: {type(name)}, Memory Address: {id(name)}")
print(f"Age -> Value: {age}, Type: {type(age)}, Memory Address: {id(age)}")
print(f"Height -> Value: {height}, Type: {type(height)}, Memory Address: {id(height)}")
print(f"Favourite Number -> Value: {fav_number}, Type: {type(fav_number)}, Memory Address: {id(fav_number)}")

print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

print("\nThank you for using the Personal Data Collector. Goodbye!")