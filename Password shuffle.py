
import random
import string

def generate_random_password(length=12):
    if length < 8:
        print("Password length should be at least 8 characters for security.")
        return None
    
    # Define character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # special characters
    
    # Ensure the password has at least one letter, digit, and symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with random choices from all sets combined
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)
    
    # Shuffle to avoid predictable pattern
    random.shuffle(password)
    
    # Join list to string
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter desired password length (minimum 8): "))
    pwd = generate_random_password(length)
    if pwd:
        print("Generated password:", pwd)
