#we need to intall pandas: in terminal I entered: pip3 install pandas, then restarted VisualSourceCode
import pandas as pd
#this structure is useful for working with data sets
#provides headers, etc for data organizing data
#has useful functions for organzing and dealing w. data

#specify full path to file (exact location)
#in Windows input:
#stats - pd.read_csv('C:\\Users\\Desktop\\etc etc')
#On Mac:
stats = pd.read_csv('/Users/hulseyvincentr/Python_code/WCC_Python/Section5/DemographicData.csv')
#(after I downloaded & converted file to .csv and saved in location)

#Another way to import data: Change workind directory
import os #don't need to do pip3 install bc already on Mac computer
print(os.getcwd()) 
print(len(stats))
#mess things up for fun: change directory
#os.chdir('/Users/hulseyvincentr/Desktop') #now it's on the Desktop
