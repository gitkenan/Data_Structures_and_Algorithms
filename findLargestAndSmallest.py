# How do you find the largest and smallest number in an unsorted integer array?

def outer_values(unsorted_arr):
    biggest = 0
    smallest = 0

    # find biggest
    for i in unsorted_arr:
        if i > biggest:
            biggest = i
        else:
            smallest = i
    
    # find smallest
    for j in unsorted_arr:
        if j < smallest:
            smallest = j
        else:
            pass

    return 'The biggest is %r and the smallest is %r' % (biggest, smallest)

array = [4, 135135, 12, 325, 2, 89712398, 874, 8273464223, 87234627834, 293479328, 38745623789479783, 2374673, 87236472374, 6743]

print(outer_values(array))