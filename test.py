# Define an array with some values
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Input a value from the user
user_input = int(input("Enter a value to filter the array: "))

# Print elements greater than the input value
print(f"\nPrinting elements greater than {user_input}:")
for value in values:
    if value > user_input:
        print(value)