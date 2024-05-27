#Python program to Display Movies : with Movies names
movie_names = ["The Lion King",'Titanic','pursuit of happyness','paddington','globe'] #Input List of Movies Names
print(movie_names) #Display the movie names
#using enumerate function to automatically count the loop staring 1 and display movie names
for count , movie_names in enumerate(movie_names, start = 1): 
   print(f"Movie {count}: {movie_names} ") #Display the output