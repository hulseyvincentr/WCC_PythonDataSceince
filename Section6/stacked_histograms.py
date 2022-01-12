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

#overlapped histograms of the budget in millions for action movies
#and thirller and drama
#plt.hist(movies[movies.Genre == 'Action'].BudgetMillions, bins = 15)
#plt.hist(movies[movies.Genre == 'Drama'].BudgetMillions, bins = 15)
#plt.hist(movies[movies.Genre == 'Thriller'].BudgetMillions, bins = 15)
#plt.show()

#this shows all the graphs, but we want these to be stacked,
#so need to change the input style. Input the filers in a list:
#movieFilterList = [movies[movies.Genre == 'Action'].BudgetMillions, 
 #movies[movies.Genre == 'Drama'].BudgetMillions,]

#plt.hist(movieFilterList, bins = 15, stacked = True)
#plt.show()

#Replace previous code with a more efficient for loop

list1 = list()
mylabels = list()
for gen in movies.Genre.cat.categories:
    print(gen)
    list1.append(movies[movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)
h = plt.hist(list1, bins = 30, stacked = True, rwidth=1, label=mylabels)
plt.legend() #need this so that the legend will appear
plt.show(h)