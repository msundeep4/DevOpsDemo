# # Input name from the user
# name = input("Enter your name: ")

# # Input the number of times to print the name
# count = int(input("Enter the number of times to print your name: "))

# # Print the name in a loop
# for i in range(count):
#     print(f"{i + 1}: {name}")

# Input name from the user
name = input("Enter your name: ")

# Input the number of levels for the hierarchy
levels = int(input("Enter the number of hierarchy levels: "))

# Print the name in a hierarchy
for i in range(1, levels + 1):
    print(f"{' ' * (i - 1)}{name}")    