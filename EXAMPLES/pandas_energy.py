#!/usr/bin/env python
"""

@author: jstrick
Created on Sat May 18 14:02:18 2013

"""
import sys
import numpy as np
import pandas as pd
from pandas.core.frame import Series, DataFrame


col_names = ['Desc',"1960","1965","1970","1975","1980","1985","1990","1991",
    "1992","1993","1994","1995","1996","1997","1998","1999","2000",
    "2001","2002","2003","2004","2005","2006","2007","2008","2009",
    "(R) 2010","2011"
]

df = pd.read_csv(
    '../DATA/energy_use_quad.csv',
    names = col_names,
    )

print(df, "\n")
print("-" * 60)
print(df[['Desc','2003']], "\n")

print(df[
     'Transportation as percent of total energy consumption',
])