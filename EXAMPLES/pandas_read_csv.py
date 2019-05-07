#!/usr/bin/env python
"""

@author: jstrick
Created on Sat May 18 11:36:57 2013

"""
import pandas as pd
from printheader import print_header

# data from
# http://www.rita.dot.gov/bts/sites/rita.dot.gov.bts/files/publications/
# national_transportation_statistics/html/table_01_44.html

airports_df = pd.read_csv('../DATA/airport_boardings.csv',thousands=',')

print_header("ENTIRE DATAFRAME")

print(airports_df, "\n")

print_header("ONLY COLUMN 'CODE'")
print(airports_df['Code'], "\n")

print_header("SELECTED COLUMNS WITH FILTERED ROWS")
columns_wanted = ['Code', '2001 Total', 'Airport']
sort_col = '2001 Total'
max_val = 20000000
selector = airports_df['2001 Total'] > max_val
print(airports_df[selector][columns_wanted])

print_header("COLUMN TOTALS")
print(airports_df[['2001 Total','2010 Total']].sum(), "\n")

print_header("'CODE' COLUMN SET AS INDEX")
airports_df.set_index('Code')
print(airports_df)
