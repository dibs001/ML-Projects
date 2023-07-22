#time series property
# introduction
# creating objects
# selection
# data manipulation
# data duping
# working with text data
# operations 
# visualization
# csv excel file
# panda refers to an open source lib that is built on top of numpy lib. This offers various data structures and operations for manipulating numerical data and time series.This is popular for importing and analysing data and it has high performance and productivity. It has been dev. by Mc Kinney.MemoryErrorfast efficient for data analysis. Data from diff file objs can be loaded easy handling of missing data in floating pt as well as non floating pt. Size mutability--> colms can be inserted and deleted from data frame and  higher dim. objects. 
# Data set merging and joining, flexible reshaping and pivoting of data sets provides time series functionality.Powerful groupby functionality for performing split applied combined operations on data sets. 
import pandas as pd
import numpy as np
ser=pd.Series();
print (ser)
data=np.array(['a','b','c','d'])
ser=pd.Series(data)
print(ser)
