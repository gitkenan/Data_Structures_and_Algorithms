# How do you find the missing number in a given integer
# array of 1 to 100?

def missing_number(arr):
    for i in range(1, upper_limit):
        if i in arr:
            pass
        elif i<upper_limit/20:
            print("This array has clear issues.")
            return i
        else:
            return i

array = [j for j in range(1, 100)]

print(missing_number(array, 100))