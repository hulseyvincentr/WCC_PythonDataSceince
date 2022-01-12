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

g = sns.FacetGrid(movies, row = 'Genre', col='Year', hue = 'Genre')
#plt.scatter(movies.CriticRating, movies.AudienceRating)
#we want to map this scatter contruct onto the blank facet grid created in
#line 21
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating')
#g.map requests a function, then requests some arguments
#because movies data structure is already called in line 21, we can now reference
#the CriticRatings and AudenceRatings columns in movies within g.map

#plt.show(g)

#can populate with any type of chart
h = sns.FacetGrid(movies, row = 'Genre', col='Year', hue = 'Genre')
h = g.map(plt.hist, 'BudgetMillions')
plt.show(h)
#practice using keyword arguments
i = sns.FacetGrid(movies, row = 'Genre', col='Year', hue = 'Genre')
kws = dict(s=50, linewidth = 0.5, edgecolor = 'black')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating', **kws)
plt.show(i)
