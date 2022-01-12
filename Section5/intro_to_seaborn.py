import pandas as pd
#import data set
stats = pd.read_csv('/Users/hulseyvincentr/Python_code/WCC_Python/Section5/DemographicData.csv')

#print(stats.head())
#we want to rename our columns with no spaces in them
stats.columns = ['CountryName', 'CountryCode','BirthRate', 'InternetUsers', 'IncomeGroup']
#print('Corrected column names: ', stats.columns)

#this package builds on top of matplotlib
#already did pip3 install for matplotlib, seaborn
import matplotlib.pyplot as plt
import seaborn as sns #seaborn builds on top of matplotlib, so still need to import that
import warnings
warnings.filterwarnings('ignore') #turn off warnings bc some stuff isn't an integer, 
#so will get lots of warnings from package
#% matplotlib inline Jupyter command
plt.rcParams['figure.figsize'] = 8,4 #increases figure size from default

#Create a distribution
vis1 = sns.distplot(stats["InternetUsers"], bins=30) #bins = x divisions
#plt.show(vis1)

vis2 = sns.boxplot(data = stats, x = 'IncomeGroup', y = 'BirthRate')
plt.show(vis2)
#Use this website: https://seaborn.pydata.org/examples/index.html
#Has different types of graphs and color schemes that you can use

