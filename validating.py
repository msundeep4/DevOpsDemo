# Function to validate username and password
def validate_credentials(username, password):
    # Example validation logic
    valid_username = "admin"
    valid_password = "password123"

    if username == valid_username and password == valid_password:
        return True
    return False

# Read input from the user
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

# Validate the credentials
if validate_credentials(input_username, input_password):
    print("Login successful!")
else:
    print("Invalid username or password.")