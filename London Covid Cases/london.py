# -*- coding: utf-8 -*-
"""
Python ex3

Author: Giorgio Sala

Objective:
This program reads a csv file of Coronavirus cases per london borough and 
displays the data in a shapefile of london.  


Links:

To run this file, geopandas and its dependencies must be downloaded and installed. to do that, follow the instructions on
https://geopandas.org/install.html#creating-a-new-environment

The CSV file was downloaded from:
    
The shapefile was downloaded from: 


"""


import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#Read the CSV file and privot the table to easier analisis
district= pd.read_csv("phe_cases_london_boroughs.csv")

district = pd.pivot_table(district, values='total_cases', index=["NAME"], columns=['date'], aggfunc=np.sum)



london = gpd.read_file(r"/Users/giorgiosala/Documents/pe/map/londonb.shp")
london = london.drop(columns=["NAME","GSS_CODE","NONLD_AREA","LAGSSCODE","HECTARES"])
"""
#search for names that doesen't match between CSV file and SHP file ( I changed the not matching names in the CSV file )

for index,row in district.iterrows():
    if index not in london["DISTRICT"].to_list():
        print(index)
    else:
        pass
    

"""

#Merging "district" with "london" geopandas geodataframe
merge = london.join(district, on="DISTRICT", how="right")

#Plot
ax= merge.plot(column = "2020-12-13",
               figsize=(14,14),
               categorical=False,
               k=5, 
               cmap='OrRd', 
               linewidth=0.1,
               edgecolor='white', 
               legend=True
               )

























