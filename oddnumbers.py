# Function to check if a number is odd
def is_odd(num):
    return num % 2 != 0

# Input range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Print odd numbers in the range
print(f"Odd numbers between {start} and {end}:")
for number in range(start, end + 1):
    if is_odd(number):
        print(number)