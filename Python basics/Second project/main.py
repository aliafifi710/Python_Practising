# Program to calculate the age of a person or item

# Input: Year of birth/creation
year_born = int(input("Enter the year the person was born or the item was created: "))

# Input: Current year
current_year = int(input("Enter the current year: "))

# Calculate age
age = current_year - year_born

# Output the result
if age < 0:
    print("The input years are invalid. The year of birth/creation cannot be in the future.")
else:
    print(f"The age of the person or item is {age} years.")
