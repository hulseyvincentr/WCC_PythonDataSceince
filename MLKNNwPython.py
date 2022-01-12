#import the necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


df = pd.read_csv('ClassifiedData.csv', index_col=0)
#print(df.head()) 

#the scale of the variable matters, this will affect the way KNN classifies data. Standardize the scaling using sklearn:
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() #create instance of standard 
scaler.fit(df.drop('TARGET CLASS', axis = 1)) #fit the scaler to all the feature columns
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis = 1)) #transform the data using the scaler, standardizes the data
print(scaled_features) #getting an error here - target glass not found in axis
