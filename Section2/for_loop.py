
a = range(5)
myList = [10, 100, 1000]
ii = 1
bb = 1
for i in range(5):
    print("Well hello there", i)
for i in range(5): #the condition
   print("Well hello there", i) #what's executed: prints message and counter
print(myList)
print(list(a))    

for jj in myList:
    print("jj is equal to: ", jj)

#two versions of the same thing
for ii in range(3):
    print("woot")
    ii = ii+1
print("now let's see if the while loop works")

while bb < 4: #this needs to be one more than the number of woots I want
    print("woot")
    bb = bb+1
print("All done :)")