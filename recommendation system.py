# Simple Recommendation System

movies = [
    {"name": "Avengers", "genre": "action"},
    {"name": "Fast and Furious", "genre": "action"},
    {"name": "The Notebook", "genre": "romance"},
    {"name": "Titanic", "genre": "romance"},
    {"name": "Conjuring", "genre": "horror"},
    {"name": "Annabelle", "genre": "horror"},
    {"name": "Interstellar", "genre": "sci-fi"},
    {"name": "Inception", "genre": "sci-fi"},
    {"name": "Toy Story", "genre": "animation"},
    {"name": "Frozen", "genre": "animation"}
]

print("===== Movie Recommendation System =====")

print("\nAvailable Genres:")
print("1. Action")
print("2. Romance")
print("3. Horror")
print("4. Sci-Fi")
print("5. Animation")

choice = input("\nEnter your preferred genre: ").lower()

print("\nRecommended Movies:")

found = False

for movie in movies:
    if movie["genre"] == choice:
        print("-", movie["name"])
        found = True

if not found:
    print("Sorry, no movies found for this genre.")

print("\nThank you!")