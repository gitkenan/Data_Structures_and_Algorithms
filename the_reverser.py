# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.
# This should be run on Python3 due to the way we are using print.

def theReverser(x):
    stringy = str(x)

    if stringy[0] == '-':
        return int('-'+stringy[:0:-1])
    else:
        return int(stringy[::-1])

print(theReverser(425))
