# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:25:06 2017

@author: nauris
"""

import pandas as pd

# Load up the Servo.data dataset. Examine the headers, and adjust them as necessary, if need be.
file_path = 'C:/Users/nauris/Dropbox/docs/studies/eDx/Programming with Python for Data Science/DAT210x/Module2/Datasets/'

df= pd.read_csv(file_path + 'servo.data', 
                sep=',',
                names = ['motor', 'screw', 'pgain', 'vgain', 'class'])

df= pd.read_csv(file_path + 'servo.data', 
                sep=',')

len(df)

# Let's try experimenting with some slicing. 
# Create a slice that contains all entries that have a vgain equal to 5. 
#Then print the length of (# of samples in) that slice:

df[df.vgain == 5].shape
len(df[df.vgain == 5])


# Create a slice that contains all entries having a motor equal to E and screw equal to E. 
# Then print the length of (# of samples in) that slice:

df[(df.motor == 'E') & (df.screw == 'E')].shape
len(df[(df.motor == 'E') & (df.screw == 'E') ])


# Create a slice that contains all entries having a pgain equal to 4. 
# Use one of the various methods of finding the mean vgain value for the samples in that slice. 
# Once you've found it, print it:

df[df.pgain == 4].mean()

df['vgain'].loc[df.pgain==4].mean(axis=0)