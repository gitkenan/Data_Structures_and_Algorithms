# How do you find the missing number in a given integer
# array of 1 to 100?

def missing_number(arr):
    for i in range(1, 101):
        if i in arr:
            pass
        else:
            return i

array = [j for j in range(1, 100)]

print(missing_number(array))