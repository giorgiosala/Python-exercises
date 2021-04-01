# -*- coding: utf-8 -*-
"""
Author: Giorgio Sala

Objective:
This program reads a csv file of Coronavirus cases per london borough and 
displays the data in a shapefile of london.  


Libraries that must be installed to run the program:

- Geopandas and its dependencies must be downloaded and installed. (https://geopandas.org/install.html#creating-a-new-environment)
- Matplotlib
- Pandas
- Numpy
- Pillow

Mapclassify must be installed (in terminal: "pip install mapclassify")

The CSV file was downloaded from:
https://data.london.gov.uk/download/coronavirus--covid-19--cases/151e497c-a16e-414e-9e03-9e428f555ae9/phe_cases_london_boroughs.csv
The shapefile was downloaded from: 
https://data.london.gov.uk/download/statistical-gis-boundary-files-london/08d31995-dd27-423c-a987-57fe8e952990/London-wards-2018.zip

(QGIS 3.10 was used to merge all the districts of a borough in one single shape)


"""


import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import PIL
import io
import cv2

image_frame=[]
#Read the CSV file and pivot the table to easier analisis
district= pd.read_csv("phe_cases_london_boroughs.csv")

district = pd.pivot_table(district, values='new_cases', index=["area_name"], columns=['date'], aggfunc=np.sum)



london = gpd.read_file(r"/Users/giorgiosala/Documents/master/London Covid Cases/l.shp")
london = london.drop(columns=["NAME","GSS_CODE","NONLD_AREA","LAGSSCODE","HECTARES"])
"""
#search for names that doesen't match between CSV file and SHP file ( I changed the not matching names in the CSV file )

for index,row in district.iterrows():
    if index not in london["DISTRICT"].to_list():
        print(index)
    else:
        pass

"""
#Changed the names of the .shp to reflect the name in the database
london.replace("Hackney","Hackney and City of London",inplace=True)
london.replace("City of Westminster","Westminster",inplace=True)



    

#Merging "district" with "london" geopandas geodataframe
merge = london.join(district, on="DISTRICT", how="right")

for dates in merge.columns.to_list()[-30:]:
    #Plot
    print(dates)
    ax= merge.plot(column=dates,
                   figsize=[15,15], 
                   cmap='OrRd',
                   vmin=0,
                   vmax=40,
                   legend=True,
                   
                   edgecolor="black",
                   linewidth=0.4
                   )
    
    #assign name to shapes
    merge.apply(lambda x: ax.annotate(text=x.DISTRICT, xy=x.geometry.centroid.coords[0], ha='center'),axis=1);
    
    ax.set_axis_off()
    ax.set_title("New Covid Cases per London District \n\n"+ dates, fontsize=30 )
    
    
    
    img= ax.get_figure()
    
    f= io.BytesIO()
    img.savefig(f, format="png",bbox_inches="tight")
    f.seek(0)
    image_frame.append(PIL.Image.open(f))


#create a gif
image_frame[0].save("Dinamic covid 19 map of london.gif",format="GIF",
                     append_images= image_frame[1:],
                     save_all= True,
                     duration=300,
                     loop=0,
                     )




f.close()










