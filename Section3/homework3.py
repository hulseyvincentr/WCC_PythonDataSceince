#Background:
#finanacial statement of organisation X
#you have 2 lists of data: monthly revanue and
#and monthly expenses for the given financial year.
################################################################
#Assignment:
#Determine the following metrics:
#-Profit for each month
#-Profit for each month after tax (tax rate is 30%)
#- profit margin for each month: profit after tax/revanue
#-bad months: where profit after tax < mean for the year
#- best month: profit after tax was max for the year
#- worst month: profit after tax was min for the year

#all reuslts need to be presented as lists
#Results for dollar values need to be calculated with $0.01
#precision, but need to be present in units of $1,000 with 
#with no decimal places

#results of profit margin ratio need to be presented in units
#of % with no decimal points

#it is ok for tax of any given month to be negative
#(this indicates deferred tax asset)

################################################################
#Hint:
#operating on array elements from arrays
#a = [1, 2, 3]
# b = [4, 5, 6]
#ab = []
#for i in range(0 len(a));
#   ab.apend(a[i]*b[i]) #append puts results of mult. in new array
#ab

#List comprehension iterates through each element of a
#doubled_a = [i*2 for i in a]
#doubled_a

#new functions to use:
#round()
#max()
#min()

#####################################################################################################################################
#My work:
import numpy as np #usd for mean function
import math as math  #use this to  generate NaN when initializing variables

revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#initialize variables and arrays for storing variables
profit = []
profit_display = []
profit_post_tax = []
profit_post_tax_display = []
profit_margin = []
profit_margin_display = []
bad_months = []
best_month = []
worst_month = []
tax_rate = 0.3
mean_profit = math.nan #just a place holdin "not a number" that will be later calculated and filled
mean_profit_display = []
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
#find lengths of arrays to ensure calculations can be executed
len_revenue = len(revenue)
len_expenses = len(expenses)
len_data = len_revenue

#determine profits for each month:
#check that revenue and expense lists are same length
if len_revenue == len_expenses and len_revenue == len(months):
    #find the profit for each month
    print("Lists are the same lengths :)")
    for i in range(len_data):
        profit.append(revenue[i]-expenses[i]) #find profit (revenue - expenses) for each month
        profit_display.append(str(int(round(revenue[i]-expenses[i], -3)))+ "k" )
        
        profit_post_tax.append(round(profit[i]*(1-tax_rate), -3))#find post-tax profit
        profit_post_tax_display.append(str(int(round(profit[i]*(1-tax_rate), -3))) + "k") #for display
        
        #check profit_post_tax to make sure they're what I expect
        
        
        profit_margin.append(profit_post_tax[i]/revenue[i])#find profit margin in percent
        profit_margin_display.append(str(int(round(profit_post_tax[i]/revenue[i]))) + "%")
        
# need to make separate display vs. math array
    max_profit = max(profit_post_tax) #find max profit
    min_profit = min(profit_post_tax) #find min profit
    mean_profit = np.mean(profit_post_tax) #find the mean profit
    mean_profit_display.append(str(int(round(mean_profit, -3))) + "k") #make it display-able
    
    for j in range(len_data):
        if profit_post_tax[j] == max_profit: #use month array to name best month
            best_month.append(months[j])
        elif profit_post_tax[j] < mean_profit: #find bad months (profit < mean profit)
            bad_months.append(months[j])    
            if profit_post_tax[j] == min_profit: #use month array to name worst month
                 worst_month.append(months[j])            
else:
     print("Revenue and expenses lists do not have the same lengths, calculations cannot be made.")

#print out results:
print("Profit each month: ", profit_display)
print("Profit post tax each month: ", profit_post_tax_display)
print("Profit margin each month in units of %: ", profit_margin_display)
print("Mean profit for the year: ", mean_profit_display)
print("Bad months: ", bad_months)
print("The maximum profit was ", max_profit, " in ", best_month[0])
print("The minimum profit was ", min_profit, " in ", worst_month[0])