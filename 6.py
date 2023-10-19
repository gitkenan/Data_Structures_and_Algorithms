# Let's write a function which can solve the following:
# Given a string of different characters, if there is less than 1 capital letter, refuse to accept the password.

def strictPass(inputString):
    # Initialize a variable to track whether a capital letter is found.
    has_capital = False

    # Loop through each character in the input string.
    for char in inputString:
        # Check if the character is a capital letter.
        if char.isupper():
            # If a capital letter is found, set has_capital to True and break out of the loop.
            has_capital = True
            break

    # Check the has_capital variable and return a result accordingly.
    if has_capital:
        print("Password accepted: It contains at least one capital letter.")
        return True
    else:
        print("Password refused: It does not contain any capital letters.")
        return False

# Example usage:
password = "Password123"
result = strictPass(password)

