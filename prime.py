# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Print prime numbers in the range
print(f"Prime numbers between {start} and {end}:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number)