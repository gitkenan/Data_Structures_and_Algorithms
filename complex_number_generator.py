# Let's generate a random complex number within an absolute value 

import random
from math import sqrt

def random_complex_number_within_abs(value):
    real_part = random.uniform(-value, value)
    imag_part = random.uniform(-value, value)
    return complex(real_part, imag_part)
    
if __name__ = "__main__":
    some_value = random.uniform(0, 1000)
    x_in_c = random_complex_number_within_abs(some_value)
    print("The generated complex value is " + x_in_x)