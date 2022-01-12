myFirstList = [3, 45, 56, 732]
print(myFirstList)
print(type(myFirstList)) #tells us what data type it is
#recall lists can contain mix of data types

list2 = ["hello", 24, True, 55.3]
list3 = ['how are you?', 55, myFirstList]
#contains a list with a list in it!
print(list3)

range(15)
print(range(15))
#range is a generator. In Python 2 it used to give a list,
#but in Py3 it uses less memory to simply give start/ending values for a list

list(range(15)) #this generates the actual list
print(list(range(15)))
#if only one input value, goes from 0 to that number
#with comma will use 1st input as starting poin t
z = list(range(3,8))
print(z)

#can specify step as the 3rd input
g = list(range(100, 111, 2))
print(g)