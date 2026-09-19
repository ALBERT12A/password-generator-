import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("=== Random Password Generator ===")
    try:
        user_input = int(input("Enter password length (e.g. 12): "))
        if user_input < 4:
            print("Error: Password length must be at least 4 characters.")
        else:
            print("\nYour secure password:", generate_password(user_input))
    except ValueError:
        print("Error: Please enter a valid number.")

