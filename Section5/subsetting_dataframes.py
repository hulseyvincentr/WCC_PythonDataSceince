#import pandas
import pandas as pd
#import data set
stats = pd.read_csv('/Users/hulseyvincentr/Python_code/WCC_Python/Section5/DemographicData.csv')

print(stats.head())
#we want to rename our columns with no spaces in them
stats.columns = ['CountryName', 'CountryCode','BirthRate', 'InternetUsers', 'IncomeGroup']
print(stats.columns)

#### subsetting rows
#use slicing
stats[21:26] #grab rows 21 thru 25
stats[185:] #this grabs rows 185 thru the end
stats[:10] #the  same as stats.head(10)
# Python knows to grab rows bc each row is a new entry
#exercise: reverse the data frame
print(stats[ : : -1]) # :) to modify, type stats = stats[: : -1]
#get only every 20th row
print(stats[: : 20])
print('##################################################')

# subsetting columns
#how to extract one column
print(stats['CountryName'])
#what if you only want the top row of the first columns?
print(stats['CountryName'].head())

stuffToPrint = ['CountryName', 'BirthRate']
print(stats[stuffToPrint].head())
#Quick access - requires name of column to be one word
#stats['Birthrate']
#in R: stats$BirthRate is an yeasy way to get it
print(stats.BirthRate.head())


print('##################################################')
# combining subsetting by rows and columns
# access rows 4-7 of CountryName and BirthRate columns
print(stats[4:8][['CountryName', 'BirthRate']])
#this takes subset 1 (the rows), then takes a second subset from that
#subset (the columns of that subset). Order doesn't matter.
#this is equivalent to the two lines:
#subset1 = stats[4:8]
#subset2 = subset1[['CountryName', 'BirthRate']]

