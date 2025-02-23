import re


def valid_first_name():
    """
    Description :
    Validates the first name.

    - Must start with an uppercase letter.
    - Remaining characters can be uppercase or lowercase.
    - Minimum length: 3 characters.

    Returns:
        None
    """
    try:
        pattern = r"^[A-Z][a-zA-Z]{2,}$"
        first_name = input("Enter first name: ").strip()
        if not first_name:
            raise ValueError("First name cannot be empty.")
        if re.match(pattern, first_name):
            print("It is a valid name.")
        else:
            print("It is an invalid name. It should start with a capital letter and have at least 3 characters.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def valid_last_name():
    """
    Description :
    Validates the first name.

    - Must start with an uppercase letter.
    - Remaining characters can be uppercase or lowercase.
    - Minimum length: 3 characters.

    Returns:
        None
    """
    try:
        pattern = r"^[A-Z][a-zA-Z]{2,}$"
        last_name = input("Enter last name: ").strip()
        if not last_name:
            raise ValueError("Last name cannot be empty.")
        if re.match(pattern, last_name):
            print("It is a valid name.")
        else:
            print("It is an invalid name. It should start with a capital letter and have at least 3 characters.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def valid_email():
    """
    Validates an email address.

<<<<<<< HEAD
    - Must contain alphanumeric characters before @.
    - Can have an optional dot before @.
    - Must have a domain after @ with at least 2 letters.
    - Can have an optional subdomain.

    Returns:
        None
    """
    try:
        pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$"
        email = input("Enter your email: ").strip()

        if not email:
            raise ValueError("Email cannot be empty.")

        if re.match(pattern, email):
            print("Valid email.")
        else:
            print("Invalid email format. Please enter a valid email (e.g., example@gmail.com).")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def valid_mobile_number():
    """
    Validates an Indian mobile number.

    - Must start with '91'.
    - Must have 10 digits starting with 6-9.

    Returns:
        None
    """
    try:
        pattern = r"^(91)[6-9][0-9]{9}$"
        mobile_number = input("Enter your phone number: ").strip()

        if not mobile_number:
            raise ValueError("Mobile number cannot be empty.")

        if re.match(pattern, mobile_number):
            print("Valid mobile number.")
        else:
            print("Not a valid number.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def validate_password():
    """
    Validates if a password meets minimum length criteria.
    
    - Must be at least 8 characters long.

    Returns:
        None
    """
    try:
        password = input("Enter your password: ").strip()

        if not password:
            raise ValueError("Password cannot be empty.")

        pattern = r"^.{8,}$"
        if re.match(pattern, password):
            print("Valid password.")
        else:
            print("Invalid password. It must be at least 8 characters long.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def password_uppercase():
    """
    Checks if a password contains at least one uppercase letter.

    - Must be at least 8 characters long.
    - Must contain at least one uppercase letter.

    Returns:
        None
    """
    try:
        password = input("Enter a password for uppercase validation: ").strip()

        if not password:
            raise ValueError("Password cannot be empty.")

        pattern = r"^(?=.*[A-Z]).{8,}$"

        if re.match(pattern, password):
            print("Password is valid (contains at least one uppercase letter).")
        else:
            print("Invalid password. It must have at least one uppercase letter.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

import re

def password_numeric():
    """
    Validates if a password contains at least one numeric digit and one uppercase letter.

    - Must be at least 8 characters long.
    - Must contain at least one uppercase letter.
    - Must contain at least one digit.

    Returns:
        None
    """
    try:
        password = input("Enter a password for numeric validation: ").strip()

        if not password:
            raise ValueError("Password cannot be empty.")

        # Corrected Regex Pattern
        pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"

        if re.match(pattern, password):
            print("✅ Valid password (contains at least one uppercase letter and one number).")
        else:
            print("❌ Invalid password. It must have at least one uppercase letter and one number.")

    except ValueError as ve:
        print(f"Error: {ve}")

def password_special_character():
    """
    Validates if a password contains at least one special character.

    - Must be at least 8 characters long.
    - Must contain at least one uppercase letter.
    - Must contain at least one numeric digit.
    - Must contain at least one special character.

    Returns:
        None
    """
    try:
        password = input("Enter a password for special character validation: ").strip()

        if not password:
            raise ValueError("Password cannot be empty.")

        pattern = r"^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[^a-zA-Z0-9]).{8,}$"

        if re.match(pattern, password):
            print("Valid password (contains at least one uppercase letter, one number, and one special character).")
        else:
            print("Invalid password. Must contain at least one uppercase letter, one number, and one special character.")

    except ValueError as ve:
        print(f"Error: {ve}")

def main():
    valid_first_name()
    valid_last_name()
    valid_email()
    valid_mobile_number()
    validate_password()
    password_uppercase()
    password_numeric()
    password_special_character()
if __name__ == "__main__":
    main()
