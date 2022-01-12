import numpy as np #important to do this or won't have array function
#we already know how to slice lists:
list1 = [123, 345, 456, 2341]
print("list 1 excluding the first element (1:)", list1[1:])
#now do this with arrays
a = np.array([234, 45494, 50398, 1, 394858, -29384])
print("elements 2 thru 3 (indexed by 2:4) of array a are: ", a[2:4])
  
#Whenever you slice an array, you are NOT creating  copy of the array.
#lists create a new copy, but in arrays you're acting on the original array

b = a[2:4]
b[:] = 111
print(a) #now the two elements in a referred to by b have been changed
#how to create a copy of array
c = a.copy()
c[0] = 0
print("array c is a copy of array a with a different 1st element: ", c)