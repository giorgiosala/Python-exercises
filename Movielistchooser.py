#reading files
import random
import os

movielist = []




def insert_title():

    movie_title = 0
    
    #A while loop to keep inserting movie titles until "stop"
    while movie_title != "stop":
        print('Please insert a movie title. To stop the insertions, write "stop" ')
        movie_title = input()
        
        #if stop is in the input, it doesent get written in movielist
        if movie_title != "stop":
            movielist.append(movie_title)
            print(movielist)
        else:
            break
    return movielist
     
try:
    #controls if the file is exist or not
    if os.path.exists('movie.txt'):
        
        #open the movie.txt file and inserts every element into a list
        f = open("movie.txt", "r+")
        for line in f:
            movielist.append(line)
            
        #count the lenght of the movielist
        count_movie = len(movielist)
        [ i.strip('[]') if type(i) == str else str(i) for i in movielist]
        #assign a random number to "m"
        m = random.randint(0, count_movie - 1)
        print(f"I choose for you:\n--> {movielist[m]}")
        
        #deletes the movie randomly chosen from the list
        del(movielist[m])  
        #eliminate everything on the list
        f.truncate(0)
        #write the movielist updated into txt 
        f.write("".join(str(item) for item in movielist))   
    else:
        print ("The list of movies does not exists.")
        f = open("movie.txt", "w")
        insert_title()
        #write the list in the txt file
                
    
        f.write("\n".join(str(i) for i in movielist))
    
        print("reopen the program")

except:
    print("The movie list file is empty. To insert a new movie title modify the file or delete the file and run this program again")
    
finally:
    f.close()
