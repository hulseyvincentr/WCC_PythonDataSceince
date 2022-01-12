#import pandas
import pandas as pd
#import data set
stats = pd.read_csv('/Users/hulseyvincentr/Python_code/WCC_Python/Section5/DemographicData.csv')
#find number of rows
#print(len(stats))
print('Names of columns in data: ',stats.columns) #prints the names of each column in stats
#find nunmber of columns
print('Number of columns in data: ', len(stats.columns))

#most if the times you don't need to see the entire data set, so you can just print
#the top rows of the data set
print(stats.head(6)) #the input number lets it know how many rows from the top to print

#print the bottom rows
print(stats.tail(2))

#get some information on the columns
print(stats.info())  #identifies data types and column names

#get stats on the columns
print(stats.describe()) #yields mean, standard deviation, min, 25%th percentile, max, etc.

print(stats.describe().transpose()) # this will transpose the matrix for you!

