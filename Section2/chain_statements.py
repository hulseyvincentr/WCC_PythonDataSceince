answer = None #resets value for answer

import numpy as np
from numpy.random import randn
#this doesn't work :( doens't recognize numpy
x = randn()
if x > 1:
    answer = 'Greater than 1'
elif x>= -1:
    answer = "Between -1 and 1"
    else:
    answer = "Less than 1"
print(x)
print(answer)