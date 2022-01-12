#Homework 1: Law of large numbers
#############################################
#Background: 
# E(X) expected value
#sample size = n
#as you increase n, xbar_n (avg of samples)
#converges to E(X)
#recall randn calls a random number with a
#normal distribution within your range (w/in standard dev)
##############################################
#Assignemnt
#Test the law of large numbers for N random nomrally
#distributed numbers with mean = 0, stdev = 1.
#Create a Python script that will count how many of these
#numbers fall between -1 and 1, and divide by the total quantitiy N
#You know E(X) = 68.2%
#Check that Mean(X_n) -> E(X) as you rerun script while increasing N
###############################################
#My work: (can't get numpy to work so I'm just going to wing it)

import numpy as np
from numpy.random import randn
#imports numpy so that I can use function randn to generate random numbers

N = 10 #number of random numbers generated
jj = 0 #counts the numbers generated that are between -1 and 1
x = 1 #this will become the random number generated in each iteration
ii = 1 #initialize counter

for i in range(N): 
  x = randn()  #generate a random number. alternative: use rand(N) to generate N big array of random numbers *shrugs*
  if (x>-1 and x < 1):
    jj = jj+1
i = i+1

#calculates and prints out the percentage of numbers that fell between -1 and 1
percentage = (jj/N)*100
print(percentage, 'of the random numbers fell between -1 and 1')