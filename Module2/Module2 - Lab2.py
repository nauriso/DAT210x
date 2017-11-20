# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:55:00 2017

@author: nauris
"""

# Import and alias Pandas
import pandas as pd

# Write code below to load up the tutorial.csv dataset. You can store it into a variable called df:
    
file_path = 'C:/Users/nauris/Dropbox/docs/studies/eDx/Programming with Python for Data Science/DAT210x/Module2/Datasets/'

# Write code below to load up the tutorial.csv dataset. You can store it into a variable called df:    
df= pd.read_csv(file_path + 'tutorial.csv', sep=',')

# Now that your dataset has been loaded, invoke the .describe() method to display some results about it:
df.describe()

# Lastly, try experimenting with indexing. Figure out which indexing method you would need to use 
# in order to index your dataframe with: [2:4, 'col3']. Finally, display the results:

df.loc[2:4, 'col3']
