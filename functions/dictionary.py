# Define a dictionary to store information about the favorite book
favorite_book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction"
}

# Retrieve the genre using the get() method
book_genre = favorite_book.get("genre")

# Print the genre
print(book_genre)