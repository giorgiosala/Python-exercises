# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:16:33 2021

@author: giorgiosala
"""

import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

#Dictionary of the seasons
df={"1":24}

#Lists of the characters
Monica=[]
Chandler=[]
Joey=[]
Ross=[]
Rachel=[]
Phoebe=[]

#Key is the season number, value is the episode number
for key,value in df.items():
    episode=1
   
    #A while loop to go through all the episodes of a season
    while value!=0:

        #Extracting the text of a episode from the website
        url = 'https://fangj.github.io/friends/season/'+"{:02d}".format(int(key))+"{:02d}".format(int(episode))+'.html'
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        bold = soup.select("b, strong, [style*=bold]")
        bold_textonly = list(map(lambda tag: tag.text, bold))
        
        #Varaibles and for cycle to count the times a character spoke
        M=0
        C=0
        J=0
        R=0
        L=0
        P=0
        
        for i in bold_textonly:
            if ((str("Monica") in i) or (str("MONICA") in i)):
                M+=1
            elif str("Chandler") in i:
                C+=1
            elif str("Joey") in i:
                J+=1
            elif str("Ross") in i:
                R+=1
            elif str("Rachel") in i:
                L+=1
            elif str("Phoebe") in i:
                P+=1
           
            
        value-=1
        episode+=1
        
        #Appending the count to the appropriate list
        Monica.append(M)
        Chandler.append(C)
        Joey.append(J)
        Ross.append(R)
        Rachel.append(L)
        Phoebe.append(P)
        
"""
print(f"Monica: {Monica}")
"""

#Plotting the data of the lists


plt.plot(Monica,label = "Monica")
plt.plot(Chandler,label = "Chandler")
plt.plot(Joey,label = "Joey")
plt.plot(Ross,label = "Ross")
plt.plot(Rachel,label = "Rachel")
plt.plot(Phoebe,label = "Phoebe")
plt.xlim([0,33])
plt.ylim([0,70])
plt.legend()
plt.title("How many times each protagonist of FRIENDS \nspoke in each episode of season 1")

plt.show()
   


