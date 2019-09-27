# How do you find all pairs of an integer array whose sum is equal to a given number?

def pairs_which_sum_to(Arr, num):
    pairs = []
    for i in range(len(Arr)):
        for j in range(len(Arr[i:])):
            if Arr[i] + Arr[i + j] == num:
                pairs.append([Arr[i], Arr[i + j]])
            else:
                pass

    return pairs

Array = [1, 4, 8, 3, 6, 134, 13, 14, 26, 52, 11]

print(pairs_which_sum_to(Array, 27))

