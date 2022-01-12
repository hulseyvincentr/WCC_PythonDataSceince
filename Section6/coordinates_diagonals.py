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


#Adjust axes and add diagonals
g = sns.FacetGrid(movies, row = 'Genre', col='Year', hue = 'Genre')
kws = dict(s=50, linewidth = 0.5, edgecolor = 'black')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating', **kws)
g.set(xlim=(0, 100), ylim = (0, 100))

#need to iterate to add diagonals
for ax in g.axes.flat: #g.axes is an array of the elements of the facet grid, flat iterates over the array, even though it's 2D 
    ax.plot((0, 100), (0, 100), c="gray", ls="--")
g.add_legend()    
plt.show(g)