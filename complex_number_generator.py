# Let's generate a random complex number within an absolute value 

import random
from math import sqrt

def random_complex_number_within_abs(value):
    real_part = random.uniform(-value, value)
    imag_part = random.uniform(-value, value)
    return complex(real_part, imag_part)