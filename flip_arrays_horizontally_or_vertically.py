# This programme does what the title says it does. 

def flip_array(arr, direction):
    if direction == 'horizontal':
        # Flip horizontally (left to right)
        # row[::-1] is the expression that is evaluated for each 
        # row. It uses slicing to reverse the order of elements in 
        # each row. row[::-1] means to start from the end of the 
        # list (-1 index) and move towards the beginning, 
        # reversing the order of elements.
        return [row[::-1] for row in arr]
    elif direction == 'vertical':
        # Flip vertically (upside down)
        return arr[::-1]
    else:
        # Handle invalid direction
        raise ValueError("Invalid direction. Use 'horizontal' or 'vertical'.")

def main():
    # Example array
    original_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("We are starting with the array:")
    for row in original_array:
            print(row)
    # Input prompt
    direction = input("Enter 'horizontal' or 'vertical' to flip the array: ")
    
    try:
        flipped_array = flip_array(original_array, direction)
        print("Flipped Array:")
        for row in flipped_array:
            print(row)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
