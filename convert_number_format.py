# The purpose of this file is to create an algorithm
# which will be able to be used by phone companies
# to deal with different formats of phone number inputs.

def format_phone_number(input_number):
    # Remove spaces and replace leading +44 with 0
    cleaned_number = input_number.replace(" ", "").replace("+44", "0").lstrip("0")
    
    # Ensure the formatted number has a total of 11 digits
    if len(cleaned_number) != 11:
        print("Invalid input. Please enter a valid 11-digit phone number.")
        return None

    return f"07{cleaned_number[2:]}"

def main():
    while True:
        user_input = input("Enter your phone number: ")
        if user_input.lower() == 'exit':
            break
        formatted_number = format_phone_number(user_input)
        # since it may not have been successful, the below is a check
        if formatted_number:
            print(f"Formatted number: {formatted_number}")

if __name__ == "__main":
    main()
