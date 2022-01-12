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

#plt.hist(movies.BudgetMillions)
#plt.show()

movies[movies.Genre =='Drama'] #filters out non-drama movies
print(movies[movies.Genre =='Drama'].BudgetMillions)

#making a kernel density estimate (KDE) plot
#this is used for visualizing probability density of a continuous variable
#vis1 = sns.lmplot(data=movies, x='CriticRating', y='AudienceRating', 
#                  fit_reg = False, hue = 'Genre', size = 7, aspect = 1)

k1 = sns.kdeplot(movies.CriticRating, movies.AudienceRating, shade = True, shade_lowest=False,
                 cmaps = 'Reds')
k1b = sns.kdeplot(movies.CriticRating, movies.AudienceRating,
                 cmaps = 'Reds')
#overlays to create cleaner map
plt.show()
#this shows the kernel density estimate - shows where the largest density of points are
#and how density is distributed across the chart. kind of like a heat map
