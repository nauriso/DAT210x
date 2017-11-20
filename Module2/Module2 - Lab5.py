# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:05:53 2017

@author: nauris
"""

#Import and alias Pandas:
import pandas as pd

file_path = 'C:/Users/nauris/Dropbox/docs/studies/eDx/Programming with Python for Data Science/DAT210x/Module2/Datasets/'

# As per usual, load up the specified dataset, setting appropriate header labels.
df= pd.read_csv(file_path + 'census.data ', 
                sep=',',
                #na_values = '?',
                names = ['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification'])

# Now, use basic pandas commands to look through the dataset. Get a feel for it before proceeding!
# Do the data-types of each column reflect the values you see when you look through the data using a text editor / spread sheet program? 
# If you see object where you expect to see int32 or float64, that is a good indicator that there might be a string or missing value or erroneous value in the column.
df.dtypes
df.head()

df.capital-gain = pd.to_numeric(df.capital-gain, errors='coerce')

# Try use your_data_frame['your_column'].unique() or equally, your_data_frame.your_column.unique() 
# to see the unique values of each column and identify the rogue values.

df['education'].unique()
df['age'].unique()
df['capital-gain'].unique()
df['race'].unique()
df['capital-loss'].unique()
df['hours-per-week'].unique()
df['sex'].unique()
df['classification'].unique()

# Look through your data and identify any potential categorical features. 
# Ensure you properly encode any ordinal and nominal types using the methods discussed in the chapter.
# Be careful! Some features can be represented as either categorical or continuous (numerical). 
# If you ever get confused, think to yourself what makes more sense generally---to represent such features with a continuous numeric type... or a series of categories?

df.groupby(by = ['education']).count()
df.groupby(by = ['classification']).count()

ordered_classification = ['<=50K', '>50K']
df.classification = df.classification.astype("category",
                                             ordered = True,
                                             categories = ordered_classification
                                             ).cat.codes

ordered_education = ['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th', '12th', 'HS-grad', 'Some-college', 'Bachelors',  'Masters', 'Doctorate']
df.education = df.education.astype("category",
                                             ordered = True,
                                             categories = ordered_education
                                             ).cat.codes