#packages contain functions that you can use in your code :)
#A module is a file containing Python definitions, functions, and statements. 
#definitions define variables, functions execute actions, statements tell the
#code to perform a function (ex. print("done with processing"))
# It's useful becuase it lets you import module functionality into script

#a package is a collection of related modules, organized in a single tree-like
#hierarchy/structure. Complex packages have a directory to keep things organized

#how to put in packages
#1) find package
    #Check GitHub (repository of code)
#2) install package on machine
    #In Mac:
    #open terminal, type "pip install packagename" or "conda install packagename" 
    # (if in conda). Can do command T to open new terminal
    #in Windows: search window, find anaconda command window (if no anaconda, look for command line).
    #"conda install packagename" (packagename changes) or "pip install packagename"
#3) import package or import funcitons
    #import scrapy (installs entire package)
    #from scrapy,crawler import (installs specific function in package)

#find package on github, install in python
#type scrapy. (press tab), and you'll see the avaiable functions from that package
import scrapy
from scrapy.crawler import CrawlerProcess #this only imports the necessary module