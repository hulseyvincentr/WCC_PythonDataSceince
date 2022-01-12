#import pandas
import pandas as pd
#import data set
stats = pd.read_csv('/Users/hulseyvincentr/Python_code/WCC_Python/Section5/DemographicData.csv')
#Recall that we previously renamed the columns to not have spaces
stats.columns = ['CountryName', 'CountryCode','BirthRate', 'InternetUsers', 'IncomeGroup']

stats[['CountryCode', 'BirthRate', 'InternetUsers']][4:8] #only looks at rows 3:8 in 2 columns
#need two sets of brackets bc you're inputting a list into an input spot

#Mathematical operations:
result = stats.BirthRate * stats.InternetUsers

#how to add a column
stats['MyCalc'] = stats.BirthRate * stats.InternetUsers;
print(stats.head())

#how to remove a column. Let's remove MyCalc
#stats.drop('MyCalc')  #this won't work because by default it looks for rows
stats.drop('MyCalc', 1) #one is for the axis (x axis is dimension 0, y axis is dimension 1)
print(stats.head())
#this returns a new object with labels in requested axis remove, but doesn't affect actual data structure
stats = stats.drop('MyCalc', 1) 