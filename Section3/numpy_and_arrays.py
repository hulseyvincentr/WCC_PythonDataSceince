list1 = [23234, 23421, 56456, 456]
#print(list1)
#Two types of arrays:
#"Array" arrays are pre-built into Python
#numpy arrays come with package. Have better flexibility & control
import numpy as np #now we can just type "np" to get numpy :)
a = np.array(list1)
print(a)
print(type(a))

b = np.array([12, 345, True, "abc"]) 
print(b) #all of the variables appear as strings bc can't have different data
#types in an array
print(type(b))
#type:
#list1. #there are a some functions that can work with lists
pop = list1.pop()
print(pop)
#type
#a. #there are way more functions/methods that can work with arrays
a_mean = a.mean()
print(a_mean)