import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generate a random password based on user-defined criteria.
    """
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type (letters, numbers, symbols) must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")

        use_letters = input("Include letters? (yes/no): ").lower().startswith('y')
        use_numbers = input("Include numbers? (yes/no): ").lower().startswith('y')
        use_symbols = input("Include symbols? (yes/no): ").lower().startswith('y')

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
