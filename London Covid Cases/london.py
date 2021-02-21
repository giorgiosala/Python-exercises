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
import PIL
import io

image_frame=[]
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

for dates in merge.columns.to_list()[2:]:
    #Plot
    ax= merge.plot(column = dates,
                   figsize=(20,20),
                   vmin = 0,
                   vmax = 35000,
                   cmap='OrRd', 
                   linewidth=0.1,
                   legend_kwds={'shrink': 0.5,},
                   edgecolor='black', 
                   legend=True
                   )
    
    #assign name to shapes
    merge.apply(lambda x: ax.annotate(s=x.DISTRICT, xy=x.geometry.centroid.coords[0], ha='center'),axis=1);
    
    ax.set_axis_off()
    ax.set_title("Total Covid Cases per London District \n\n"+ dates, fontsize=30 )
    
    
    
    img= ax.get_figure()
    
    f= io.BytesIO()
    img.savefig(f, format="png")
    f.seek(0)
    image_frame.append(PIL.Image.open(f))


#create a gif
image_frame[0].save("Dinamic covid 19 map of london.gif",format="GIF",
                     append_images= image_frame[1:],
                     save_all= True,
                     duration=300,
                     loop=1,
                     )



f.close()











