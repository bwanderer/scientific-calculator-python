############################################################################
# Python
# Date: 9/4/2024
# This program evaluates a function at a specific range of x.
############################################################################

import math

print('This shows the evaluation of (1 + (1 / x))^x evaluated for values of x ranging from 1 to 10,000,000')

x_values = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]

print('Evaluating (1 + (1 / x))^x at 1, 10, 100,... 100000000 and outputting results would give:')

for value in x_values:
    result = math.pow((1 + (1 / value)), value)
    print(result)
