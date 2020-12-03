import imdb

moviesDB = imdb.IMDb()

# print(dir(moviesDB))
# print all movies of this name
movies = moviesDB.search_movie('inception')


print(f"Searching for the {movies}")
for movie in movies:
    title = movie['title']
    year = movie['year']
    kind = movie['kind']
    print(f"{title} - {year} - {kind}")
    print(f"{movies[0]}")

## to see the keys
# print(movies[0].keys())
print("******************")
# print one perticular movie with index
id = movies[0].getID()
movie = moviesDB.get_movie(id)
print(f"{movie} Info --")
title = movie['title']
year=movie['year']
rating = movie['rating']
directors = movie['directors']
casting = movie['cast']

print("----------")
print(f"{title} - {year}")
print(f"rating: {rating}")
# print(f"directors: {directors}")

directorStr = ' '.join(map(str, directors))
print(f"Directors: {directorStr}")

# actors = ', '.join(map(str, casting))
# print(f"Actors: {actors}")
print("------------")
print("Actors Info")



actorId = casting[0].getID()
person = moviesDB.get_person(actorId)
# bio = moviesDB.get_person_biography(actorId)

name = person['name']
birthDate = person['birth date']
height = person['height']


print(f"name: {name}")
print(f"birth date: {birthDate}")
print(f"height: {height}")

print("***********")

