fav = input('Have you heard of Sampson?')
possibleYes = {'yes', 'yeah', 'yup'}
numPossibleYes = len(possibleYes)
possibleNo = {'no','nah','nope'}
numPossibleNo = len(possibleNo)

doesItMatchPositive = False

for i in range(0, numPossibleYes):
    currentPossibleYes = possibleYes{i}
    if fav == currentPossibleYes:
        doesItMatchPositive = True
    
for i in range(0, numPossibleNo):
     currentPossibleNo = possibleNo{i}
    if fav = currentPossibleNo:
    doesItMatchPositive = False
    else:
    print("You didn't choose yes or no. >:()")
    
    if doesItMatchPositive == True:
    print("You're a poser")
    elif doesItMatchPositive == False:
    print("HEYYYYoooooo")
    else:
        print("You decided nothing. Boooooo")