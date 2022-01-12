#Using .at() and .iat()

import pandas as pd
#import data set
stats = pd.read_csv('/Users/hulseyvincentr/Python_code/WCC_Python/Section5/DemographicData.csv')

print(stats.head())
#we want to rename our columns with no spaces in them
stats.columns = ['CountryName', 'CountryCode','BirthRate', 'InternetUsers', 'IncomeGroup']
print('Corrected column names: ', stats.columns)
# this will be all about accessing individual elements
#stats[2,2] will yield an error. This is because you
#usually access rows and use filter rather than going to
#the individual element

# .iat is for labels
#important: even integers are treated as labels (for integer location)
# .iat is for integer location
print(stats.iat[3,4])
print(stats.iat[0,1]) #counts rows from the top, columns from the left

#.at will look at labels
print(stats.at[2, 'BirthRate'])

#why do we need .at? 
subset10 = stats[::10]
print(subset10.iat[10, 0])
print(subset10.at[10, 'CountryName'])
#these yield different values: .iat starts counting as we would expect.
#.at looks for the label 10, which, in this case, finds the 10th country number (1st column's element)

