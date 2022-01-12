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

#Histograms
#already know the following method:
m1 = sns.distplot(movies.AudienceRating, bins = 15)
plt.show(m1)

#we can also use pyplot to get figures, and it has a lot of 
#useful included functions/options in it
#sns.set_style('white')
sns.set_style('darkgrid') #sets colors/grid stuff for plot
m2 = plt.hist(movies.CriticRating, bins = 15)
plt.show(m2)