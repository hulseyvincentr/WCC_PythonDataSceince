#Introducing the mighty COLON
# start: end: step
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
print(letters[:])
print(letters[:7])
print(letters[2:7])
print(letters[-8:7]) #will be the same result
print(letters[-8:-3])
print(letters[::3])

#challenge: what if you specify a negative step?
#you need to "reverse" the start and ending numbers
print(letters[0:5:-2]) #this yields empty bracket
print(letters[5:0:-2]) #this yields correct answer :)