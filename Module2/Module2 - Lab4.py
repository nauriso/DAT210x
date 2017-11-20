# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 17:59:49 2017

@author: nauris
"""

#Module2 - Lab4

import pandas as pd
import numpy as np

# Load up the table from the link, and extract the dataset out of it. 
# If you're having issues with this, look carefully at the sample code provided in the reading:

url = 'http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2'
df_list = pd.read_html(url,
                       header = 0) # import as list
df = pd.read_html(url,
                  header = 1)[0] # import as dataframe

# Next up, rename the columns so that they are similar to the column definitions provided to you on the website. 
# Be careful and don't accidentally use any column names twice. 
# If a column uses special characters, you can replace them with regular characters to make it easier to work with:
                  
df.columns = ['RK', 'PLAYER', 'TEAM' , 'GP', 'G', 'A', 'PTS', '+/-', 
              'PIM', 'PTS/G', 'SOG', 'PCT', 'GWG',
              'PP_G', 'PP_A', 'SH_G', 'SH_A']


#Get rid of any row that has at least 4 NANs in it. 
# That is, any rows that do not contain player points statistics:

df = df.dropna(axis = 0, thresh=4)

# At this point, look through your dataset by printing it. 
# There probably still are some erroneous rows in there.
# remove rows, that contains column names
df = df.drop_duplicates(subset=['PLAYER']) # remove duplicatos
df = df[df['PLAYER'] != 'PLAYER']          # remove rows based on filter value


# Get rid of the 'RK' column:
df = df.drop('RK', axis = 1)

# Make sure there are no holes in your index by resetting it. 
# There is an example of this in the reading material. By the way, drop the original index.

df = df.reset_index(drop=True)

# Check the data type of all columns, and ensure those that should be numeric are numeric.
df.dtypes
#convert to integers
cols_to_int = ['GP', 'G', 'A', 'PTS', '+/-', 
              'PIM', 'SOG',
              'GWG', 'PP_G', 'PP_A', 'SH_G', 'SH_A']

df[cols_to_int] = df[cols_to_int].apply(pd.to_numeric, 
                  errors = 'coerce',
                  axis = 1)

#convert to float
cols_to_float = ['PTS/G', 'PCT']

df[cols_to_float] = df[cols_to_float].apply(pd.to_numeric, 
                  errors = 'coerce',
                  axis = 1)
#After completing the 6 steps above, how many rows remain in this dataset? (
# Not to be confused with the index!)
len(df)
df.shape

# How many unique PCT values exist in the table?
df.PCT.nunique()

# What is the value you get by adding the GP values at indices 15 and 16 of this table?

df.ix[15:16, 'GP'].sum()
df.loc[15:16, 'GP'].sum()
