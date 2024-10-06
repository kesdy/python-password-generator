import random
import string

def password_generator(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    # Create a basic character set
    characters = string.ascii_lowercase  # Lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase  # Uppercase letters
    if use_numbers:
        characters += string.digits  # Digits
    if use_symbols:
        characters += string.punctuation  # Symbols

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Specify the password length and character types
length = int(input("Enter password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Generate the password
generated_password = password_generator(length, use_uppercase, use_numbers, use_symbols)
print("Generated Password:", generated_password)
