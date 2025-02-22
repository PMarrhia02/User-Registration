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



def main():
    valid_first_name()
    valid_last_name()
    valid_email()
if __name__ == "__main__":
    main()
