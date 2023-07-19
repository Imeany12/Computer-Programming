# -*- coding: utf-8 -*-
"""HW3_6538094021.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iCy69o7y0Nssu5nkSQlv95MY-lPF-x1w

# Assignment #3: Movie Dictionary Database

In this problem, we aim to load movie data into a dictionary and summarize it by genre.

Please read all the details [here](https://docs.google.com/document/d/1FGQUzzsBuDdVCoW7nJG6IHDnlbJd58Q9BS76gMlS01A/edit?usp=sharing).

# **Important**
- Do not delete or modify the first line in the given code cell.
- You work must be add in the provided area only. 
- You must not change the declaration of the provided functions.
- You are allowed to add your own functions.
- If you want to write your own program to test, add new code cell at the very end of the file and add your code there.
"""

# Full data (import_movies.redis)
# !curl https://raw.githubusercontent.com/redis-developer/redis-datasets/movie-dataset/movie-database/import_movies.redis > import_movies.redis

file = open("import_movies.redis", encoding='utf8')
lines = file.readlines()
file.close()

# Small sample data (import_movies_small.redis)
# !curl https://dl.dropboxusercontent.com/s/id6d0qq7ks5y4b3/import_movies_small.redis > import_movies_small.redis

file = open("import_movies_small.redis", encoding='utf8')
lines = file.readlines()
file.close()



# # preview 10 movies
lines[:10]

# MOVIE_DICTIONARY (*** DO NOT DELETE this line or add line before this ***)
# Only add your code in the provided area.
# DO NOT delete or modified the given code in main().
def load_data_to_movie_dict(lines):
  movies = dict()
  # Your code here
  import shlex
  attribute={'title','genre','votes','rating','release_year','plot','poster','ibmdb_id'}
  for i in range(len(lines)):
    if lines[i].count('"')%2!=0:
      lines[i]+='"'
    line=shlex.split(lines[i].replace('HSET ','').replace('\\',''))
    id=int(line[0][6:])
    att={}
    for i in range(len(line)):
      if line[i] in attribute:
        if line[i]=='rating' or line[i]=='votes':
          att[line[i]]=float(line[i+1])
        elif line[i]=='release_year':
          att[line[i]]=int(line[i+1])
        else:
          att[line[i]]=line[i+1]
    movies[id]=att
  return movies

#------------------------------------------------------------#

def summarize_movies_by_genre(movies):
  movies_by_genre = dict()
  # Your code here
  for i in movies:
    if 'genre' in movies[i]:
      if movies[i]['genre'] not in movies_by_genre:
        movies_by_genre[movies[i]['genre']]=[i]
      else:
        movies_by_genre[movies[i]['genre']]+=[i]
        movies_by_genre[movies[i]['genre']].sort()
  return movies_by_genre

#------------------------------------------------------------#

def calcualte_genre_stats(movies, movies_by_genre):
  genre_stats = dict()
  # Your code here
  mbg=movies_by_genre
  for i in mbg:
    rating=0
    votes=0      
    num=len(mbg[i])
    temp={}
    for j in mbg[i]:
      rating+=movies[j]['rating']
      votes+=movies[j]['votes']
    temp['num']=len(mbg[i])
    temp['rating']=round(rating/len(mbg[i]),2)
    temp['votes']=round(votes/len(mbg[i]),2)
    genre_stats[i]=temp
  return genre_stats

#------------------------------------------------------------#    
# DO NOT DELETE OR MODIFIED THE CODE BELOW
#------------------------------------------------------------#

from collections import OrderedDict

# print "data" dict ordered by key
# if top is blank, print all members in the data
# if details is true, print detailed data
#   ; otherwise, print only the number of attributes
def print_ordered_dict(data, top='', details=True):
  if top == '':
    top = len(data)
  sorted_ids = sorted(data.keys())[:top]

  i = 0
  for id in sorted_ids:
    if details:
      print(id, data[id])
    else:
      print(id, len(data[id]))

#------------------------------------------------------------#
# *** MAIN PART ****
movies = load_data_to_movie_dict(lines)
movies_by_genre = summarize_movies_by_genre(movies)
genre_stats = calcualte_genre_stats(movies, movies_by_genre)

"""# Test you code

To speed up the testing of your program, some of test cases of some functions are given, but might not cover all possibilies.  You should add more test cases using provided test case as an example. 

Uncomment the test function that you want to test. You results should be similar to the expected output in [the Google Sheet here](https://docs.google.com/spreadsheets/d/1enpJps0zUN0SjZcgMPO9ijzgcDruyO2jsAHazWx1yhY/edit?usp=sharing).

**Important!!!** You must run the above code cell without any error before running the test.
"""

print(len(movies))
# print_ordered_dict(data=movies, top=200, details=False) # print attributes (Google Sheet1)
print_ordered_dict(data=movies, top=200, details=True) # print data (Google Sheet2)
 
print(len(movies_by_genre))
# print_ordered_dict(data=movies_by_genre, top=5, details=False) # print attributes (Google Sheet3)
# print_ordered_dict(data=movies_by_genre, top=5) # print data (Google Sheet4)
# print_ordered_dict(data=genre_stats, top=5) # print data (Google Sheet5)
