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

#a dashboard is a combination of plots
sns.setstyle = ("darkgrid")
f, axes = plt.subplots(2, 2, figsize = (15, 15))

k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0,0])
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax = axes[0,1])
k1.set(xlim=(-20, 160))
k2.set(xlim = (-20, 160))
z = sns.violinplot(data=movies, x='Genre', y='CriticRating', ax = axes[1,1])
k1 = sns.kdeplot(movies.CriticRating, movies.AudienceRating, shade = True, shade_lowest=False,
                 cmaps = 'Reds')
k1b = sns.kdeplot(movies.CriticRating, movies.AudienceRating,
                 cmaps = 'Reds')
plt.show()