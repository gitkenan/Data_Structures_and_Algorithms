# What about something a bit simpler for a change - finding the absolute difference between the max and mimimum in an array

def get_absolute_difference(array_of_numbers):
    if len(array_of_numbers) < 2:
        return 0  # If there are fewer than 2 numbers, the absolute difference is 0.

    return abs(max(array_of_numbers) - min(array_of_numbers))

if __name__ == "__main__":
    # Example usage:
    numbers = [5, 3, 9, 1, 7]
    result = get_absolute_difference(numbers)
    print("The absolute difference is:", result)
