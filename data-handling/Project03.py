"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import os 
import json
import uuid




FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME,"r",encoding="utf-8") as f:
        return json.load(f)
    
def save_movie(movies):
    with open(FILENAME,"w",encoding="utf-8") as f:
        json.dump(movies, f, indent=2)

def add_movie(movies):
    title=input("Enetr movie title").strip().lower()
    if any(movie["title"]==title for movie in movies):
        print("Movie Already Exist!")
        return
    rating=int(input("Enter rating from 1-10!"))
    try:
        if not( 0<=rating<=10):
            raise ValueError
    except ValueError:
        print("Please enter valid number")
        return
    genre=input("Genre of Movie!").strip().lower()
    
    id = str(uuid.uuid4())
    
    movies.append({"id": id,"title": title, "genre": genre, "rating": rating})
    save_movie(movies)
    print("Movie added ✅")

def search_movies(movies):
    if len(movies)==0:
        print("DB Empty!")
        return
    term = input("Enter the title or genre: ").strip().lower()
    results = [
        movie for movie in movies 
        if term in movie['title'].lower() or term in movie['genre'].lower()
     
    ]
    if not results:
        print("No matching result")
        return
    for movie in results:
        print(f"{movie["id"]} -- {movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")
    
def view_database(movies):
    if len(movies)==0:
        print("DB Empty!")
        return
    for movie in movies:
         print("_"*50)
         print(f"{movie["id"]} -- {movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")
         print("_"*50)

def update_movie(movies):
    view_database(movies)
    movie_id = input("Just copy-paste the ID you want to update: ").strip()

    # Find the movie with this ID
    movie = next((m for m in movies if m["id"] == movie_id), None)

    if not movie:
        print("Movie not found!")
        return

    print("What do you want to update?")
    print("1. Title")
    print("2. Genre")
    print("3. Rating")

    choice = input("Choose an option (1-3): ").strip()

    match choice:
        case "1":
            new_title = input("Enter new title: ").strip().lower()
            if any(m["title"] == new_title for m in movies if m != movie):
                print("Movie Already Exists!")
                return
            movie["title"] = new_title

        case "2":
            new_genre = input("Enter new genre: ").strip().lower()
            movie["genre"] = new_genre

        case "3":
            try:
                new_rating = int(input("Enter rating from 1-10: "))
                if not (0 <= new_rating <= 10):
                    raise ValueError
                movie["rating"] = new_rating
            except ValueError:
                print("Please enter a valid number")
                return

        case _:
            print("Invalid choice")
            return

    save_movie(movies)
    print("Movie updated ✅")


def run_movie_db():
    movies = load_movies()

    while True:
        print("\n🍿 MyMovieDB")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4.Update Movies")
        print("5. Exit")
    
        choice = input("Choose an option (1-4): ").strip()
        match choice:
            case "1": add_movie(movies)
            case "2": view_database(movies)
            case "3": search_movies(movies)
            case "4": update_movie(movies)
            case "5": break
            case _: print("Enter valid choice") 


if __name__ == "__main__":
    run_movie_db()



    



