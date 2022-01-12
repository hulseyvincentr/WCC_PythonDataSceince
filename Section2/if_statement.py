answer = None #resets value for answer

import numpy as np
from numpy.random import randn
#this doesn't work :( doesn't recognize numpy
#now it does!! Use pip3 to install from now on (in terminal window)
x = randn()
if x > 1:
    answer = 'Greater than 1'
else:
    answer = "Less than 1"
print(x)
print(answer)