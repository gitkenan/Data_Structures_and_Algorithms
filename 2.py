# How do you find the duplicate number on a given integer array?

def duplicate_numbers(Arr):
    duplicates = []
    singulars = []
    for i in Arr:
        if i not in singulars:
            singulars.append(i)
        else:
            duplicates.append(i)

    return duplicates

Array = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 23, 23, 545, 3463, 235, 2363]

print(duplicate_numbers(Array))
