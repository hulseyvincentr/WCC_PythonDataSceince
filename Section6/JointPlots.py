#import necessary packages
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
import seaborn as sns
#turn off warnings for now
import warnings
warnings.filterwarnings('ignore')

#import data from .csv file
movies = pd.read_csv("Movie-Ratings.csv")
#rename column headers to remove spaces so we can use . operator
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']

#change Film, Genre, and Year colunns into Category data type
movies.Film = movies.Film.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')

#create Jointplots
j = sns.jointplot(data=movies, x='CriticRating', y = 'AudienceRating',
                  kind = 'hex')
#kind variable's default is a scatter plot. changing it to hex
#makes a hexago-shaped scatter plot with density corrleated to 
#darkness of hexagon color
plt.show(j)
#how to read this jointplot:
#this is a scatter plot, and shows if there is a relationship/
#dependency of the two variables. 
#the top chart and side chart show the distributions of each
#variable.
