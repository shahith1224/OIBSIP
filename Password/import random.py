import random
import string

def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    """Generates a random password based on user preferences."""
    char_pool = ""
    
    # Build the pool of allowed characters
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation
        
    # Validate that at least one option was selected
    if not char_pool:
        return "Error: You must select at least one character type."
        
    # Generate the password by picking random choices from the pool
    password = "".join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("--- Python Command-Line Password Generator ---")
    
    try:
        # 1. Get user input for length
        length = int(input("Enter desired password length (e.g., 12): "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return

        # 2. Get user preferences (y/n)
        print("\nInclude the following character types? (y/n)")
        opt_upper = input("Uppercase letters (A-Z)? ").lower() == 'y'
        opt_lower = input("Lowercase letters (a-z)? ").lower() == 'y'
        opt_numbers = input("Numbers (0-9)? ").lower() == 'y'
        opt_symbols = input("Symbols (!@#$ etc)? ").lower() == 'y'

        # 3. Generate and display
        result = generate_password(length, opt_upper, opt_lower, opt_numbers, opt_symbols)
        
        print("\n--- Your Generated Password ---")
        print(result)
        print("-------------------------------")

    except ValueError:
        print("Error: Please enter a valid number for the length.")

if __name__ == "__main__":
    main()