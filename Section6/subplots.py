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

sns.set_style("dark")
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating)
#plt.show(k1)

k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating)
#plt.show(k2)

#making subplots now. f is a coding dimension, 1 row, 2 columns
f, axes = plt.subplots(1, 2, figsize = (12,6), sharex=True, sharey= True) 
#number of rows, number of columns, figsize is an inner function. ax is a 
#single axis object or an array of axes objects. will share the same
#x axis and y axis
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0])
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax = axes[1])
k1.set(xlim=(-20, 160))

plt.show()
