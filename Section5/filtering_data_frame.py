## Filtering is all about rows
#import pandas
import pandas as pd
#import data set
stats = pd.read_csv('/Users/hulseyvincentr/Python_code/WCC_Python/Section5/DemographicData.csv')

print(stats.head())
#we want to rename our columns with no spaces in them
stats.columns = ['CountryName', 'CountryCode','BirthRate', 'InternetUsers', 'IncomeGroup']
print(stats.columns)

#prints list of bools about which countries have
#less than 2% internet users
InternetFilter = stats.InternetUsers < 2
#can list elements in stats that fulfil 
# filter statement
print(stats[InternetFilter])

BirthFilter = stats.BirthRate > 40
print(stats[BirthFilter])

#combine filters: make a dataframe with
#internet users less than 2 and birthrate > 40
#Cannot type:
#stats[stats.BirthRate > 40 and stats.InternetUsers < 2]
#the and is expecting a single true or false to combine. 
#and doesn't know how to work with these objects

#InternetFilter and BirthFilter;  #this yields an error
#because the filters contain lists of boolean values
#use &, which is a bit-wise operator and goes element by elemnt

#print('Two filters applied', stats[InternetFilter & BirthFilter])
#this will yield an error bc doesn't know which condition to 
#apply first. It requires more brackets

print('Two filters applied', stats[(stats.BirthRate > 40) & (stats.InternetUsers < 2)])

print(stats[stats.IncomeGroup == 'High income'])
#how to find possible values in column? use .unique
print(stats.IncomeGroup.unique())

#find everything you can out about Malta (find row)
print(stats[stats.CountryName == 'Malta'])